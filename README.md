# 使用教程

## 环境

ubuntu 22.04
gnuradio 3.10.11.0

## 安装步骤

gnuradio安装请参考[https://wiki.gnuradio.org/index.php?title=LinuxInstall#From_Source](https://wiki.gnuradio.org/index.php?title=LinuxInstall#From_Source)
请从From source开始看起，按照依赖项->uhd->volk->gnuradio的顺序安装
最后需要按照[https://wiki.gnuradio.org/index.php?title=ModuleNotFoundError#B._Finding_the_Python_library](https://wiki.gnuradio.org/index.php?title=ModuleNotFoundError#B._Finding_the_Python_library)设置你的python环境变量

通过在python中输入`import gnuradio`来检查环境变量是否设置成功

## How to run

### build && install

```shell
cd /gr-rfid/
mkdir build
cd build
cmake ..
make
sudo make install
sudo ldconfig
```

`if you want to konw whether the module is installed successfully, you can run the following command`

```shell
python
from gnuradio import rfid
```

`if there is no error, the module is installed successfully`

### run in gnuradio-companion

1. open gnuradio-companion in shell, because the wirite in to system serial port need root permission
2. change file_path in file_source module block to your file path
3. run the flow graph 