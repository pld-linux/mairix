Summary:	EMail index and search tool
Summary(pl):	Narz�dzie do indeksowania i przeszukiwania poczty elektronicznej
Name:		mairix
Version:	0.15.2
Release:	2
License:	GPL
Group:		Applications/Mail
Source0:	http://www.rpcurnow.force9.co.uk/mairix/%{name}-%{version}.tar.gz
# Source0-md5:	cab61e4e95184541e6b7b4f67dfca3cc
URL:		http://www.rpcurnow.force9.co.uk/mairix/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	texconfig
BuildRequires:	texinfo-texi2dvi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mairix is a program for indexing and searching email messages stored
in Maildir, MH or mbox folders.

Some features:
* Indexing is fast. It runs incrementally on new messages - any
  particular message only gets scanned once in the lifetime of the
  index file.
* The search mode populates a "virtual" maildir (or MH) folder with
  symlinks which point to the real messages. This folder can be opened
  as usual in your mail program. (Note, if messages are in mbox
  folders, copies are made. Similarly if the virtual folder has mbox
  format, it is filled with copies of the matched messages.)
* The search mode is very fast.
* Indexing and searching works on the basis of words. The index file
  tabulates which words occur in which parts (particular headers +
  body) of which messages.

%description -l pl
mairix to program do indeksowania i przeszukiwania poczty
elektronicznej zapisanej w folderach typu Maildir, MH lub mbox.

Niekt�re mo�liwo�ci:
- Indeksowanie jest szybkie - program dzia�a przyrostowo na nowych
  wiadomo�ciach, a ka�da wiadomo�� jest skanowana tylko raz w ramach
  czasu �ycia pliku indeksu.
- Tryb przeszukiwania wype�nia "wirtualny" folder maildir (lub MH)
  dowi�zaniami wskazuj�cymi na w�a�ciwe wiadomo�ci. Folder ten mo�e
  by� normalnie otwierany w programie pocztowym. (Uwaga: je�li
  wiadomo�ci s� w folderach mbox, tworzone s� kopie. Podobnie je�li
  wirtualny folder ma format mbox, jest wype�niany kopiami pasuj�cych
  wiadomo�ci).
- Tryb przeszukiwania jest bardzo szybki.
- Indeksowanie i przeszukiwanie dzia�a w oparciu o s�owa. Plik indeksu
  tablicuje kt�re s�owa wyst�puj� w kt�rych cz�ciach (konkretnych
  nag��wkach i ciele) kt�rych wiadomo�ci.

%prep
%setup -q 

%build
./configure \
	--prefix=%{_prefix} \
	--mandir=%{_mandir}

%{__make}

%{__make} docs

for i in README NEWS ;do mv dfasyn/$i $i.dfasyn done

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install dfasyn/dfasyn $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README dotmairixrc.eg ACKNOWLEDGEMENTS  mairix.info mairix.txt mairix.html mairix.dvi mairix.pdf README.dfasyn NEWS.dfasyn
%attr(755,root,root) %{_bindir}/*
