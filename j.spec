Summary:	j editor
Summary(pl):	Edytof j
Name:		j
Version:	0.18.0
Release:	1
Group:		Development/Tools
License:	GPL
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/armedbear-j/%{name}-%{version}.tar.gz
URL:		http://armedbear-j.sourceforge.net/
Patch0:		%{name}-destdir.patch
BuildRequires:	jdk
Requires:	jre
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
J is a text editor written entirely in Java.

%description -l pl
J to edytor tekstu napisany ca³kowicie w Javie.

%prep
%setup -q
%patch0 -p1

%build
chmod 755 configure
chmod 755 mkinstalldirs
%configure2_13 				\
        --with-jdk=/usr/lib/java	\
	--enable-jpty
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr (755,root,root) %{_bindir}/*
%doc doc/*
%dir %{_datadir}/j
%{_datadir}/j/themes
%{_datadir}/j/j.jar
