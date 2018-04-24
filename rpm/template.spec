Name:           ros-lunar-plotjuggler
Version:        1.5.2
Release:        0%{?dist}
Summary:        ROS plotjuggler package

Group:          Development/Libraries
License:        LGPLv3
URL:            https://github.com/facontidavide/PlotJuggler
Source0:        %{name}-%{version}.tar.gz

Requires:       binutils-devel
Requires:       qt5-qtbase-devel
Requires:       qt5-qtsvg-devel
Requires:       ros-lunar-ros-type-introspection
Requires:       ros-lunar-rosbag
Requires:       ros-lunar-rosbag-storage
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-roscpp-serialization
Requires:       ros-lunar-rostime
Requires:       ros-lunar-topic-tools
BuildRequires:  binutils-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-ros-type-introspection
BuildRequires:  ros-lunar-rosbag
BuildRequires:  ros-lunar-rosbag-storage
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-roscpp-serialization
BuildRequires:  ros-lunar-rostime
BuildRequires:  ros-lunar-topic-tools

%description
PlotJuggler: juggle with data

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Tue Apr 24 2018 Davide Faconti <davide.faconti@gmail.com> - 1.5.2-0
- Autogenerated by Bloom

* Wed Feb 14 2018 Davide Faconti <davide.faconti@gmail.com> - 1.5.1-0
- Autogenerated by Bloom

* Tue Nov 28 2017 Davide Faconti <davide.faconti@gmail.com> - 1.5.0-0
- Autogenerated by Bloom

* Mon Nov 20 2017 Davide Faconti <davide.faconti@gmail.com> - 1.4.2-0
- Autogenerated by Bloom

* Tue Nov 14 2017 Davide Faconti <davide.faconti@gmail.com> - 1.4.0-0
- Autogenerated by Bloom

* Thu Oct 12 2017 Davide Faconti <davide.faconti@gmail.com> - 1.3.0-0
- Autogenerated by Bloom

* Wed Aug 30 2017 Davide Faconti <davide.faconti@gmail.com> - 1.2.1-0
- Autogenerated by Bloom

* Tue Aug 29 2017 Davide Faconti <davide.faconti@gmail.com> - 1.2.0-0
- Autogenerated by Bloom

* Tue Jul 11 2017 Davide Faconti <davide.faconti@gmail.com> - 1.1.3-0
- Autogenerated by Bloom

* Mon Jun 26 2017 Davide Faconti <davide.faconti@gmail.com> - 1.1.1-0
- Autogenerated by Bloom

* Tue Jun 20 2017 Davide Faconti <davide.faconti@gmail.com> - 1.1.0-0
- Autogenerated by Bloom

