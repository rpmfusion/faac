Name:           faac
Version:        1.25
Release:        7%{?dist}
Summary:        Encoder and encoding library for MPEG2/4 AAC

Group:          Applications/Multimedia
License:        LGPL2+
URL:            http://www.audiocoding.com/
Source0:        http://download.sourceforge.net/sourceforge/faac/faac-1.25.tar.gz
Patch0:         faac-1.25-enable-libmp4v2.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libmp4v2-devel
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dos2unix


%description
FAAC is an AAC audio encoder. It currently supports MPEG-4 LTP, MAIN and LOW
COMPLEXITY object types and MAIN and LOW MPEG-2 object types. It also supports
multichannel and gapless encoding.

%package devel
Summary:        Development libraries of the FAAC AAC encoder
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
FAAC is an AAC audio encoder. It currently supports MPEG-4 LTP, MAIN and LOW
COMPLEXITY object types and MAIN and LOW MPEG-2 object types. It also supports
multichannel and gapless encoding.

This package contains development files and documentation for libfaac.

%prep
%setup -q -n %{name}
find . -type f -print|xargs dos2unix 
%patch0 -p1 -b .patch0
chmod 0644 COPYING ChangeLog README TODO

%build
sh ./bootstrap
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files 
%defattr(-,root,root,-)
%doc COPYING ChangeLog README TODO
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%exclude  %{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/*.h

%changelog
* Tue Nov 04 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 1.25-7
- chmod 644 all docs (fixes #115)

* Thu Jul 24 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 1.25-6
- rebuild

* Tue Jul 22 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 1.25-5
- rebuild for RPM Fusion

* Sat Sep 17 2007 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 1.25-4
- update license tag

* Sat Sep 17 2007 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 1.25-3
- incorporate some minor adjustments from the freshrpms pacakge

* Sun Dec 17 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> 1.25-2
- BR dos2unix

* Sun Dec 17 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> 1.25-1
- Update to 1.25
- appy patch from to enable build against libmp4v2 from #1317
  (thx to noa)

* Sat Sep 30 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> 1.24-6
- rebuild for new libmp4v2-devel

* Sun May 28 2006 Noa Resare <noa@resare.com> 1.24-5
- libmp4v2 is now a separate package, updated BR
- shortened summary string

* Mon Mar 13 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> 1.24-4
- Drop Epoch completely

* Thu Mar 09 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- switch to new release field

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Mon Oct 25 2004 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 0:1.24-0.lvn.3
- BR automake autoconf (how could I have been that stupid and missed those? 
  don't answer please)

* Mon Oct 25 2004 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 0:1.24-0.lvn.2
- BR libtool

* Fri Oct 22 2004 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 0:1.24-0.lvn.1
- Initial RPM release. 
