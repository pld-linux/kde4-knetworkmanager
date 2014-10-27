#
# Conditional build:
%bcond_with	verbose		# verbose build

%define		qtver	4.6.4
%define		origname	networkmanagement

Summary:	Plasma applet that controls network via NetworkManager backend
Name:		kde4-knetworkmanager
Version:	0.9.0.11
Release:	2
Epoch:		1
License:	GPL v2
Group:		X11/Applications
# git clone git://anongit.kde.org/networkmanagement.git
# git checkout nm09 (until is merged to master)
Source0:	ftp://ftp.kde.org/pub/kde/unstable/networkmanagement/%{version}/src/%{origname}-%{version}.tar.xz
# Source0-md5:	f1b5d6ae1cfd869ca2c377f3d4647cbf
Patch0:	%{origname}-kill_rest_sr.patch
Patch1:	%{name}-solid.patch
URL:		http://en.opensuse.org/Projects/KNetworkManager
BuildRequires:	NetworkManager-devel >= 2:0.9.8
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
BuildRequires:	mobile-broadband-provider-info-devel
BuildRequires:	openconnect-devel >= 3.12
BuildRequires:	openssl-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.293
Requires:	NetworkManager >= 2:0.9.0
Obsoletes:	kde4-kdeplasma-addons-networkmanager
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plasma applet that controls network via NetworkManager backend.

%prep
%setup -q -n %{origname}-%{version}
%patch0 -p1
%patch1 -p1

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

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc DESIGN TODO
#%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/*.conf

%attr(755,root,root) %{_libdir}/kde4/kcm_networkmanagement.so
%attr(755,root,root) %{_libdir}/kde4/kcm_networkmanagement_tray.so
%attr(755,root,root) %{_libdir}/kde4/kded_networkmanagement.so
%attr(755,root,root) %{_libdir}/kde4/libexec/networkmanagement_configshell
%attr(755,root,root) %{_libdir}/kde4/networkmanagement_novellvpnui.so
%attr(755,root,root) %{_libdir}/kde4/networkmanagement_openconnectui.so
%attr(755,root,root) %{_libdir}/kde4/networkmanagement_openvpnui.so
%attr(755,root,root) %{_libdir}/kde4/networkmanagement_pptpui.so
%attr(755,root,root) %{_libdir}/kde4/networkmanagement_strongswanui.so
%attr(755,root,root) %{_libdir}/kde4/networkmanagement_vpncui.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_networkmanagement.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_networkmanagement.so
%attr(755,root,root) %{_libdir}/kde4/solid_modemmanager05.so
%attr(755,root,root) %{_libdir}/kde4/solid_networkmanager09.so
%attr(755,root,root) %{_libdir}/libknmclient.so
%attr(755,root,root) %{_libdir}/libknmclient.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libknmclient.so.?
%attr(755,root,root) %{_libdir}/libknminternals.so
%attr(755,root,root) %{_libdir}/libknminternals.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libknminternals.so.?
%attr(755,root,root) %{_libdir}/libknm_nm.so
%attr(755,root,root) %{_libdir}/libknmservice.so
%attr(755,root,root) %{_libdir}/libknmservice.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libknmservice.so.?
%attr(755,root,root) %{_libdir}/libknmui.so
%attr(755,root,root) %{_libdir}/libknmui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libknmui.so.?
%attr(755,root,root) %{_libdir}/libsolidcontrolfuture.so
%attr(755,root,root) %{_libdir}/libsolidcontrolnm09ifaces.so
%attr(755,root,root) %{_libdir}/libsolidcontrolnm09ifaces.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsolidcontrolnm09ifaces.so.?
%attr(755,root,root) %{_libdir}/libsolidcontrolnm09.so
%attr(755,root,root) %{_libdir}/libsolidcontrolnm09.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsolidcontrolnm09.so.?

%{_datadir}/apps/desktoptheme/default/icons/network2.svgz
%{_datadir}/apps/networkmanagement
%{_datadir}/kde4/services/*.desktop
%{_datadir}/kde4/services/kded/*.desktop
%{_datadir}/kde4/servicetypes/*.desktop
%{_iconsdir}/oxygen/*x*/apps/networkmanager.png
%{_iconsdir}/oxygen/*x*/devices/network-wireless*.png
%{_iconsdir}/oxygen/*x*/devices/network-wired-activated.png
%{_iconsdir}/oxygen/*x*/devices/network-defaultroute.png
