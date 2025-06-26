Summary:	Shapefile C Library
Summary(pl.UTF-8):	Biblioteka Shapefile dla C
Name:		shapelib
Version:	1.6.1
Release:	1
License:	MIT or LGPL v2+
Group:		Libraries
Source0:	http://download.osgeo.org/shapelib/%{name}-%{version}.tar.gz
# Source0-md5:	39065725a4b9211e29c9e8b0dfef6deb
URL:		http://shapelib.maptools.org/
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake >= 1:1.11
BuildRequires:	libtool >= 2:2
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
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki shapelib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for shapelib library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki shapelib.

%package static
Summary:	Static shapelib library
Summary(pl.UTF-8):	Statyczna biblioteka shapelib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static shapelib library.

%description static -l pl.UTF-8
Statyczna biblioteka shapelib.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libshp.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README* web/*.html
%attr(755,root,root) %{_bindir}/Shape_PointInPoly
%attr(755,root,root) %{_bindir}/csv2shp
%attr(755,root,root) %{_bindir}/dbf*
%attr(755,root,root) %{_bindir}/shp*
%attr(755,root,root) %{_libdir}/libshp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libshp.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libshp.so
%{_includedir}/shapefil.h
%{_pkgconfigdir}/shapelib.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libshp.a
