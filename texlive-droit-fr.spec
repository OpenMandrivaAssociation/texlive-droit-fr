# revision 32918
# category Package
# catalog-ctan /macros/latex/contrib/droit-fr
# catalog-date 2014-02-08 13:46:42 +0100
# catalog-license lppl1.3
# catalog-version 0.4
Name:		texlive-droit-fr
Version:	0.4
Release:	4
Summary:	Document class and bibliographic style for French law
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/droit-fr
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/droit-fr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/droit-fr.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/droit-fr/droit-fr.bbx
%{_texmfdistdir}/tex/latex/droit-fr/droit-fr.cbx
%{_texmfdistdir}/tex/latex/droit-fr/droit-fr.cls
%doc %{_texmfdistdir}/doc/latex/droit-fr/.latexmkrc
%doc %{_texmfdistdir}/doc/latex/droit-fr/CHANGELOG
%doc %{_texmfdistdir}/doc/latex/droit-fr/README
%doc %{_texmfdistdir}/doc/latex/droit-fr/droit-fr.pdf
%doc %{_texmfdistdir}/doc/latex/droit-fr/droit-fr.tex
%doc %{_texmfdistdir}/doc/latex/droit-fr/example/.latexmkrc
%doc %{_texmfdistdir}/doc/latex/droit-fr/example/annexes.tex
%doc %{_texmfdistdir}/doc/latex/droit-fr/example/bibliographie.bib
%doc %{_texmfdistdir}/doc/latex/droit-fr/example/bibliographie.tex
%doc %{_texmfdistdir}/doc/latex/droit-fr/example/conclusion.tex
%doc %{_texmfdistdir}/doc/latex/droit-fr/example/glossaire.tex
%doc %{_texmfdistdir}/doc/latex/droit-fr/example/index.tex
%doc %{_texmfdistdir}/doc/latex/droit-fr/example/introduction.tex
%doc %{_texmfdistdir}/doc/latex/droit-fr/example/journaux.bib
%doc %{_texmfdistdir}/doc/latex/droit-fr/example/main.tex
%doc %{_texmfdistdir}/doc/latex/droit-fr/example/misc.tex
%doc %{_texmfdistdir}/doc/latex/droit-fr/example/partie1.tex
%doc %{_texmfdistdir}/doc/latex/droit-fr/example/partie2.tex
%doc %{_texmfdistdir}/doc/latex/droit-fr/example/sommaire.tex
%doc %{_texmfdistdir}/doc/latex/droit-fr/example/titre.tex
%doc %{_texmfdistdir}/doc/latex/droit-fr/example/toc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
