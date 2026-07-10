%global tl_name etex-pkg
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.7
Release:	%{tl_revision}.1
Summary:	E-TeX support package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/etex-pkg
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/etex-pkg.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/etex-pkg.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides support for LaTeX documents to use many of the
extensions offered by e-TeX; in particular, it modifies LaTeX's register
allocation macros to make use of the extended register range. The
etextools package provides macros that make more sophisticated use of
e-TeX's facilities.

