import os

os.system('E:/simcity/VisBuildPro8/VisBuildCmd.exe "build_type=release" "workdir=E:/simcity/trunk/client" "target=Android_prod" "server_name=Prod" "IsBuildData=1" "commit_versioninfo=0" "compile_code=1" ../project/ibcs_main_build.bld')
os.system('E:/simcity/VisBuildPro8/VisBuildCmd.exe "build_type=qa" "workdir=E:/simcity/trunk/client" "target=Android_latest" "server_name=Kingsoft" "IsBuildData=0" "commit_versioninfo=0" "compile_code=1" ../project/ibcs_main_build.bld')
os.system('E:/simcity/VisBuildPro8/VisBuildCmd.exe "build_type=qa" "workdir=E:/simcity/trunk/client" "target=Android_prod_qa" "server_name=Prod" "IsBuildData=0" "commit_versioninfo=0" "compile_code=0" ../project/ibcs_main_build.bld')
os.system('E:/simcity/VisBuildPro8/VisBuildCmd.exe "build_type=dev" "workdir=E:/simcity/trunk/client" "target=Android_dev" "server_name=Dev" "IsBuildData=0" "commit_versioninfo=1" "compile_code=0" ../project/ibcs_main_build.bld')
os._exit(0)
