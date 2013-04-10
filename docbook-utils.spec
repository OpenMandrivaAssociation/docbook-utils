Summary:	Shell scripts to manage DocBook documents
Name: 		docbook-utils
Version: 	0.6.14
Release:	15
Group:		Publishing
License:	GPLv2+
Url:		ftp://sources.redhat.com/pub/docbook-tools/new-trials/
Source0:	ftp://sources.redhat.com/pub/docbook-tools/new-trials/SOURCES/%name-%version.tar.bz2
Source1:	db2html
Source2:	docbook2man-spec.pl
Patch0:		docbook-utils-spaces.patch
Patch1:		docbook-utils-2ndspaces.patch
Patch2:		docbook-utils-w3mtxtconvert.patch
Patch3:		docbook-utils-grepnocolors.patch
Patch4:		docbook-utils-sgmlinclude.patch
Patch5:		docbook-utils-rtfmanpage.patch
Patch6:		docbook-utils-papersize.patch
Patch7:		docbook-utils-nofinalecho.patch
Patch8:		docbook-utils-newgrep.patch
BuildArch:	noarch

BuildRequires:	docbook-style-dsssl >= 1.72
BuildRequires:	docbook-dtd31-sgml
Requires:	docbook-style-dsssl >= 1.72
Requires:	perl-SGMLSpm >= 1.03ii
Requires:	gawk
Requires:	grep
Provides:	sgml-tools
Requires: 	which

%Description
This package contains scripts are for easy conversion from DocBook
files to other formats (for example, HTML, RTF, and PostScript), and
for comparing SGML files.

%package pdf
Requires:	tetex-dvips
Requires:	jadetex >= 2.5
Requires:	docbook-utils = %{version}
Group:		Publishing
Provides:	stylesheets-db2pdf
Summary:	A script for converting DocBook documents to PDF format
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
mkdir -p %{buildroot}/%_mandir/man{1,7}
for sec in 1 7; do cp -af doc/man/*.$sec %{buildroot}/%_mandir/man$sec; done

%makeinstall_std

for util in dvi html pdf ps rtf man
do
        ln -s docbook2$util %{buildroot}%{_bindir}/db2$util
        ln -s jw.1 %{buildroot}/%{_mandir}/man1/db2$util.1
done
ln -s jw.1 %{buildroot}/%{_mandir}/man1/docbook2txt.1

# db2html is not just a symlink, as it has to create the output directory
rm -f %{buildroot}%{_bindir}/db2html
install -c -m 775 %{SOURCE1} %{buildroot}%{_bindir}/db2html
install -p -m 755 %{SOURCE2} %{buildroot}%{_datadir}/sgml/docbook/utils-%{version}/helpers/docbook2man-spec.pl

# clean install html files
rm -rf %{buildroot}/%_prefix/doc

%files
%doc README COPYING TODO doc/HTML/*.html
%{_bindir}/jw
%{_bindir}/docbook2html
%{_bindir}/docbook2man
%{_bindir}/docbook2rtf
%{_bindir}/docbook2tex
%{_bindir}/docbook2texi
%{_bindir}/docbook2txt
%{_bindir}/db2html
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

