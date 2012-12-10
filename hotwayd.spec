%define name hotwayd
%define version 0.8.4
%define release 3

Summary: POP3 to HTTPMail gateway daemon to access Hotmail / Lycos mailboxes
Name: %{name}
Version: %{version}
Release: %{release}
License: GPLv2+
Group: System/Servers
URL: http://hotwayd.sourceforge.net/
Source0: %{name}-%{version}.tar.bz2
Source1: hotwayd.xinetd.bz2
Source2: hotsmtpd.xinetd.bz2
patch0:  hotwayd-0.8.4.printf.patch
BuildRequires: pkgconfig(libxml-2.0) libsasl-devel

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
%patch0 -p1 -b .printf

%build
%configure
%make  

%install
%makeinstall
mkdir -p %{buildroot}/%{_sysconfdir}/xinetd.d
bzcat %{SOURCE1} > %{buildroot}/%{_sysconfdir}/xinetd.d/%{name}
bzcat %{SOURCE2} > %{buildroot}/%{_sysconfdir}/xinetd.d/hotsmtpd
chmod a+x %{buildroot}/%{_sbindir}/%{name}

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



%changelog
* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.8.4-3mdv2009.0
+ Revision: 246898
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Nov 23 2007 Adam Williamson <awilliamson@mandriva.com> 0.8.4-1mdv2008.1
+ Revision: 111718
- misc spec clean
- new license policy
- new release 0.8.4
- import hotwayd


* Sat Apr 23 2005 Michael Scherer <misc@mandriva.org> 0.8-2mdk
- Rebuild


* Mon Feb 09 2004 Michael Scherer <misc@mandrake.org> 0.8-1mdk
- 0.8
- split package
 
* Sat Jan 17 2004 Michael Scherer <misc@mandrake.org> 0.7.4-1mdk
- 0.7.4

* Sun Jan 11 2004 Michael Scherer <misc@mandrake.org> 0.7.2-1mdk
- 0.7.2
 
* Fri Nov 14 2003 Michael Scherer <scherer.michael@free.fr> 0.7.1-2mdk 
- changed the Summary, thanks to David Smith  <courierdave@users.sourceforge.net>

* Tue Nov 11 2003 Michael Scherer <scherer.michael@free.fr> 0.7.1-1mdk
- mandrakification on the specs, based on 
   works of David Smith <courierdave@users.sourceforge.net>

