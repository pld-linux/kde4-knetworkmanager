#
# Conditional build:
%bcond_with	verbose		# verbose build

%define		snap	1102779
%define		qtver	4.6.2
%define		origname	networkmanagement

Summary:	Plasma applet that controls network via NetworkManager backend
Name:		kde4-knetworkmanager
Version:	4.4.1
Release:	0.%{snap}.1
License:	GPL v2
Group:		X11/Applications
# svn co svn://anonsvn.kde.org/home/kde/trunk/kdereview/networkmanagement
Source0:	%{origname}-%{snap}.tar.gz
# Source0-md5:	d7a4cdc57cd107713c44a99896615264
URL:		http://en.opensuse.org/Projects/KNetworkManager
BuildRequires:	NetworkManager-devel >= 0.7.1
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtXml-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdebase-workspace-devel >= %{version}
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.293
Obsoletes:	kde4-kdeplasma-addons-networkmanager
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plasma applet that controls network via NetworkManager backend.

%prep
%setup -q -n %{origname}-%{snap}

%build
install -d build
cd build
%cmake \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	%{?with_verbose:-DCMAKE_VERBOSE_MAKEFILE=true} \
	-DDBUS_SYSTEM_POLICY_DIR=/etc/dbus-1/system.d \
%if "%{_lib}" != "lib"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc DESIGN TODO
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/*.conf
%attr(755,root,root) %{_bindir}/knetworkmanager
%attr(755,root,root) %ghost %{_libdir}/libknmclient.so.?
%attr(755,root,root) %{_libdir}/libknmclient.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libknminternals.so.?
%attr(755,root,root) %{_libdir}/libknminternals.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libknmservice.so.?
%attr(755,root,root) %{_libdir}/libknmservice.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libknmui.so.?
%attr(755,root,root) %{_libdir}/libknmui.so.*.*.*
%attr(755,root,root) %{_libdir}/libknm_nm.so
%attr(755,root,root) %{_libdir}/libsolidcontrolfuture.so
%attr(755,root,root) %{_libdir}/kde4/kcm_networkmanagement.so
%attr(755,root,root) %{_libdir}/kde4/networkmanagement_openvpnui.so
%attr(755,root,root) %{_libdir}/kde4/networkmanagement_vpncui.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_networkmanagement.so
%attr(755,root,root) %{_libdir}/kde4/libexec/networkmanagement_configshell
%attr(755,root,root) %{_libdir}/kde4/kcm_networkmanagement_tray.so
%attr(755,root,root) %{_libdir}/kde4/kded_networkmanagement.so
%attr(755,root,root) %{_libdir}/kde4/networkmanagement_novellvpnui.so
%attr(755,root,root) %{_libdir}/kde4/networkmanagement_pptpui.so
%{_datadir}/apps/networkmanagement
%{_datadir}/kde4/services/*.desktop
%{_datadir}/kde4/services/kded/*.desktop
%{_datadir}/kde4/servicetypes/*.desktop
%{_desktopdir}/kde4/knetworkmanager.desktop
%{_datadir}/autostart/kde4-knetworkmanager-autostart.desktop
%{_iconsdir}/oxygen/*x*/devices/network-wireless*.png
%{_iconsdir}/oxygen/*x*/devices/network-wired-activated.png
%{_iconsdir}/hicolor/32x32/apps/knetworkmanager.png
