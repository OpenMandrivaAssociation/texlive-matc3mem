# revision 29894
# category Package
# catalog-ctan /macros/latex/contrib/matc3mem
# catalog-date 2013-04-14 10:19:50 +0200
# catalog-license lppl1.3
# catalog-version 1.0.2
Name:		texlive-matc3mem
Version:	1.0.2
Release:	3
Summary:	Class for MatematicaC3 textbooks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/matc3mem
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/matc3mem.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/matc3mem.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/matc3mem.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class is a development of memoir, with additions
(specifically, mathematical extensions) that provide support
for writing the books for the Matematica C3 project to produce
free mathematical textbooks for use in Italian high schools.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/matc3mem/matc3mem.cls
%doc %{_texmfdistdir}/doc/latex/matc3mem/Makefile
%doc %{_texmfdistdir}/doc/latex/matc3mem/README
%doc %{_texmfdistdir}/doc/latex/matc3mem/matc3mem.pdf
#- source
%doc %{_texmfdistdir}/source/latex/matc3mem/matc3mem.dtx
%doc %{_texmfdistdir}/source/latex/matc3mem/matc3mem.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
