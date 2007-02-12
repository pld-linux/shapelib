Summary:	Shapefile C Library
Summary(pl.UTF-8):   Biblioteka Shapefile dla C
Name:		shapelib
Version:	1.2.10
Release:	1
License:	MIT or LGPL
Group:		Libraries
Source0:	ftp://ftp.remotesensing.org/pub/shapelib/%{name}-%{version}.tar.gz
# Source0-md5:	4d96bd926167193d27bf14d56e2d484e
Patch0:		%{name}-make.patch
URL:		http://www.remotesensing.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Shapefile C Library provides the ability to write simple C
programs for reading, writing and updating (to a limited extent) ESRI
Shapefiles, and the associated attribute file (.dbf).

%description -l pl.UTF-8
Biblioteka C Shapefile daje możliwość pisania prostych programów w C
do odczytu, zapisu i uaktualniania (w pewnym zakresie) plików ESRI
oraz związanych z nimi plików atrybutów (.dbf).

%package devel
Summary:	Header files for shapelib library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki shapelib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for shapelib library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki shapelib.

%package static
Summary:	Static shapelib library
Summary(pl.UTF-8):   Statyczna biblioteka shapelib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static shapelib library.

%description static -l pl.UTF-8
Statyczna biblioteka shapelib.

%prep
%setup -q
%patch0 -p1

%build
%{__make} lib all \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	libdir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} lib_install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir} \
	includedir=%{_includedir}

install -d $RPM_BUILD_ROOT%{_bindir}
for p in dbfadd dbfcreate dbfdump shpadd shpcreate shpdump shprewind shptest ; do
	sh ./libtool --mode=install install $p $RPM_BUILD_ROOT%{_bindir}
done

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README* *.html
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libshp.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libshp.so
%{_libdir}/libshp.la
%{_includedir}/libshp

%files static
%defattr(644,root,root,755)
%{_libdir}/libshp.a
