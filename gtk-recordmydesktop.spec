%define oname recordMyDesktop
%define	gtkoname gtk-%{oname}

Summary:	GTK fronted for recordmydesktop
Name:		gtk-recordmydesktop
Version:	0.3.6
Release:	%mkrel 1
License:	GPL
Group:		Video
URL:		http://recordmydesktop.sourceforge.net
Source0:	http://downloads.sourceforge.net/recordmydesktop/%{name}-%{version}.tar.bz2
BuildRequires:	pygtk2.0-devel
Requires:	recordmydesktop	>= %{version}
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
desktop-file-install \
	--add-category="Video" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{gtkoname}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{gtkoname}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README COPYING
%{_bindir}/%{gtkoname}
%dir %{py_sitedir}/%{oname}/
%{py_sitedir}/%{oname}/*.py*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
