Summary:	Nagg - HDF NPP Aggregation tool
Summary(pl.UTF-8):	Nagg - narzędzie do agregacji HDF NPP
Name:		nagg
Version:	1.4.0
Release:	2
Group:		Applications/File
License:	BSD-like, changed sources must be marked
Source0:	http://www.hdfgroup.uiuc.edu/ftp/pub/outgoing/NPOESS/source/NAGG/v140/%{name}-%{version}.tar.gz
# Source0-md5:	eeb96e6c2087639d90ebfe1796f49709
URL:		http://www.hdfgroup.org/projects/npoess/nagg_index.html
BuildRequires:	hdf5-devel
BuildRequires:	hdf5_hl_region-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nagg is a tool for aggregating JPSS data granules from existing files
into new files with a different number of granules per file or
different combinations of compatible products than in the original
files. The tool was created to provide individual users the ability to
rearrange NPP product data granules from downloaded files into new
files with aggregations or packaging that are better suited as input
for a particular application.

%description -l pl.UTF-8
Nagg to narzędzie do agregacji porcji danych JPSS z istniejących
plików do nowych plików o innej liczbie porcji w pliku lub innej
kombinacji zgodnych wyników niż w plikach oryginalnych. Narzędzie
powstało w celu umożliwienia użytkownikom zmiany rozłożenia porcji
wyników NPP z pobranych plików do nowych plików z agregatami lub
pakowania bardziej dopasowanego do wejścia danej aplikacji.

%prep
%setup -q

%build
%configure

%{__make} \
	nagg_LDADD="-lm"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING doc/{History,RELEASE.txt,*.pdf}
%attr(755,root,root) %{_bindir}/nagg
