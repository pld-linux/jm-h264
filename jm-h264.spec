#
# Conditional build:
%bcond_without	gomp	# OpenMP support
#
Summary:	H.264/AVC reference software
Summary(pl.UTF-8):	Referencyjna implementacja H.264/AVC
Name:		jm-h264
Version:	18.4
Release:	0.1
License:	free (but may require patent license)
Group:		Libraries
Source0:	http://iphome.hhi.de/suehring/tml/download/jm%{version}.zip
# Source0-md5:	da79fd3c66c9b98537dc2de65487b31c
URL:		http://iphome.hhi.de/suehring/tml/
%if %{with gomp}
BuildRequires:	gcc-c++ >= 6:4.2
BuildRequires:	libgomp-devel
%endif
BuildRequires:	libstdc++-devel
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
H.264/AVC reference software.

%description -l pl.UTF-8
Referencyjna implementacja H.264/AVC.

%prep
%setup -q -n JM

%build
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	OPT_FLAG="%{rpmcflags}" \
	%{?with_gomp:OPENMP=1}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install bin/ldecod.exe $RPM_BUILD_ROOT%{_bindir}/jm-ldecod
install bin/lencod.exe $RPM_BUILD_ROOT%{_bindir}/jm-lencod
install bin/rtp_loss.exe $RPM_BUILD_ROOT%{_bindir}/jm-rtp_loss
install bin/rtpdump.exe $RPM_BUILD_ROOT%{_bindir}/jm-rtpdump

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.TXT COPYRIGHT_ISO_IEC.txt COPYRIGHT_ITU.txt Changes_detail.txt FREXT_changes.txt Readme.txt disclaimer.txt
%attr(755,root,root) %{_bindir}/jm-ldecod
%attr(755,root,root) %{_bindir}/jm-lencod
%attr(755,root,root) %{_bindir}/jm-rtp_loss
%attr(755,root,root) %{_bindir}/jm-rtpdump
