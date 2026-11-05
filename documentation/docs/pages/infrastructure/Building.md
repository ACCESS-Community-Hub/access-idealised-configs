# Building MOM6

!!! tip "Do you need to build MOM6?"
    The ACCESS-OM3 release module `access-om3/2026.05.004` includes the MOM6 ocean-only executable, `mom6-solo`. To find it:

    ```bash
    module use /g/data/vk83/modules
    module load access-om3/2026.05.004
    which mom6-solo
    ```

    To run it with payu, set `exe: mom6-solo` in `config.yaml` and load
    `access-om3/2026.05.004` in its `modules:` section; the scripts on the
    [configuration pages](../configurations/Overview.md) do both. The executable is built for
    Intel Sapphire Rapids CPUs, so run it on the `normalsr` queue.

You only need to build MOM6 yourself if you want to **change its source code** or use a
different version. The rest of this page shows how.

## Build your own `mom6-solo` with Spack

The script `build_mom6_solo.sh` (shown in full below):

- uses the shared [Spack](https://spack.io) 1.1 installation that ACCESS-NRI provides on Gadi
  (`module use /g/data/vk83/modules && module load spack`, as in the ACCESS-Hive docs'
  [Enable spack](https://docs.access-hive.org.au/getting_started/spack/#enable-spack));
  you need to be a member of `vk83`;
- starts from the recipe (`spack.yaml`) of an ACCESS-OM3 release;
- swaps the release's `access-om3` spec (the full coupled model) for `access-mom6`
  (`+mom6_solo ~access3`), so only the ocean-only model is built;
- reuses the release's dependencies (FMS, netCDF, MPI, ...), so it compiles only MOM6 and the
  small `access-generic-tracers` library it links to.

### Build it

From a Gadi login node, copy `build_mom6_solo.sh` (below) and run it:

```bash
PROJECT=<your-project> bash build_mom6_solo.sh
```

It works in `/g/data/<your-project>/$USER/mom6-solo-build` and prints the path of your new
`mom6-solo` at the end. It needs a CPU with AVX-512, because the release and its build tools
are compiled for `x86_64_v4`; the script checks this and stops if the CPU lacks it.

!!! warning "Not yet tested on a login node"
    Our tested build (below) ran as a PBS job on a `normalsr` (Sapphire Rapids) node, after
    downloading the sources on a login node. If the script stops on your login node because
    of AVX-512, use the two-step route below.

??? note "Two-step build (download on a login node, compile in a PBS job)"
    1. On a login node, download everything without compiling:

        ```bash
        FETCH_ONLY=1 PROJECT=<your-project> bash build_mom6_solo.sh
        ```

    2. Compile in a PBS job on a Sapphire Rapids node:

        ```bash
        qsub -q normalsr -l wd -l ncpus=8,mem=32GB,walltime=1:30:00,jobfs=20GB \
             -l storage=gdata/vk83+gdata/$PROJECT -- /bin/bash -l build_mom6_solo.sh
        ```

    Don't use Broadwell nodes (`normalbw`): without AVX-512 Spack cannot reuse any of the
    release's packages and starts compiling everything, and the release's own `cmake` crashes
    there with an illegal instruction.

??? example "build_mom6_solo.sh"
    ```bash
    --8<-- "tested-configs/build/build_mom6_solo.sh"
    ```

### Check it matches the release

A plain `md5sum` of your `mom6-solo` will never match the release's, because each executable
records where it is installed, and that shifts every address in the file. Instead, compare
what does not depend on the install location, the symbol table and the machine code
(about a minute):

```bash
bash compare_with_release.sh /path/to/your/bin/mom6-solo
```

It prints `MATCH` if your build has the same functions and the same instructions as the
release. To also check the answers, run double_gyre with your executable
(`test_own_build.sh`, below) and compare its `ocean.stats` with the
[tested run](../configurations/mom6examples/double_gyre.md).

??? example "compare_with_release.sh"
    ```bash
    --8<-- "tested-configs/build/compare_with_release.sh"
    ```

--8<-- "tested-configs/build/tested.md"

!!! info "Where Spack puts things"
    By default, installs go to `/g/data/$PROJECT/$USER/spack/1.1/release` and caches to
    `/g/data/$PROJECT/$USER/spack/1.1/`. `LOCAL_SPACK_DIRS=1` moves the install tree and
    the source/misc caches into `BUILD_DIR` (a few small cache files still go to
    `/g/data/$PROJECT/$USER/spack/1.1`).

## Additional resources for building MOM6

To **change the MOM6 source code** and build it with Spack (`spack develop`), follow ACCESS-NRI's
guide [Modify and build an ACCESS model's source code](https://docs.access-hive.org.au/models/build_a_model/build_source_code/),
using `access-mom6` as the package to develop.

Here are some other guides for building MOM6 using [FMS](https://www.gfdl.noaa.gov/fms/).
These builds will be more difficult to relate to ACCESS-OM3. Links:

 - [Building with `ninja`](https://github.com/angus-g/mom6-ninja-nci)
 - [Building with Autoconf](https://noaa-gfdl.github.io/MOM6/ac/)
 - [Presentation slides on building MOM6](https://www.marshallward.org/mom6workshop/build.html#/title-slide)
 - [Step-by-step video guide to building MOM6](https://www.youtube.com/watch?v=xuqjV1OYjbI)


