Name:		texlive-matc3mem
Version:	35773
Release:	1
Summary:	Class for MatematicaC3 textbooks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/matc3mem
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/matc3mem.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/matc3mem.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/matc3mem.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
