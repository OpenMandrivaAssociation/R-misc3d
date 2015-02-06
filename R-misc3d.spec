%global packname  misc3d
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.8.4
Release:          2
Summary:          Miscellaneous 3D Plots
Group:            Sciences/Mathematics
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/misc3d_0.8-4.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-rgl R-tkrplot R-MASS 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    R-rgl R-tkrplot R-MASS 

%description
A collection of miscellaneous 3d plots, including isosurfaces.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if 0
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/help


%changelog
* Sat Feb 18 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.8_2-1
+ Revision: 776390
- Import R-misc3d
- Import R-misc3d


