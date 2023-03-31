Name:		texlive-etex-pkg
Version:	41784
Release:	2
Summary:	E-TeX support package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/etex-pkg/etex.sty
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etex-pkg.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etex-pkg.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
