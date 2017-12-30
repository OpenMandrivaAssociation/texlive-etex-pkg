# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/etex-pkg/etex.sty
# catalog-date 2009-07-22 12:43:06 +0200
# catalog-license other-free
# catalog-version 2.0
Name:		texlive-etex-pkg
Version:	2.7
Release:	1
Summary:	E-TeX support package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/etex-pkg/etex.sty
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etex-pkg.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etex-pkg.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a straightforward interface to many of the
extensions offered by e-TeX; in particular, it modifies LaTeX's
register allocation macros to make use of the extended register
range. The etoolbox and etextools packages provide macros that
make more sophisticated use of e-TeX's facilities.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/etex-pkg/etex.sty
%doc %{_texmfdistdir}/doc/latex/etex-pkg/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.0-2
+ Revision: 751587
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.0-1
+ Revision: 718376
- texlive-etex-pkg
- texlive-etex-pkg
- texlive-etex-pkg
- texlive-etex-pkg

