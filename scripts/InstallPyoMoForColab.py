def install_pyomo:
    !pip install -q pyomo

def install_glpk:
    !apt-get install -y -qq glpk-utils

def install_cbc:
    !apt-get install -y -qq coinor-cbc

def instll_ipopt:
    !wget -N -q "https://ampl.com/dl/open/ipopt/ipopt-linux64.zip"
    !unzip -o -q ipopt-linux64

def install_bonmin:
    !wget -N -q "https://ampl.com/dl/open/bonmin/bonmin-linux64.zip"
    !unzip -o -q bonmin-linux64

def install_couenne():
    !wget -N -q "https://ampl.com/dl/open/couenne/couenne-linux64.zip"
    !unzip -o -q couenne-linux64

def install_gecode():
    !wget -N -q "https://ampl.com/dl/open/gecode/gecode-linux64.zip"
    !unzip -o -q gecode-linux64