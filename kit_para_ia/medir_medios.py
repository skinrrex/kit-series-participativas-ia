"""Usage: python medir_medios.py FILE [FILE ...]. Requires ffprobe on PATH."""
import json, subprocess, sys
from pathlib import Path
for arg in sys.argv[1:]:
    file=Path(arg)
    result=subprocess.run(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(file)],capture_output=True,text=True,encoding='utf-8')
    if result.returncode:
        print(json.dumps({'archivo':str(file),'error':result.stderr},ensure_ascii=False)); continue
    data=json.loads(result.stdout)
    print(json.dumps({'archivo':str(file),'duracion_s':data.get('format',{}).get('duration'),'streams':[{k:s.get(k) for k in ['codec_type','codec_name','width','height','avg_frame_rate','sample_rate','channels']} for s in data['streams']]},ensure_ascii=False))
