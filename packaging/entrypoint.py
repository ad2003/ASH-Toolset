"""Windows launcher with a CI-only functional check for the frozen bundle."""
import json
from pathlib import Path
import sys
import tempfile
import traceback


def smoke_test():
    import sqlite3
    import numpy as np
    import soundfile as sf
    from ash_toolset import constants as cn, hpcf_functions as hp

    with sqlite3.connect(f'file:{cn.DATABASE_ASH_DIR}?mode=ro', uri=True) as conn:
        headphones = hp.get_all_headphone_list(conn)
        assert headphones, 'Bundled database is empty'
        filters = hp.get_hpcf_samples_dicts(conn, headphones[0])
        assert filters and np.isfinite(filters[0]['fir']).all()
        with tempfile.TemporaryDirectory() as output:
            assert hp.hpcf_to_file(filters[0], output, hesuvi_export=False)
            wavs = list(Path(output).rglob('*.wav'))
            assert len(wavs) >= 2, 'Missing mono/stereo WAV exports'
            for wav in wavs:
                samples, rate = sf.read(wav)
                assert samples.size and rate == cn.SAMP_FREQ
                assert np.isfinite(samples).all()
    # Exercise startup and the actual rendering backend before exiting normally.
    import dearpygui.dearpygui as dpg
    from ash_toolset.__main__ import main

    def render_frames():
        assert dpg.does_item_exist('Primary Window')
        for _ in range(5):
            dpg.render_dearpygui_frame()

    dpg.start_dearpygui = render_frames
    main()
    return {'status': 'passed', 'headphones': len(headphones), 'gui_frames': 5}


if __name__ == '__main__':
    if '--smoke-test' in sys.argv:
        report = Path(sys.argv[sys.argv.index('--smoke-output') + 1])
        try:
            result = smoke_test()
        except Exception:
            report.write_text(json.dumps({'status': 'failed', 'error': traceback.format_exc()}))
            raise
        report.write_text(json.dumps(result))
    else:
        from ash_toolset.__main__ import main
        main()
