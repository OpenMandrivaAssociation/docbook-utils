Name: 		docbook-utils
Version: 	0.6.14
Release:	%mkrel 6
Group:		Publishing
Url:		ftp://sources.redhat.com/pub/docbook-tools/new-trials/
Summary:	Shell scripts to manage DocBook documents

License:	GPL

Requires:	docbook-style-dsssl >= 1.72
Requires:	jadetex >= 2.5
Requires:	tetex-latex
Requires:	perl-SGMLSpm >= 1.03ii
Requires: 	which
BuildRequires:	docbook-style-dsssl >= 1.72
BuildRequires:	docbook-dtd31-sgml
Obsoletes:	sgml-tools
Provides:	sgml-tools

BuildRoot:	%{_tmppath}/%name-%version-buildroot

Source0:	ftp://sources.redhat.com/pub/docbook-tools/new-trials/SOURCES/%name-%version.tar.bz2
Source1:	db2html

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
Conflicts: %{name} < 0.6.14-3mdk

%description pdf
This package contains a script for converting DocBook documents to
PDF format.


%prep
%setup -q

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
        ln -s jw.1.gz $RPM_BUILD_ROOT/%{_mandir}/man1/db2$util.1
done

# db2html is not just a symlink, as it has to create the output directory
rm -f $RPM_BUILD_ROOT%{_bindir}/db2html
install -c -m 775 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/db2html

# clean install html files
rm -rf $RPM_BUILD_ROOT/%_prefix/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc README COPYING TODO doc/HTML/*.html
%{_bindir}/jw
%{_bindir}/docbook2dvi
%{_bindir}/docbook2html
%{_bindir}/docbook2man
%{_bindir}/docbook2ps
%{_bindir}/docbook2rtf
%{_bindir}/docbook2tex
%{_bindir}/docbook2texi
%{_bindir}/docbook2txt
%{_bindir}/db2dvi
%attr(0755,root,root) %{_bindir}/db2html
%{_bindir}/db2ps
%{_bindir}/db2rtf
%{_bindir}/db2man
%{_bindir}/sgmldiff
%dir %{_datadir}/sgml/docbook/utils-%{version}
%dir %{_datadir}/sgml/docbook/utils-%{version}/backends
%{_datadir}/sgml/docbook/utils-%{version}/backends/dvi
%{_datadir}/sgml/docbook/utils-%{version}/backends/html
%{_datadir}/sgml/docbook/utils-%{version}/backends/man
%{_datadir}/sgml/docbook/utils-%{version}/backends/pdf
%{_datadir}/sgml/docbook/utils-%{version}/backends/ps
%{_datadir}/sgml/docbook/utils-%{version}/backends/rtf
%{_datadir}/sgml/docbook/utils-%{version}/backends/tex
%{_datadir}/sgml/docbook/utils-%{version}/backends/texi
%{_datadir}/sgml/docbook/utils-%{version}/backends/txt
%{_datadir}/sgml/docbook/utils-%{version}/docbook-utils.dsl
%dir %{_datadir}/sgml/docbook/utils-%{version}/frontends
%{_datadir}/sgml/docbook/utils-%{version}/frontends/docbook
%dir %{_datadir}/sgml/docbook/utils-%{version}/helpers
%{_datadir}/sgml/docbook/utils-%{version}/helpers/docbook2man-spec.pl
%{_datadir}/sgml/docbook/utils-%{version}/helpers/docbook2texi-spec.pl
%exclude %{_mandir}/man1/docbook2pdf.*
%{_mandir}/man1/*
%{_mandir}/man7/*


%files pdf
%defattr (-,root,root)
%{_bindir}/docbook2pdf
%{_bindir}/db2pdf
%{_mandir}/man1/docbook2pdf*


