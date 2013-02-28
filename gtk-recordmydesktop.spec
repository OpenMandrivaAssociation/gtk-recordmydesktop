%define oname recordMyDesktop
%define	gtkoname gtk-%{oname}

Summary:	GTK fronted for recordmydesktop
Name:		gtk-recordmydesktop
Version:	0.3.8
Release:	4
License:	GPLv2+
Group:		Video
URL:		http://recordmydesktop.sourceforge.net
Source0:	http://downloads.sourceforge.net/recordmydesktop/%{name}-%{version}.tar.bz2
Source1:	gtk-recordmydesktop.rpmlintrc
BuildRequires:	pygtk2.0-devel
BuildRequires:	desktop-file-utils
Requires:	recordmydesktop >= %{version}


%description
Frontend for recordmydesktop tool.

%prep
%setup -q

%build

%configure2_5x

%make

%install
%makeinstall_std

#(tpg) handle icon extension
sed -i -e 's/^Icon=%{name}.png$/Icon=%{name}/g' %{buildroot}%{_datadir}/applications/*

desktop-file-install \
	--add-category="Video;GTK" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{gtkoname}

%files -f %{gtkoname}.lang
%doc AUTHORS ChangeLog README
%{_bindir}/%{gtkoname}
%dir %{py_sitedir}/%{oname}/
%{py_sitedir}/%{oname}/*.py*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png


%changelog
* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 0.3.8-3mdv2011.0
+ Revision: 592390
- rebuild for python 2.7

* Mon Jan 05 2009 Funda Wang <fwang@mandriva.org> 0.3.8-2mdv2009.1
+ Revision: 324925
- rebuild

* Mon Nov 24 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.8-1mdv2009.1
+ Revision: 306401
- update to new version 0.3.8

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.3.7.2-3mdv2009.0
+ Revision: 246704
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Feb 21 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.7.2-1mdv2008.1
+ Revision: 173742
- new version
- drop patch 0

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Tue Dec 18 2007 Thierry Vignaud <tv@mandriva.org> 0.3.7-2mdv2008.1
+ Revision: 132289
- patch 0: fix desktop entry

* Tue Dec 18 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.7-1mdv2008.1
+ Revision: 131933
- remove icon extension in desktop file
- new version
- do not package COPYING file
- new license policy

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Aug 21 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.6-2mdv2008.0
+ Revision: 68631
- add missing scriplets
- tune up desktop file

* Sat Aug 18 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.6-1mdv2008.0
+ Revision: 65432
- new version
- spec file clean

* Sun Jul 15 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.5-2mdv2008.0
+ Revision: 52201
- readd BR on desktop-file-utils
- correct menu category

* Sun Jul 15 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.5-1mdv2008.0
+ Revision: 52181
- new version
- drop buildrequires on desktop-file-utils
- remove X-MandrivaLinux

* Sat Apr 21 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.4-1mdv2008.0
+ Revision: 16481
- new version
- drop P0


* Tue Mar 06 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.3.1-1mdv2007.0
+ Revision: 133961
- new version

* Wed Feb 14 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.3-1mdv2007.1
+ Revision: 120665
- Import gtk-recordmydesktop

