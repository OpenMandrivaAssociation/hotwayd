%define name hotwayd
%define version 0.8.4
%define release %mkrel 1

Summary: POP3 to HTTPMail gateway daemon to access Hotmail / Lycos mailboxes
Name: %{name}
Version: %{version}
Release: %{release}
License: GPLv2+
Group: System/Servers
URL: http://hotwayd.sourceforge.net/
Source: %{name}-%{version}.tar.bz2
Source1: hotwayd.xinetd.bz2
Source2: hotsmtpd.xinetd.bz2
BuildRequires: libxml2-devel libsasl-devel

%description
Hotway is a POP3-HTTPMail gateway daemon. HTTPMail is an undocumented 
WebDAV-based protocol used by hotmail. This gateway allows *any* POP3 
compatible email client to handle (download, delete, etc) messages on 
hotmail.com, msn.com and lycos.co.uk mailboxes.

%package -n hotsmtpd
Summary: ESMTP to HTTPMail gateway daemon to access Hotmail / Lycos mailboxes
Group: System/Servers

%description -n hotsmtpd
This package contains hotsmtpd, a ESMTP to HTTPMail proxy. It works
like Hotwayd. It allows any SMTP client to post through a hotmail account.

%prep
%setup -q

%build
%configure
%make  

%install
rm -rf %{buildroot} 
%makeinstall
mkdir -p %{buildroot}/%{_sysconfdir}/xinetd.d
bzcat %{SOURCE1} > %{buildroot}/%{_sysconfdir}/xinetd.d/%{name}
bzcat %{SOURCE2} > %{buildroot}/%{_sysconfdir}/xinetd.d/hotsmtpd
chmod a+x %{buildroot}/%{_sbindir}/%{name}

%clean
rm -rf %{buildroot}

%post
service xinetd condrestart

%postun
service xinetd condrestart

%files
%defattr(0644,root,root,755)
%doc README NEWS AUTHORS ChangeLog
%config(noreplace) %{_sysconfdir}/xinetd.d/%{name}
%{_mandir}/man1/%{name}.1*
%defattr(0755,root,root,755)
%{_sbindir}/%{name}

%files -n hotsmtpd
%defattr(0644,root,root,755)
%doc README.hotsmtpd
%config(noreplace) %{_sysconfdir}/xinetd.d/hotsmtpd
%{_mandir}/man1/hotsmtpd.1*
%defattr(0755,root,root,755)
%{_sbindir}/hotsmtpd

