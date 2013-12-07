# revision 23164
# category Package
# catalog-ctan /language/malayalam
# catalog-date 2007-11-17 22:03:55 +0100
# catalog-license lppl
# catalog-version 0.9.6
Name:		texlive-malayalam
Version:	0.9.6
Release:	4
Summary:	LaTeX for Malayalam
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/malayalam
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/malayalam.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/malayalam.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/malayalam.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Fonts (in Adobe Type 1 format), metrics and macros for
typesetting Malayalam with LaTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/malayalam/effects/effect.mf
%{_texmfdistdir}/fonts/source/public/malayalam/effects/esoteric.mf
%{_texmfdistdir}/fonts/source/public/malayalam/effects/hstripes.mf
%{_texmfdistdir}/fonts/source/public/malayalam/effects/malayalam-reverse.mf
%{_texmfdistdir}/fonts/source/public/malayalam/effects/outline.mf
%{_texmfdistdir}/fonts/source/public/malayalam/effects/shadow.mf
%{_texmfdistdir}/fonts/source/public/malayalam/fnt_code.mf
%{_texmfdistdir}/fonts/source/public/malayalam/mm.bat
%{_texmfdistdir}/fonts/source/public/malayalam/mm.fts
%{_texmfdistdir}/fonts/source/public/malayalam/mm.job
%{_texmfdistdir}/fonts/source/public/malayalam/mmcillu.mf
%{_texmfdistdir}/fonts/source/public/malayalam/mmcoding.mf
%{_texmfdistdir}/fonts/source/public/malayalam/mmconj.mf
%{_texmfdistdir}/fonts/source/public/malayalam/mmcons.mf
%{_texmfdistdir}/fonts/source/public/malayalam/mmcvconj.mf
%{_texmfdistdir}/fonts/source/public/malayalam/mmdefs.mf
%{_texmfdistdir}/fonts/source/public/malayalam/mmfnt.mf
%{_texmfdistdir}/fonts/source/public/malayalam/mmfont.mf
%{_texmfdistdir}/fonts/source/public/malayalam/mmlnums.mf
%{_texmfdistdir}/fonts/source/public/malayalam/mmnums.mf
%{_texmfdistdir}/fonts/source/public/malayalam/mmpunct.mf
%{_texmfdistdir}/fonts/source/public/malayalam/mmrconj.mf
%{_texmfdistdir}/fonts/source/public/malayalam/mmscons.mf
%{_texmfdistdir}/fonts/source/public/malayalam/mmsec.mf
%{_texmfdistdir}/fonts/source/public/malayalam/mmstyles.txt
%{_texmfdistdir}/fonts/source/public/malayalam/mmtest.mf
%{_texmfdistdir}/fonts/source/public/malayalam/mmvowels.mf
%{_texmfdistdir}/fonts/source/public/malayalam/orn10.mf
%{_texmfdistdir}/fonts/source/public/malayalam/rejected.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mm10.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mm10s.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mm12.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mm12s.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mm17.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mm17s.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mm6.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mm6s.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mm8.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mm8s.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mmb10.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mmb10s.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mmb12.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mmb12s.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mmb17.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mmb17s.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mmbig.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mmbigo.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mmc10.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mmc10s.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mmc12.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mmc12s.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mmc17.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mmc17s.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mmcb10.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mmcb10s.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mmcb12.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mmcb12s.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mmcb17.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mmcb17s.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mmcsl10.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mmcsl10s.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mmcsl12.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mmcsl12s.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mmexpa12.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mmexpb12.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mmexpc12.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mmsl10.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mmsl10s.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mmsl12.mf
%{_texmfdistdir}/fonts/source/public/malayalam/styles/mmsl12s.mf
%{_texmfdistdir}/fonts/source/public/malayalam/var_ja.mf
%{_texmfdistdir}/fonts/tfm/public/malayalam/mm10.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mm10s.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mm12.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mm12s.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mm17.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mm17s.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mm6.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mm6s.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mm8.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mm8s.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mmb10.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mmb10s.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mmb12.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mmb12s.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mmb17.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mmb17s.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mmbig.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mmbigo.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mmc10.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mmc10s.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mmc12.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mmc12s.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mmc17.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mmc17s.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mmcb10.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mmcb10s.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mmcb12.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mmcb12s.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mmcb17.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mmcb17s.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mmcsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mmcsl10s.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mmcsl12.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mmcsl12s.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mmexpa12.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mmexpb12.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mmexpc12.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mmsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mmsl10s.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mmsl12.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/mmsl12s.tfm
%{_texmfdistdir}/fonts/tfm/public/malayalam/orn10.tfm
%doc %{_texmfdistdir}/doc/fonts/malayalam/FILES
%doc %{_texmfdistdir}/doc/fonts/malayalam/INSTALL
%doc %{_texmfdistdir}/doc/fonts/malayalam/README
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/elephant.mm
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/elephant.tex
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/lion.mm
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/lion.tex
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/mmarticl.mm
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/mmarticl.tex
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/mmchart.tex
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/mmconj.mm
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/mmconj.tex
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/mmexp.mm
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/mmexp.tex
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/mmfont.tex
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/mmfuture.tex
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/mmguide.dvi
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/mmguide.mm
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/mmguide.tex
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/mmmacs.tex
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/mmphmacs.tex
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/mmqfont.tex
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/mmqmacs.tex
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/mmsample.mm
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/mmsample.tex
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/mmscript.mm
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/mmtable.mm
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/mmtable.tex
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/mmtrans.mm
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/mmtrans.tex
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/mmtrmacs.tex
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/mmxfont.tex
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/ornament.tex
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/prodigal.mm
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/prodigal.tex
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/test.mm
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/test.tex
%doc %{_texmfdistdir}/doc/fonts/malayalam/article/twolines.tex
%doc %{_texmfdistdir}/doc/fonts/malayalam/charity
%doc %{_texmfdistdir}/doc/fonts/malayalam/todo
#- source
%doc %{_texmfdistdir}/source/fonts/malayalam/dng/dn2dng.pat
%doc %{_texmfdistdir}/source/fonts/malayalam/dng/dng.pat
%doc %{_texmfdistdir}/source/fonts/malayalam/dng/dng.tex
%doc %{_texmfdistdir}/source/fonts/malayalam/dng/dngmacs.tex
%doc %{_texmfdistdir}/source/fonts/malayalam/dng/dngtrans.dng
%doc %{_texmfdistdir}/source/fonts/malayalam/dng/dngtrans.tex
%doc %{_texmfdistdir}/source/fonts/malayalam/dng/dntrmacs.tex
%doc %{_texmfdistdir}/source/fonts/malayalam/dng/misspaal.dng
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/ack2mm.pat
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/avltree.c
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/avltree.h
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/makefile
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/ml.bat
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/ml.g
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/mlr.bat
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/mlr.g
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/mltr.g
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/mltrth.g
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/mm.c
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/mm.exe
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/mm.h
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/mm.pat
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/mm.prj
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/mm.scr
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/mm.trs
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/mm.ttp
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/mm2ack.pat
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/mmr.scr
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/mmr.trs
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/mmrfull.trs
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/patc/detex.g
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/patc/detex.pat
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/patc/patc.c
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/patc/patc.exe
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/patc/patc.prj
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/patc/patc.ttp
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/patc/patc.txt
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/patc/pstree.c
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/patc/pstree.h
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/pstree.c
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/pstree.h
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/readfile.c
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/readfile.h
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/scr.c
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/scr.h
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/trs.c
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/trs.h
%doc %{_texmfdistdir}/source/fonts/malayalam/preproc/unicode/UNICODE.TXT
%doc %{_texmfdistdir}/source/fonts/malayalam/tamil/adami.pat
%doc %{_texmfdistdir}/source/fonts/malayalam/tamil/tamil.pat
%doc %{_texmfdistdir}/source/fonts/malayalam/tamil/tamil.tex
%doc %{_texmfdistdir}/source/fonts/malayalam/tamil/test.tam
%doc %{_texmfdistdir}/source/fonts/malayalam/tamil/test.tex
%doc %{_texmfdistdir}/source/fonts/malayalam/tamil/test.tml
%doc %{_texmfdistdir}/source/fonts/malayalam/tamil/tmlmacs.tex
%doc %{_texmfdistdir}/source/fonts/malayalam/tamil/tmltrans.tex
%doc %{_texmfdistdir}/source/fonts/malayalam/tamil/tmltrans.tml
%doc %{_texmfdistdir}/source/fonts/malayalam/tamil/tmltrans.txt
%doc %{_texmfdistdir}/source/fonts/malayalam/tamil/wntml.pat

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.9.6-2
+ Revision: 753734
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.9.6-1
+ Revision: 718951
- texlive-malayalam
- texlive-malayalam
- texlive-malayalam
- texlive-malayalam

