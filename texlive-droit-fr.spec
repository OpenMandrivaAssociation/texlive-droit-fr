%global tl_name droit-fr
%global tl_revision 39802

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Document class and bibliographic style for French law
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/droit-fr
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/droit-fr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/droit-fr.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides a toolkit intended for students writing a thesis in
French law. It features: a LaTeX document class; a bibliographic style
for BibLaTeX package; a practical example of french thesis document; and
documentation. The class assumes use of biber and BibLaTeX.

