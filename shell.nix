{ nixpkgs ? import <nixpkgs> {} }: with nixpkgs;
stdenv.mkDerivation {
  name = "seL4_performance";
  buildInputs = [
    gnumake
    texlive.combined.scheme-full
  ];
}
