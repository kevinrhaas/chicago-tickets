import os,sys,pathlib,json
sys.path.insert(0,'/workspace/shared')
import owned_child_reaper_20261023 as owned
owned.enable()
p=pathlib.Path('/workspace/shared/T2800-STALE-LAP-DIAGNOSTIC-G10-20261023')
env=os.environ.copy()
env['PATH']='/workspace/shared/w01-python-sum-recovery-20261022/venv311/bin:/workspace/shared/chicago-tools/usr/bin:'+env['PATH']
env.update(CHECK_JOBS='1',NODE_OPTIONS='--v8-pool-size=1 --disable-sigusr1',UV_THREADPOOL_SIZE='1',GOMAXPROCS='1',GIT_CONFIG_COUNT='3',GIT_CONFIG_KEY_0='index.threads',GIT_CONFIG_VALUE_0='1',GIT_CONFIG_KEY_1='pack.threads',GIT_CONFIG_VALUE_1='1',GIT_CONFIG_KEY_2='core.preloadIndex',GIT_CONFIG_VALUE_2='false')
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','VECLIB_MAXIMUM_THREADS']: env[key]='1'
try:
 for name,cmd,cwd,timeout in [
  ('diagnostic',['bash','/workspace/shared/T2800-LAP-LOCK-SERIAL-DEPTH-FOCUSED-ACTUAL-20261023/same-two-shell-depth.sh',str(p/'diagnostic.mjs')],'/workspace/chicago-waistcoat/chicago/4d',120)]:
  r=owned.run(cmd,cwd,env,p/(name+'.log'),timeout)
  (p/(name+'.json')).write_text(json.dumps(r,indent=2))
  print(name,json.dumps(r),flush=True); print((p/(name+'.log')).read_text(),flush=True)
  if r['returncode']!=0 and name!='claim': raise SystemExit(r['returncode'])
finally:
 r=owned.finish(); (p/'cleanup.json').write_text(json.dumps(r)); print('cleanup',r,flush=True)
