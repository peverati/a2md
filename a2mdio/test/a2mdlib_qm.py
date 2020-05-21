from a2mdio.qm import GaussianLog
from a2mdtest.a2mdtests import aca
if __name__ == '__main__':

    gl = GaussianLog(
        file='ATA_000000.g09.output', method='dft-mPW3PBE',
        charges='MK', ep=False
    )
    out_dict = gl.read()

    gl = GaussianLog(
        file=aca.out, method='MP2',
        charges='NPA', ep=False
    )
    out_dict = gl.read()

    print('DONE!')