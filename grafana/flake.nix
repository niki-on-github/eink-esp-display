{
  description = "Python development environment with Pillow and Requests";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        pythonEnv = pkgs.python3.withPackages (ps: with ps; [
          pillow
          requests
        ]);
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = [
            pythonEnv
          ];
          shellHook = ''
            echo "Python development environment loaded with Pillow and Requests"
            echo "Python version: $(python --version)"
            echo "Pillow version: $(python -c 'import PIL; print(PIL.__version__)')"
            echo "Requests version: $(python -c 'import requests; print(requests.__version__)')"
          '';
        };
      }
    );
}
