Name:          zettelkasten
Version:       3.2.4.3
Release:       1%{?dist}
Summary:       Digital File Card System
SOURCE:        http://zettelkasten.danielluedecke.de/download/Zettelkasten3_linux.zip
URL:           http://zettelkasten.danielluedecke.de/
License:       GPL
Group:         Applications/Databases
Packager:      Wuffi

BuildArch:     noarch

BuildRequires: java-devel desktop-file-utils

Requires:      java opencsv jdom

%description
Zettelkasten is a digital file card system implementing a card catalog system designed by Niklas Luhmann with the purpose of collecting notes for texts thereby making the process of writing texts easier

%prep
%setup -q -c -n zettelkasten
cat > zettelkasten << 'EOF'
java -jar zettelkasten.jar
EOF

%build

%install
mkdir -p %{buildroot}%{_javadir}
mkdir -p %{buildroot}%{_datadir}/pixmaps
unzip -j zettelkasten.jar de/danielluedecke/zettelkasten/resources/icons/zkn3-256x256.png -d %{buildroot}%{_datadir}/pixmaps/
mv zettelkasten.jar %{buildroot}%{_javadir}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 zettelkasten %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}/usr/share/applications/%{name}.desktop << 'EOF'
[Desktop Entry]
Encoding=UTF-8
Name=Zettelkasten
Comment=Digitaler Zettelkasten
Exec=zettelkasten
Icon=/usr/share/pixmaps/zkn3-256x256.png
Type=Application
Categories=Application;Office;
Terminal=false
X-Desktop-File-Install-Version=0.21
EOF
desktop-file-validate %{buildroot}/%{_datadir}/applications/zettelkasten.desktop

%files
%{_javadir}/zettelkasten.jar
%{_bindir}/zettelkasten
%{_datadir}/applications/zettelkasten.desktop
%{_datadir}/pixmaps/zkn3-256x256.png

%changelog
*Sat Jun 14 2014 Wuffi
- Corrected errors found by rpmlint (converted tabs and made setup quiet)
*Thu Jun 12 2014 Wuffi
- Added desktop file and icon
*Wed Jun 04 2014 Wuffi
- Created initial spec file
