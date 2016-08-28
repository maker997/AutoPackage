import  os
import sys
#[说明]:这个打包普通的项目,用 cocoapod 管理的不能用.(更改一点也能用)

# 一.声明好路径
#项目文件夹的路径(换成自己项目的路径)
project_path = '/Users/xxx/Desktop/xxx'

#编译成功之后.app文件的路径(换成自己项目的路径)
app_path = '/Users/xxx/Desktop/xxx/build/Release-iphoneos/xxx.app'

#打包好 IPA 路径
targerIPA_parth = "/Users/xxx/Desktop"


# 二.clean 项目
def clean_project_mkdir_build():
    os.system('cd %s;xcodebuild clean' % project_path) # clean 项目
    os.system('cd %s;mkdir build' % project_path)      # 创建build文件夹

# 三.编译项目
def build_project():
    print("build release start")
    os.system ('cd %s;xcodebuild build' % project_path )

# 四.打包
def build_ipa():
    print('build_ipaing...')
    global ipa_filename
    ipa_filename = 'skin.ipa'#ipa文件名换成你自己的
    os.system ('xcrun -sdk iphoneos PackageApplication -v %s -o %s/%s' % (app_path,targerIPA_parth,ipa_filename))

# 主函数 调用
def main():
    # 清理并创建build目录
    clean_project_mkdir_build()
    # 编译coocaPods项目文件并 执行编译目录
    build_project()
    # 打包ipa 并制定到桌面
    build_ipa()
    
if __name__ == '__main__':
    main()
