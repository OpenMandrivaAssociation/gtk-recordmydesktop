Summary:	GTK fronted for recordmydesktop
Name:		gtk-recordmydesktop
Version:	0.3.8
Release:	6
License:	GPLv2+
Group:		Video
Url:		https://recordmydesktop.sourceforge.net
Source0:	http://downloads.sourceforge.net/recordmydesktop/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	desktop-file-utils
Requires:	recordmydesktop >= %{version}
BuildArch:	noarch

%description
Frontend for recordmydesktop tool.

%files -f gtk-recordMyDesktop.lang
%doc AUTHORS ChangeLog README
%{_bindir}/gtk-recordMyDesktop
%dir %{py_sitedir}/recordMyDesktop/
%{py_sitedir}/recordMyDesktop/*.py*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

#----------------------------------------------------------------------------

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

%find_lang gtk-recordMyDesktop

