#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-waldo
Version  : 0.2.3
Release  : 2
URL      : https://cran.r-project.org/src/contrib/waldo_0.2.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/waldo_0.2.3.tar.gz
Summary  : Find Differences Between R Objects
Group    : Development/Tools
License  : MIT
Requires: R-cli
Requires: R-diffobj
Requires: R-fansi
Requires: R-glue
Requires: R-rematch2
Requires: R-rlang
Requires: R-tibble
BuildRequires : R-cli
BuildRequires : R-diffobj
BuildRequires : R-fansi
BuildRequires : R-glue
BuildRequires : R-rematch2
BuildRequires : R-rlang
BuildRequires : R-tibble
BuildRequires : buildreq-R

%description
differences.  Designed particularly for use in testing packages where
    being able to quickly isolate key differences makes understanding test
    failures much easier.

%prep
%setup -q -c -n waldo
cd %{_builddir}/waldo

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610308107

%install
export SOURCE_DATE_EPOCH=1610308107
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library waldo
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library waldo
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library waldo
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc waldo || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/waldo/DESCRIPTION
/usr/lib64/R/library/waldo/INDEX
/usr/lib64/R/library/waldo/LICENSE
/usr/lib64/R/library/waldo/Meta/Rd.rds
/usr/lib64/R/library/waldo/Meta/features.rds
/usr/lib64/R/library/waldo/Meta/hsearch.rds
/usr/lib64/R/library/waldo/Meta/links.rds
/usr/lib64/R/library/waldo/Meta/nsInfo.rds
/usr/lib64/R/library/waldo/Meta/package.rds
/usr/lib64/R/library/waldo/NAMESPACE
/usr/lib64/R/library/waldo/NEWS.md
/usr/lib64/R/library/waldo/R/waldo
/usr/lib64/R/library/waldo/R/waldo.rdb
/usr/lib64/R/library/waldo/R/waldo.rdx
/usr/lib64/R/library/waldo/help/AnIndex
/usr/lib64/R/library/waldo/help/aliases.rds
/usr/lib64/R/library/waldo/help/paths.rds
/usr/lib64/R/library/waldo/help/waldo.rdb
/usr/lib64/R/library/waldo/help/waldo.rdx
/usr/lib64/R/library/waldo/html/00Index.html
/usr/lib64/R/library/waldo/html/R.css
/usr/lib64/R/library/waldo/tests/testthat.R
/usr/lib64/R/library/waldo/tests/testthat/_snaps/compare-value.md
/usr/lib64/R/library/waldo/tests/testthat/_snaps/compare.md
/usr/lib64/R/library/waldo/tests/testthat/f2.R
/usr/lib64/R/library/waldo/tests/testthat/test-compare-atomic.txt
/usr/lib64/R/library/waldo/tests/testthat/test-compare-attr-1.txt
/usr/lib64/R/library/waldo/tests/testthat/test-compare-chr.txt
/usr/lib64/R/library/waldo/tests/testthat/test-compare-class.R
/usr/lib64/R/library/waldo/tests/testthat/test-compare-class.txt
/usr/lib64/R/library/waldo/tests/testthat/test-compare-fun.txt
/usr/lib64/R/library/waldo/tests/testthat/test-compare-lang.txt
/usr/lib64/R/library/waldo/tests/testthat/test-compare-list.txt
/usr/lib64/R/library/waldo/tests/testthat/test-compare-opts.R
/usr/lib64/R/library/waldo/tests/testthat/test-compare-r6.txt
/usr/lib64/R/library/waldo/tests/testthat/test-compare-s3-weird.txt
/usr/lib64/R/library/waldo/tests/testthat/test-compare-s3.txt
/usr/lib64/R/library/waldo/tests/testthat/test-compare-s4.txt
/usr/lib64/R/library/waldo/tests/testthat/test-compare-value-chr.txt
/usr/lib64/R/library/waldo/tests/testthat/test-compare-value-lines.txt
/usr/lib64/R/library/waldo/tests/testthat/test-compare-value-num.txt
/usr/lib64/R/library/waldo/tests/testthat/test-compare-value.R
/usr/lib64/R/library/waldo/tests/testthat/test-compare.R
/usr/lib64/R/library/waldo/tests/testthat/test-diff-element-wise.txt
/usr/lib64/R/library/waldo/tests/testthat/test-diff-paired.txt
/usr/lib64/R/library/waldo/tests/testthat/test-diff-side-by-side.txt
/usr/lib64/R/library/waldo/tests/testthat/test-diff.R
/usr/lib64/R/library/waldo/tests/testthat/test-num_equal.R
/usr/lib64/R/library/waldo/tests/testthat/test-ses.R
