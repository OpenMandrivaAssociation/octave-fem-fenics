%global octpkg fem-fenics

Summary:	Toolkit for the resolution of PDE based on fenics with Octave
Name:		octave-%{octpkg}
Version:	0.0.5
Release:	3
Source0:	https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# (debian)
Patch0:		octave-value-cast.patch
Patch1:		mesheditor-celltype.patch
Patch2:		mesh-topology-global-indices.patch
Patch3:		error-format-string.patch
Patch4:		no-vtk-plot.patch
Patch5:		deprecated-declarations.patch

License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/%{octpkg}/

BuildRequires:	octave-devel >= 3.8.0
BuildRequires:	pkgconfig(dolfin)
BuildRequires:	python3dist(fenics-ufl)

Requires:	octave(api) = %{octave_api}
Requires:	python3dist(fenics-ufl)

Requires(post): octave
Requires(postun): octave

%description
Toolkit for the resolution of partial differential equations based on fenics
with Octave

%files
%license COPYING
%doc NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*
%{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}

# remove backup files
find . -name \*~ -delete

%build
export CPPFLAGS="%{optflags} -I%{py_sitedir}/ffc/backends/ufc -I%{_includedir}/eigen3 -I%{_includedir}/openmpi-%{?_arch}"
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

