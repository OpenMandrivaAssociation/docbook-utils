Name: 		docbook-utils
Version: 	0.6.14
Release:	%mkrel 15
Group:		Publishing
Url:		ftp://sources.redhat.com/pub/docbook-tools/new-trials/
Summary:	Shell scripts to manage DocBook documents

License:	GPLv2+

Requires:	docbook-style-dsssl >= 1.72
Requires:	perl-SGMLSpm >= 1.03ii
Requires: 	which grep gawk
BuildRequires:	docbook-style-dsssl >= 1.72
BuildRequires:	docbook-dtd31-sgml
Obsoletes:	sgml-tools
Provides:	sgml-tools

BuildRoot:	%{_tmppath}/%name-%version-buildroot

Source0:	ftp://sources.redhat.com/pub/docbook-tools/new-trials/SOURCES/%name-%version.tar.bz2
Source1:	db2html
Source2:	docbook2man-spec.pl
Patch0: docbook-utils-spaces.patch
Patch1: docbook-utils-2ndspaces.patch
Patch2: docbook-utils-w3mtxtconvert.patch
Patch3: docbook-utils-grepnocolors.patch
Patch4: docbook-utils-sgmlinclude.patch
Patch5: docbook-utils-rtfmanpage.patch
Patch6: docbook-utils-papersize.patch
Patch7: docbook-utils-nofinalecho.patch
Patch8: docbook-utils-newgrep.patch
BuildArch:	noarch

%Description
This package contains scripts are for easy conversion from DocBook
files to other formats (for example, HTML, RTF, and PostScript), and
for comparing SGML files.

%package pdf
Requires: tetex-dvips jadetex >= 2.5
Requires: docbook-utils = %{version}
Group: Publishing
Obsoletes: stylesheets-db2pdf
Provides: stylesheets-db2pdf
Summary: A script for converting DocBook documents to PDF format
URL: ftp://sources.redhat.com/pub/docbook-tools/new-trials/
Conflicts: %{name} < 0.6.14-13

%description pdf
This package contains a script for converting DocBook documents to
PDF format.


%prep
%setup -q
%apply_patches

%build

%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_mandir/man{1,7}
for sec in 1 7; do cp -af doc/man/*.$sec $RPM_BUILD_ROOT/%_mandir/man$sec; done

%makeinstall_std

for util in dvi html pdf ps rtf man
do
        ln -s docbook2$util $RPM_BUILD_ROOT%{_bindir}/db2$util
        ln -s jw.1 $RPM_BUILD_ROOT/%{_mandir}/man1/db2$util.1
done
ln -s jw.1 $RPM_BUILD_ROOT/%{_mandir}/man1/docbook2txt.1

# db2html is not just a symlink, as it has to create the output directory
rm -f $RPM_BUILD_ROOT%{_bindir}/db2html
install -c -m 775 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/db2html
install -p -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/utils-%{version}/helpers/docbook2man-spec.pl

# clean install html files
rm -rf $RPM_BUILD_ROOT/%_prefix/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc README COPYING TODO doc/HTML/*.html
%{_bindir}/jw
%{_bindir}/docbook2html
%{_bindir}/docbook2man
%{_bindir}/docbook2rtf
%{_bindir}/docbook2tex
%{_bindir}/docbook2texi
%{_bindir}/docbook2txt
%attr(0755,root,root) %{_bindir}/db2html
%{_bindir}/db2rtf
%{_bindir}/db2man
%{_bindir}/sgmldiff
%{_datadir}/sgml/docbook/utils-%{version}
%{_mandir}/*/db2dvi.*
%{_mandir}/*/db2html.*
%{_mandir}/*/db2man.*
%{_mandir}/*/db2ps.*
%{_mandir}/*/db2rtf.*
%{_mandir}/*/docbook2html.*
%{_mandir}/*/docbook2rtf.*
%{_mandir}/*/docbook2man.*
%{_mandir}/*/docbook2tex.*
%{_mandir}/*/docbook2texi.*
%{_mandir}/*/docbook2txt.*
%{_mandir}/*/jw.*
%{_mandir}/*/sgmldiff.*
%{_mandir}/*/*-spec.*

%files pdf
%defattr (-,root,root)
%{_bindir}/docbook2pdf
%{_bindir}/docbook2dvi
%{_bindir}/docbook2ps
%{_bindir}/db2dvi
%{_bindir}/db2pdf
%{_bindir}/db2ps
%{_mandir}/*/db2pdf.*
%{_mandir}/*/docbook2pdf.*
%{_mandir}/*/docbook2dvi.*
%{_mandir}/*/docbook2ps.*


%changelog
* Wed Apr 06 2011 Funda Wang <fwang@mandriva.org> 0.6.14-13mdv2011.0
+ Revision: 650855
- sync with fedora rpm, so that docbook-utils won't pull out all the tex pacakges

* Tue Sep 28 2010 Götz Waschk <waschk@mandriva.org> 0.6.14-12mdv2011.0
+ Revision: 581614
- fix for new grep (bug #61127)

* Wed Jan 13 2010 Jérôme Brenier <incubusss@mandriva.org> 0.6.14-11mdv2010.1
+ Revision: 491012
- replace the docbook2man-spec.pl file by a corrected one from Fedora
- fix license tag

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.6.14-10mdv2010.0
+ Revision: 413373
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.6.14-9mdv2009.1
+ Revision: 350833
- rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.6.14-8mdv2009.0
+ Revision: 220679
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 0.6.14-7mdv2008.1
+ Revision: 149207
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.6.14-6mdv2008.0
+ Revision: 83600
- rebuild


* Wed Feb 28 2007 Emmanuel Andry <eandry@mandriva.org> 0.6.14-5mdv2007.0
+ Revision: 130195
- create db2man symlink
- %%mkrel
- Import docbook-utils

* Tue May 23 2006 Camille Begnis <camille@mandriva.com> 0.6.14-4mdk
- rebuild

* Fri Apr 29 2005 Frederic Crozat <fcrozat@mandriva.com> 0.6.14-3mdk 
- Move docbook2pdf manpage to subpackage

* Fri Apr 22 2005 Camille Begnis <camille@mandriva.com> 0.6.14-2mdk
- rebuild

