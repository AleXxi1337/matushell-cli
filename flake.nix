{
  description = "matushell CLI utility";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-26.05";

  outputs =
    { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      packages.${system}.default = pkgs.python3Packages.buildPythonApplication {
        pname = "matushell-cli";
        version = "0.1.0";
        pyproject = true;

        src = self;

        build-system = [ pkgs.python3Packages.hatchling ];

        dependencies = with pkgs.python3Packages; [
          rich
        ];
      };
    };
}
