%define oname		recordMyDesktop
%define	gtkoname	gtk-%{oname}

Summary:	GTK fronted for recordmydesktop
Name:		gtk-recordmydesktop
Version:	0.3.4
Release:	%mkrel 1
License:	GPL
Group:		Video
URL:		http://recordmydesktop.sourceforge.net/
Source0:	http://downloads.sourceforge.net/recordmydesktop/%{name}-%{version}.tar.bz2
BuildRequires:	pygtk2.0-devel
Requires:	recordmydesktop	>= 0.3.3
BuildRequires:	desktop-file-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Frontend for recordmydesktop tool.

%prep
%setup -q

%build

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

desktop-file-install --vendor="" \
	--add-category="X-MandrivaLinux-Multimedia-Video" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*
	
%find_lang %{gtkoname}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{gtkoname}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README COPYING
%attr(755,root,root) %{_bindir}/%{gtkoname}
%dir %{py_sitedir}/%{oname}/
%{py_sitedir}/%{oname}/*.py*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
