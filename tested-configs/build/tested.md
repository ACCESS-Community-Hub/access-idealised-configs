!!! success "Tested: the build works and reproduces the release bit-for-bit"
    Tested on 2026-11-04 with ACCESS-OM3 `2026.05.004` (`access-mom6@2026.05.003`,
    ACCESS-NRI/MOM6 commit `d11a149c`), Spack 1.1 (`module load spack/1.1`) and
    access-spack-packages `2026.09.005`:

    - Sources fetched with `spack fetch` (the same commands `FETCH_ONLY=1` now runs; that option itself was added afterwards and is untested) on an internet-connected node; then the script ran
      in a `normalsr` PBS job (8 cores): **4 minutes walltime, 1.07 SU**. Spack reused all
      dependencies from the release and compiled only `access-mom6` (2 min) and
      `access-generic-tracers`.
    - Result: `.../linux-x86_64_v4/access-mom6-2026.05.003-zvhf6um.../bin/mom6-solo`
      (file md5 `1bfa03e94c085862049e6513f37bc79c`; the release's is `4785d157c76c30d8d01baf7d0f69d218`).
    - `compare_with_release.sh` on the two executables: **MATCH**. The symbol tables (md5
      `6afa1279eb4eb58a7122f8a7f074fc9b`) and the address-masked machine code (md5
      `a052e1c20fbdb1ae9e1a1b0f12cc51c4`) are identical; the file md5s differ only because the
      install path shifts the addresses.
    - We ran [double_gyre](../configurations/mom6examples/double_gyre.md) with it
      (`tested-configs/build/test_own_build.sh`). Its `ocean.stats` is **byte-for-byte
      identical** to the run with the released executable.

??? example "test_own_build.sh: check your own build with double_gyre"
    ```bash
    --8<-- "tested-configs/build/test_own_build.sh"
    ```
