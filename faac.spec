Name:           faac
Version:        1.31.1
Release:        1%{?dist}
Summary:        Encoder and encoding library for MPEG2/4 AAC

License:        LGPLv2+
URL:            http://www.audiocoding.com/
Source0:        https://github.com/knik0/faac/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  automake
BuildRequires:  libtool


%description
FAAC is an AAC audio encoder. It currently supports MPEG-4 LTP, MAIN and LOW
COMPLEXITY object types and MAIN and LOW MPEG-2 object types. It also supports
multichannel and gapless encoding.

%package devel
Summary:        Development libraries of the FAAC AAC encoder
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
FAAC is an AAC audio encoder. It currently supports MPEG-4 LTP, MAIN and LOW
COMPLEXITY object types and MAIN and LOW MPEG-2 object types. It also supports
multichannel and gapless encoding.

This package contains development files and documentation for libfaac.

%prep
%autosetup -p1 -n %{name}-%{name}-%{version}
./bootstrap
#fix encoding
/usr/bin/iconv -f iso8859-1 -t utf-8 AUTHORS > AUTHORS.conv && touch -r AUTHORS AUTHORS.conv && /bin/mv -f AUTHORS.conv AUTHORS


%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build


%install
%make_install

#Remove libtool archives.
find %buildroot -name '*.la' -or -name '*.a' | xargs rm -f


%ldconfig_scriptlets


%files
%doc AUTHORS ChangeLog NEWS README TODO docs/*
%license COPYING
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man1/%{name}*

%files devel
%{_libdir}/pkgconfig/faac.pc
%{_libdir}/*.so
%{_includedir}/*.h

%changelog
* Wed Mar 05 2025 Leigh Scott <leigh123linux@gmail.com> - 1.31.1-1
- Update to 1.31.1

* Wed Jan 29 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.30-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.30-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.30-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 03 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.30-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.30-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.30-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.30-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.30-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 01 2020 Leigh Scott <leigh123linux@gmail.com> - 1.30-2
- bootstrap after applying patch

* Wed Jan 01 2020 Leigh Scott <leigh123linux@gmail.com> - 1.30-1
- Update to 1.30

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.29.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.29.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Nicolas Chauvet <kwizart@gmail.com> - 1.29.9.2-5
- Drop libtool deps

* Mon Oct 08 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.29.9.2-4
- Enable DRM support (rfbz#5043)
- Spec file clean up

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.29.9.2-3
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 1.29.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 15 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.29.9.2-1
- Update to 1.29.9.2
- Fix rpath
- Update scriptlets

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.29.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.29.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 28 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.29.3-1
- Update to 1.29.3

* Sat Dec  6 2014 Nicolas Chauvet <kwizart@gmail.com> - 1.28-7
- Fix build with libmp4v2-devel - rfbz#3188
- Clean-up spec file

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Mar 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.28-5
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 25 2009 kwizart < kwizart at gmail.com > - 1.28-2
- Install with -p
- Moved in nonfree

