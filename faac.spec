Name:           faac
Version:        1.29.9.2
Release:        2%{?dist}
Summary:        Encoder and encoding library for MPEG2/4 AAC

Group:          Applications/Multimedia
License:        LGPLv2+
URL:            http://www.audiocoding.com/
Source0:        http://downloads.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  libtool


%description
FAAC is an AAC audio encoder. It currently supports MPEG-4 LTP, MAIN and LOW
COMPLEXITY object types and MAIN and LOW MPEG-2 object types. It also supports
multichannel and gapless encoding.

%package devel
Summary:        Development libraries of the FAAC AAC encoder
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
FAAC is an AAC audio encoder. It currently supports MPEG-4 LTP, MAIN and LOW
COMPLEXITY object types and MAIN and LOW MPEG-2 object types. It also supports
multichannel and gapless encoding.

This package contains development files and documentation for libfaac.

%prep
%setup -q
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
find $RPM_BUILD_ROOT -name '*.la' -or -name '*.a' | xargs rm -f


%ldconfig_scriptlets


%files 
%doc AUTHORS ChangeLog NEWS README TODO docs/*
%license COPYING
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man1/%{name}*

%files devel
%{_libdir}/*.so
%{_includedir}/*.h

%changelog
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

