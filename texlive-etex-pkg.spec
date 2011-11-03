# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/etex-pkg/etex.sty
# catalog-date 2009-07-22 12:43:06 +0200
# catalog-license other-free
# catalog-version 2.0
Name:		texlive-etex-pkg
Version:	2.0
Release:	1
Summary:	E-TeX support package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/etex-pkg/etex.sty
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etex-pkg.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etex-pkg.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
The package provides a straightforward interface to many of the
extensions offered by e-TeX; in particular, it modifies LaTeX's
register allocation macros to make use of the extended register
range. The etoolbox and etextools packages provide macros that
make more sophisticated use of e-TeX's facilities.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/etex-pkg/etex.sty
%doc %{_texmfdistdir}/doc/latex/etex-pkg/README
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
