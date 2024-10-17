Name:		texlive-droit-fr
Version:	39802
Release:	2
Summary:	Document class and bibliographic style for French law
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/droit-fr
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/droit-fr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/droit-fr.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides a toolkit intended for students writing a
thesis in French law. It features: a LaTeX document class; a
bibliographic style for Biblatex package; a practical example
of french thesis document; and documentation. The class assumes
use of biber and biblatex.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/droit-fr
%doc %{_texmfdistdir}/doc/latex/droit-fr

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
