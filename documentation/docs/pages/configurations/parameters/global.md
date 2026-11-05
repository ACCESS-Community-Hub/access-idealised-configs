---
search:
  exclude: true
---

# global: MOM_parameter_doc.all

Every MOM6 parameter of the tested run of [global](../mom6examples/global.md), as MOM6 wrote it to `MOM_parameter_doc.all` in the run's output folder. Line numbers match the file.

<pre class="paramdoc"><span id="L1">! This file was written by the model and records all non-layout or debugging parameters used at run-time.</span>
<span id="L2"></span>
<span id="L3">! === module MOM ===</span>
<span id="L4">SPLIT = True                    !   [Boolean] default = True</span>
<span id="L5">                                ! Use the split time stepping if true.</span>
<span id="L6">SPLIT_RK2B = False              !   [Boolean] default = False</span>
<span id="L7">                                ! If true, use a version of the split explicit time stepping scheme that</span>
<span id="L8">                                ! exchanges velocities with step_MOM that have the average barotropic phase over</span>
<span id="L9">                                ! a baroclinic timestep rather than the instantaneous barotropic phase.</span>
<span id="L10">CALC_RHO_FOR_SEA_LEVEL = False  !   [Boolean] default = False</span>
<span id="L11">                                ! If true, the in-situ density is used to calculate the effective sea level that</span>
<span id="L12">                                ! is returned to the coupler. If false, the Boussinesq parameter RHO_0 is used.</span>
<span id="L13">ENABLE_THERMODYNAMICS = True    !   [Boolean] default = True</span>
<span id="L14">                                ! If true, Temperature and salinity are used as state variables.</span>
<span id="L15">USE_EOS = True                  !   [Boolean] default = True</span>
<span id="L16">                                ! If true,  density is calculated from temperature and salinity with an equation</span>
<span id="L17">                                ! of state.  If USE_EOS is true, ENABLE_THERMODYNAMICS must be true as well.</span>
<span id="L18">DIABATIC_FIRST = False          !   [Boolean] default = False</span>
<span id="L19">                                ! If true, apply diabatic and thermodynamic processes, including buoyancy</span>
<span id="L20">                                ! forcing and mass gain or loss, before stepping the dynamics forward.</span>
<span id="L21">USE_CONTEMP_ABSSAL = False      !   [Boolean] default = False</span>
<span id="L22">                                ! If true, the prognostics T&amp;S are the conservative temperature and absolute</span>
<span id="L23">                                ! salinity. Care should be taken to convert them to potential temperature and</span>
<span id="L24">                                ! practical salinity before exchanging them with the coupler and/or reporting</span>
<span id="L25">                                ! T&amp;S diagnostics.</span>
<span id="L26">ADIABATIC = False               !   [Boolean] default = False</span>
<span id="L27">                                ! There are no diapycnal mass fluxes if ADIABATIC is true.  This assumes that KD</span>
<span id="L28">                                ! = 0.0 and that there is no buoyancy forcing, but makes the model faster by</span>
<span id="L29">                                ! eliminating subroutine calls.</span>
<span id="L30">DO_DYNAMICS = True              !   [Boolean] default = True</span>
<span id="L31">                                ! If False, skips the dynamics calls that update u &amp; v, as well as the gravity</span>
<span id="L32">                                ! wave adjustment to h. This may be a fragile feature, but can be useful during</span>
<span id="L33">                                ! development</span>
<span id="L34">OFFLINE_TRACER_MODE = False     !   [Boolean] default = False</span>
<span id="L35">                                ! If true, barotropic and baroclinic dynamics, thermodynamics are all bypassed</span>
<span id="L36">                                ! with all the fields necessary to integrate the tracer advection and diffusion</span>
<span id="L37">                                ! equation are read in from files stored from a previous integration of the</span>
<span id="L38">                                ! prognostic model. NOTE: This option only used in the ocean_solo_driver.</span>
<span id="L39">USE_REGRIDDING = False          !   [Boolean] default = False</span>
<span id="L40">                                ! If True, use the ALE algorithm (regridding/remapping). If False, use the</span>
<span id="L41">                                ! layered isopycnal algorithm.</span>
<span id="L42">BULKMIXEDLAYER = True           !   [Boolean] default = True</span>
<span id="L43">                                ! If true, use a Kraus-Turner-like bulk mixed layer with transitional buffer</span>
<span id="L44">                                ! layers.  Layers 1 through NKML+NKBL have variable densities. There must be at</span>
<span id="L45">                                ! least NKML+NKBL+1 layers if BULKMIXEDLAYER is true. BULKMIXEDLAYER can not be</span>
<span id="L46">                                ! used with USE_REGRIDDING. The default is influenced by ENABLE_THERMODYNAMICS.</span>
<span id="L47">USE_POROUS_BARRIER = False      !   [Boolean] default = False</span>
<span id="L48">                                ! If true, use porous barrier to constrain the widths and face areas at the</span>
<span id="L49">                                ! edges of the grid cells.</span>
<span id="L50">BATHYMETRY_AT_VEL = False       !   [Boolean] default = False</span>
<span id="L51">                                ! If true, there are separate values for the basin depths at velocity points.</span>
<span id="L52">                                ! Otherwise the effects of topography are entirely determined from thickness</span>
<span id="L53">                                ! points.</span>
<span id="L54">ENABLE_BUGS_BY_DEFAULT = True   !   [Boolean] default = True</span>
<span id="L55">                                ! If true, the defaults for certain recently added bug-fix flags are set to</span>
<span id="L56">                                ! recreate the bugs so that the code can be moved forward without changing</span>
<span id="L57">                                ! answers for existing configurations.  The defaults for groups of bug-fix flags</span>
<span id="L58">                                ! are periodcially changed to correct the bugs, at which point this parameter</span>
<span id="L59">                                ! will no longer be used to set their default.  Setting this to false means that</span>
<span id="L60">                                ! bugs are only used if they are actively selected, but it also means that</span>
<span id="L61">                                ! answers may change when code is updated due to newly found bugs.</span>
<span id="L62">DT = 3600.0                     !   [s]</span>
<span id="L63">                                ! The (baroclinic) dynamics time step.  The time-step that is actually used will</span>
<span id="L64">                                ! be an integer fraction of the forcing time-step (DT_FORCING in ocean-only mode</span>
<span id="L65">                                ! or the coupling timestep in coupled mode.)</span>
<span id="L66">DT_THERM = 7200.0               !   [s] default = 3600.0</span>
<span id="L67">                                ! The thermodynamic time step. Ideally DT_THERM should be an integer multiple of</span>
<span id="L68">                                ! DT and of DT_TRACER_ADVECT and less than the forcing or coupling time-step.</span>
<span id="L69">                                ! However, if THERMO_SPANS_COUPLING is true, DT_THERM can be an integer multiple</span>
<span id="L70">                                ! of the coupling timestep. By default DT_THERM is set to DT.</span>
<span id="L71">THERMO_SPANS_COUPLING = False   !   [Boolean] default = False</span>
<span id="L72">                                ! If true, the MOM will take thermodynamic timesteps that can be longer than the</span>
<span id="L73">                                ! coupling timestep. The actual thermodynamic timestep that is used in this case</span>
<span id="L74">                                ! is the largest integer multiple of the coupling timestep that is less than or</span>
<span id="L75">                                ! equal to DT_THERM.</span>
<span id="L76">DT_TRACER_ADVECT = 7200.0       !   [s] default = 7200.0</span>
<span id="L77">                                ! The tracer advection time step. Ideally DT_TRACER_ADVECT should be an integer</span>
<span id="L78">                                ! multiple of DT, less than DT_THERM, and less than the forcing or coupling</span>
<span id="L79">                                ! time-step. However, if TRADV_SPANS_COUPLING is true, DT_TRACER_ADVECT can be</span>
<span id="L80">                                ! longer than the coupling timestep. By default DT_TRACER_ADVECT is set to</span>
<span id="L81">                                ! DT_THERM.</span>
<span id="L82">TRADV_SPANS_COUPLING = False    !   [Boolean] default = False</span>
<span id="L83">                                ! If true, the MOM will take tracer advection timesteps that can be longer than</span>
<span id="L84">                                ! the coupling timestep. The actual tracer advection timestep that is used in</span>
<span id="L85">                                ! this case is the largest integer multiple of the coupling timestep that is</span>
<span id="L86">                                ! less than or equal to DT_TRACER_ADVECT.</span>
<span id="L87">THICKNESSDIFFUSE = True         !   [Boolean] default = False</span>
<span id="L88">                                ! If true, isopycnal surfaces are diffused with a Laplacian coefficient of KHTH.</span>
<span id="L89">APPLY_INTERFACE_FILTER = False  !   [Boolean] default = False</span>
<span id="L90">                                ! If true, model interface heights are subjected to a grid-scale dependent</span>
<span id="L91">                                ! spatial smoothing, often with biharmonic filter.</span>
<span id="L92">THICKNESSDIFFUSE_FIRST = True   !   [Boolean] default = False</span>
<span id="L93">                                ! If true, do thickness diffusion or interface height smoothing before dynamics.</span>
<span id="L94">                                ! This is only used if THICKNESSDIFFUSE or APPLY_INTERFACE_FILTER is true.</span>
<span id="L95">HFREEZE = -1.0                  !   [m] default = -1.0</span>
<span id="L96">                                ! If HFREEZE &gt; 0, melt potential will be computed. The actual depth over which</span>
<span id="L97">                                ! melt potential is computed will be min(HFREEZE, OBLD), where OBLD is the</span>
<span id="L98">                                ! boundary layer depth. If HFREEZE &lt;= 0 (default), melt potential will not be</span>
<span id="L99">                                ! computed.</span>
<span id="L100">INTERPOLATE_P_SURF = False      !   [Boolean] default = False</span>
<span id="L101">                                ! If true, linearly interpolate the surface pressure over the coupling time</span>
<span id="L102">                                ! step, using the specified value at the end of the step.</span>
<span id="L103">DTBT_RESET_PERIOD = 0.0         !   [s] default = 7200.0</span>
<span id="L104">                                ! The period between recalculations of DTBT (if DTBT &lt;= 0). If DTBT_RESET_PERIOD</span>
<span id="L105">                                ! is negative, DTBT is set based only on information available at</span>
<span id="L106">                                ! initialization.  If 0, DTBT will be set every dynamics time step. The default</span>
<span id="L107">                                ! is set by DT_THERM.  This is only used if SPLIT is true.</span>
<span id="L108">FRAZIL = True                   !   [Boolean] default = False</span>
<span id="L109">                                ! If true, water freezes if it gets too cold, and the accumulated heat deficit</span>
<span id="L110">                                ! is returned in the surface state.  FRAZIL is only used if</span>
<span id="L111">                                ! ENABLE_THERMODYNAMICS is true.</span>
<span id="L112">DO_GEOTHERMAL = True            !   [Boolean] default = False</span>
<span id="L113">                                ! If true, apply geothermal heating.</span>
<span id="L114">BOUND_SALINITY = True           !   [Boolean] default = False</span>
<span id="L115">                                ! If true, limit salinity to being positive. (The sea-ice model may ask for more</span>
<span id="L116">                                ! salt than is available and drive the salinity negative otherwise.)</span>
<span id="L117">MIN_SALINITY = 0.0              !   [PPT] default = 0.0</span>
<span id="L118">                                ! The minimum value of salinity when BOUND_SALINITY=True.</span>
<span id="L119">SALINITY_UNDERFLOW = 0.0        !   [PPT] default = 0.0</span>
<span id="L120">                                ! A tiny value of salinity below which the it is set to 0.  For reference, one</span>
<span id="L121">                                ! molecule of salt per square meter of ocean is of order 1e-29 ppt.</span>
<span id="L122">TEMPERATURE_UNDERFLOW = 0.0     !   [degC] default = 0.0</span>
<span id="L123">                                ! A tiny magnitude of temperatures below which they are set to 0.</span>
<span id="L124">C_P = 3925.0                    !   [J kg-1 K-1] default = 3991.86795711963</span>
<span id="L125">                                ! The heat capacity of sea water, approximated as a constant. This is only used</span>
<span id="L126">                                ! if ENABLE_THERMODYNAMICS is true. The default value is from the TEOS-10</span>
<span id="L127">                                ! definition of conservative temperature.</span>
<span id="L128">USE_PSURF_IN_EOS = True         !   [Boolean] default = True</span>
<span id="L129">                                ! If true, always include the surface pressure contributions in equation of</span>
<span id="L130">                                ! state calculations.</span>
<span id="L131">P_REF = 2.0E+07                 !   [Pa] default = 2.0E+07</span>
<span id="L132">                                ! The pressure that is used for calculating the coordinate density.  (1 Pa = 1e4</span>
<span id="L133">                                ! dbar, so 2e7 is commonly used.) This is only used if USE_EOS and</span>
<span id="L134">                                ! ENABLE_THERMODYNAMICS are true.</span>
<span id="L135">NONBLOCKING_P_SURF_BUG = True   !   [Boolean] default = True</span>
<span id="L136">                                ! If true, recover a bug in which the non-blocking halo update of the surface</span>
<span id="L137">                                ! pressure is not completed before the halo points of forces%p_surf are copied</span>
<span id="L138">                                ! into tv%p_surf, so that those halo points hold the surface pressure from the</span>
<span id="L139">                                ! previous coupling step, or zeros on the first step after a restart.  This is</span>
<span id="L140">                                ! only used if NONBLOCKING_UPDATES and USE_PSURF_IN_EOS are true</span>
<span id="L141">NKML = 2                        !   [nondim] default = 2</span>
<span id="L142">                                ! The number of sublayers within the mixed layer if BULKMIXEDLAYER is true.</span>
<span id="L143">NKBL = 2                        !   [nondim] default = 2</span>
<span id="L144">                                ! The number of layers that are used as variable density buffer layers if</span>
<span id="L145">                                ! BULKMIXEDLAYER is true.</span>
<span id="L146">FIRST_DIRECTION = 0             ! default = 0</span>
<span id="L147">                                ! An integer that indicates which direction goes first in parts of the code that</span>
<span id="L148">                                ! use directionally split updates, with even numbers (or 0) used for x- first</span>
<span id="L149">                                ! and odd numbers used for y-first.</span>
<span id="L150">ALTERNATE_FIRST_DIRECTION = False !   [Boolean] default = False</span>
<span id="L151">                                ! If true, after every dynamic timestep alternate whether the x- or y- direction</span>
<span id="L152">                                ! updates occur first in directionally split parts of the calculation. If this</span>
<span id="L153">                                ! is true, FIRST_DIRECTION applies at the start of a new run or if the next</span>
<span id="L154">                                ! first direction can not be found in the restart file.</span>
<span id="L155">CHECK_BAD_SURFACE_VALS = False  !   [Boolean] default = False</span>
<span id="L156">                                ! If true, check the surface state for ridiculous values.</span>
<span id="L157">DEFAULT_ANSWER_DATE = 99991231  ! default = 99991231</span>
<span id="L158">                                ! This sets the default value for the various _ANSWER_DATE parameters.</span>
<span id="L159">SURFACE_ANSWER_DATE = 99991231  ! default = 99991231</span>
<span id="L160">                                ! The vintage of the expressions for the surface properties.  Values below</span>
<span id="L161">                                ! 20190101 recover the answers from the end of 2018, while higher values use</span>
<span id="L162">                                ! updated and more robust forms of the same expressions.</span>
<span id="L163">SAVE_INITIAL_CONDS = True       !   [Boolean] default = False</span>
<span id="L164">                                ! If true, write the initial conditions to a file given by IC_OUTPUT_FILE.</span>
<span id="L165">IC_OUTPUT_FILE = &quot;GOLD_IC&quot;      ! default = &quot;MOM_IC&quot;</span>
<span id="L166">                                ! The file into which to write the initial conditions.</span>
<span id="L167">WRITE_GEOM = 1                  ! default = 1</span>
<span id="L168">                                ! If =0, never write the geometry and vertical grid files. If =1, write the</span>
<span id="L169">                                ! geometry and vertical grid files only for a new simulation. If =2, always</span>
<span id="L170">                                ! write the geometry and vertical grid files. Other values are invalid.</span>
<span id="L171">GEOM_FILE = &quot;ocean_geometry&quot;    ! default = &quot;ocean_geometry&quot;</span>
<span id="L172">                                ! The file into which to write the ocean geometry.</span>
<span id="L173">USE_DBCLIENT = False            !   [Boolean] default = False</span>
<span id="L174">                                ! If true, initialize a client to a remote database that can be used for online</span>
<span id="L175">                                ! analysis and machine-learning inference.</span>
<span id="L176">ICE_SHELF = False               !   [Boolean] default = False</span>
<span id="L177">                                ! If true, enables the ice shelf model.</span>
<span id="L178">USE_PARTICLES = False           !   [Boolean] default = False</span>
<span id="L179">                                ! If true, use the particles package.</span>
<span id="L180">USE_UH_PARTICLES = False        !   [Boolean] default = False</span>
<span id="L181">                                ! If true, use the uh velocity in the particles package.</span>
<span id="L182">ENSEMBLE_OCEAN = False          !   [Boolean] default = False</span>
<span id="L183">                                ! If False, The model is being run in serial mode as a single realization. If</span>
<span id="L184">                                ! True, The current model realization is part of a larger ensemble and at the</span>
<span id="L185">                                ! end of step MOM, we will perform a gather of the ensemble members for</span>
<span id="L186">                                ! statistical evaluation and/or data assimilation.</span>
<span id="L187">HOMOGENIZE_FORCINGS = False     !   [Boolean] default = False</span>
<span id="L188">                                ! If True, homogenize the forces and fluxes.</span>
<span id="L189"></span>
<span id="L190">! === module MOM_domains ===</span>
<span id="L191">REENTRANT_X = True              !   [Boolean] default = True</span>
<span id="L192">                                ! If true, the domain is zonally reentrant.</span>
<span id="L193">REENTRANT_Y = False             !   [Boolean] default = False</span>
<span id="L194">                                ! If true, the domain is meridionally reentrant.</span>
<span id="L195">TRIPOLAR_N = True               !   [Boolean] default = False</span>
<span id="L196">                                ! Use tripolar connectivity at the northern edge of the domain.  With</span>
<span id="L197">                                ! TRIPOLAR_N, NIGLOBAL must be even.</span>
<span id="L198">NIGLOBAL = 360                  !</span>
<span id="L199">                                ! The total number of thickness grid points in the x-direction in the physical</span>
<span id="L200">                                ! domain. With STATIC_MEMORY_ this is set in MOM_memory.h at compile time.</span>
<span id="L201">NJGLOBAL = 210                  !</span>
<span id="L202">                                ! The total number of thickness grid points in the y-direction in the physical</span>
<span id="L203">                                ! domain. With STATIC_MEMORY_ this is set in MOM_memory.h at compile time.</span>
<span id="L204">NIHALO = 4                      ! default = 4</span>
<span id="L205">                                ! The number of halo points on each side in the x-direction.  How this is set</span>
<span id="L206">                                ! varies with the calling component and static or dynamic memory configuration.</span>
<span id="L207">NJHALO = 4                      ! default = 4</span>
<span id="L208">                                ! The number of halo points on each side in the y-direction.  How this is set</span>
<span id="L209">                                ! varies with the calling component and static or dynamic memory configuration.</span>
<span id="L210"></span>
<span id="L211">! === module MOM_hor_index ===</span>
<span id="L212">! Sets the horizontal array index types.</span>
<span id="L213"></span>
<span id="L214">! === module MOM_grid ===</span>
<span id="L215">! Parameters providing information about the lateral grid.</span>
<span id="L216">REFERENCE_HEIGHT = 0.0          !   [m] default = 0.0</span>
<span id="L217">                                ! A reference value for geometric height fields, such as bathyT.</span>
<span id="L218"></span>
<span id="L219">! === module MOM_fixed_initialization ===</span>
<span id="L220">INPUTDIR = &quot;INPUT&quot;              ! default = &quot;.&quot;</span>
<span id="L221">                                ! The directory in which input files are found.</span>
<span id="L222"></span>
<span id="L223">! === module MOM_grid_init ===</span>
<span id="L224">GRID_CONFIG = &quot;mosaic&quot;          !</span>
<span id="L225">                                ! A character string that determines the method for defining the horizontal</span>
<span id="L226">                                ! grid.  Current options are:</span>
<span id="L227">                                !     mosaic - read the grid from a mosaic (supergrid)</span>
<span id="L228">                                !              file set by GRID_FILE.</span>
<span id="L229">                                !     cartesian - use a (flat) Cartesian grid.</span>
<span id="L230">                                !     spherical - use a simple spherical grid.</span>
<span id="L231">                                !     mercator - use a Mercator spherical grid.</span>
<span id="L232">GRID_FILE = &quot;ocean_hgrid.nc&quot;    !</span>
<span id="L233">                                ! Name of the file from which to read horizontal grid data.</span>
<span id="L234">USE_TRIPOLAR_GEOLONB_BUG = False !   [Boolean] default = False</span>
<span id="L235">                                ! If true, use older code that incorrectly sets the longitude in some points</span>
<span id="L236">                                ! along the tripolar fold to be off by 360 degrees.</span>
<span id="L237">RAD_EARTH = 6.378E+06           !   [m] default = 6.378E+06</span>
<span id="L238">                                ! The radius of the Earth.</span>
<span id="L239">TOPO_CONFIG = &quot;file&quot;            !</span>
<span id="L240">                                ! This specifies how bathymetry is specified:</span>
<span id="L241">                                !     file - read bathymetric information from the file</span>
<span id="L242">                                !       specified by (TOPO_FILE).</span>
<span id="L243">                                !     flat - flat bottom set to MAXIMUM_DEPTH.</span>
<span id="L244">                                !     bowl - an analytically specified bowl-shaped basin</span>
<span id="L245">                                !       ranging between MAXIMUM_DEPTH and MINIMUM_DEPTH.</span>
<span id="L246">                                !     spoon - a similar shape to &#x27;bowl&#x27;, but with an vertical</span>
<span id="L247">                                !       wall at the southern face.</span>
<span id="L248">                                !     halfpipe - a zonally uniform channel with a half-sine</span>
<span id="L249">                                !       profile in the meridional direction.</span>
<span id="L250">                                !     bbuilder - build topography from list of functions.</span>
<span id="L251">                                !     benchmark - use the benchmark test case topography.</span>
<span id="L252">                                !     Neverworld - use the Neverworld test case topography.</span>
<span id="L253">                                !     DOME - use a slope and channel configuration for the</span>
<span id="L254">                                !       DOME sill-overflow test case.</span>
<span id="L255">                                !     ISOMIP - use a slope and channel configuration for the</span>
<span id="L256">                                !       ISOMIP test case.</span>
<span id="L257">                                !     DOME2D - use a shelf and slope configuration for the</span>
<span id="L258">                                !       DOME2D gravity current/overflow test case.</span>
<span id="L259">                                !     Kelvin - flat but with rotated land mask.</span>
<span id="L260">                                !     seamount - Gaussian bump for spontaneous motion test case.</span>
<span id="L261">                                !     dumbbell - Sloshing channel with reservoirs on both ends.</span>
<span id="L262">                                !     shelfwave - exponential slope for shelfwave test case.</span>
<span id="L263">                                !     Phillips - ACC-like idealized topography used in the Phillips config.</span>
<span id="L264">                                !     dense - Denmark Strait-like dense water formation and overflow.</span>
<span id="L265">                                !     USER - call a user modified routine.</span>
<span id="L266">TOPO_FILE = &quot;topog.nc&quot;          ! default = &quot;topog.nc&quot;</span>
<span id="L267">                                ! The file from which the bathymetry is read.</span>
<span id="L268">TOPO_VARNAME = &quot;depth&quot;          ! default = &quot;depth&quot;</span>
<span id="L269">                                ! The name of the bathymetry variable in TOPO_FILE.</span>
<span id="L270">TOPO_EDITS_FILE = &quot;&quot;            ! default = &quot;&quot;</span>
<span id="L271">                                ! The file from which to read a list of i,j,z topography overrides.</span>
<span id="L272">ALLOW_LANDMASK_CHANGES = False  !   [Boolean] default = False</span>
<span id="L273">                                ! If true, allow topography overrides to change land mask.</span>
<span id="L274">MINIMUM_DEPTH = 0.5             !   [m] default = 0.0</span>
<span id="L275">                                ! If MASKING_DEPTH is unspecified, then anything shallower than MINIMUM_DEPTH is</span>
<span id="L276">                                ! assumed to be land and all fluxes are masked out. If MASKING_DEPTH is</span>
<span id="L277">                                ! specified, then all depths shallower than MINIMUM_DEPTH but deeper than</span>
<span id="L278">                                ! MASKING_DEPTH are rounded to MINIMUM_DEPTH.</span>
<span id="L279">MASKING_DEPTH = -9999.0         !   [m] default = -9999.0</span>
<span id="L280">                                ! The depth below which to mask points as land points, for which all fluxes are</span>
<span id="L281">                                ! zeroed out. MASKING_DEPTH is ignored if it has the special default value.</span>
<span id="L282">MAXIMUM_DEPTH = 6000.0          !   [m]</span>
<span id="L283">                                ! The maximum depth of the ocean.</span>
<span id="L284"></span>
<span id="L285">! === module MOM_open_boundary ===</span>
<span id="L286">! Controls where open boundaries are located, what kind of boundary condition to impose, and what data to apply,</span>
<span id="L287">! if any.</span>
<span id="L288">OBC_NUMBER_OF_SEGMENTS = 0      ! default = 0</span>
<span id="L289">                                ! The number of open boundary segments.</span>
<span id="L290">CHANNEL_CONFIG = &quot;global_1deg&quot;  ! default = &quot;none&quot;</span>
<span id="L291">                                ! A parameter that determines which set of channels are</span>
<span id="L292">                                ! restricted to specific  widths.  Options are:</span>
<span id="L293">                                !     none - All channels have the grid width.</span>
<span id="L294">                                !     global_1deg - Sets 16 specific channels appropriate</span>
<span id="L295">                                !       for a 1-degree model, as used in CM2G.</span>
<span id="L296">                                !     list - Read the channel locations and widths from a</span>
<span id="L297">                                !       text file, like MOM_channel_list in the MOM_SIS</span>
<span id="L298">                                !       test case.</span>
<span id="L299">                                !     file - Read open face widths everywhere from a</span>
<span id="L300">                                !       NetCDF file on the model grid.</span>
<span id="L301">SUBGRID_TOPO_AT_VEL = False     !   [Boolean] default = False</span>
<span id="L302">                                ! If true, use variables from TOPO_AT_VEL_FILE as parameters for porous barrier.</span>
<span id="L303">ROTATION = &quot;2omegasinlat&quot;       ! default = &quot;2omegasinlat&quot;</span>
<span id="L304">                                ! This specifies how the Coriolis parameter is specified:</span>
<span id="L305">                                !     2omegasinlat - Use twice the planetary rotation rate</span>
<span id="L306">                                !       times the sine of latitude.</span>
<span id="L307">                                !     betaplane - Use a beta-plane or f-plane.</span>
<span id="L308">                                !     USER - call a user modified routine.</span>
<span id="L309">OMEGA = 7.2921E-05              !   [s-1] default = 7.2921E-05</span>
<span id="L310">                                ! The rotation rate of the earth.</span>
<span id="L311">GRID_ROTATION_ANGLE_BUGS = False !   [Boolean] default = False</span>
<span id="L312">                                ! If true, use an older algorithm to calculate the sine and cosines needed</span>
<span id="L313">                                ! rotate between grid-oriented directions and true north and east.  Differences</span>
<span id="L314">                                ! arise at the tripolar fold.</span>
<span id="L315"></span>
<span id="L316">! === module MOM_verticalGrid ===</span>
<span id="L317">! Parameters providing information about the vertical grid.</span>
<span id="L318">G_EARTH = 9.8                   !   [m s-2] default = 9.8</span>
<span id="L319">                                ! The gravitational acceleration of the Earth.</span>
<span id="L320">RHO_0 = 1035.0                  !   [kg m-3] default = 1035.0</span>
<span id="L321">                                ! The mean ocean density used with BOUSSINESQ true to calculate accelerations</span>
<span id="L322">                                ! and the mass for conservation properties, or with BOUSSINSEQ false to convert</span>
<span id="L323">                                ! some parameters from vertical units of m to kg m-2.</span>
<span id="L324">BOUSSINESQ = True               !   [Boolean] default = True</span>
<span id="L325">                                ! If true, make the Boussinesq approximation.</span>
<span id="L326">ANGSTROM = 1.0E-10              !   [m] default = 1.0E-10</span>
<span id="L327">                                ! The minimum layer thickness, usually one-Angstrom.</span>
<span id="L328">H_TO_M = 1.0                    !   [m H-1] default = 1.0</span>
<span id="L329">                                ! A constant that translates the model&#x27;s internal units of thickness into m.</span>
<span id="L330">NK = 63                         !   [nondim]</span>
<span id="L331">                                ! The number of model layers.</span>
<span id="L332">ADVECTION_SCHEME_VARIANCE_UNDERFLOW = 1.0E-23 !   [Conc2 (tracer dependent)] default = 1.0E-23</span>
<span id="L333">                                ! A tiny magnitude for variance used to determine when advection scheme variance</span>
<span id="L334">                                ! production is set to 0.</span>
<span id="L335"></span>
<span id="L336">! === module MOM_tracer_registry ===</span>
<span id="L337"></span>
<span id="L338">! === module MOM_EOS ===</span>
<span id="L339">EQN_OF_STATE = &quot;WRIGHT&quot;         ! default = &quot;WRIGHT_FULL&quot;</span>
<span id="L340">                                ! EQN_OF_STATE determines which ocean equation of state should be used.</span>
<span id="L341">                                ! Currently, the valid choices are &quot;LINEAR&quot;, &quot;UNESCO&quot;, &quot;JACKETT_MCD&quot;, &quot;WRIGHT&quot;,</span>
<span id="L342">                                ! &quot;WRIGHT_REDUCED&quot;, &quot;WRIGHT_FULL&quot;, &quot;NEMO&quot;, &quot;ROQUET_RHO&quot;, &quot;ROQUET_SPV&quot; and</span>
<span id="L343">                                ! &quot;TEOS10&quot;.  This is only used if USE_EOS is true.</span>
<span id="L344">USE_WRIGHT_2ND_DERIV_BUG = False !   [Boolean] default = False</span>
<span id="L345">                                ! If true, use a bug in the calculation of the second derivatives of density</span>
<span id="L346">                                ! with temperature and with temperature and pressure that causes some terms to</span>
<span id="L347">                                ! be only 2/3 of what they should be.</span>
<span id="L348">EOS_QUADRATURE = False          !   [Boolean] default = False</span>
<span id="L349">                                ! If true, always use the generic (quadrature) code code for the integrals of</span>
<span id="L350">                                ! density.</span>
<span id="L351">TFREEZE_FORM = &quot;LINEAR&quot;         ! default = &quot;LINEAR&quot;</span>
<span id="L352">                                ! TFREEZE_FORM determines which expression should be used for the freezing</span>
<span id="L353">                                ! point.  Currently, the valid choices are &quot;LINEAR&quot;, &quot;MILLERO_78&quot;, &quot;TEOS_POLY&quot;,</span>
<span id="L354">                                ! &quot;TEOS10&quot;</span>
<span id="L355">TFREEZE_S0_P0 = 0.0             !   [degC] default = 0.0</span>
<span id="L356">                                ! When TFREEZE_FORM=LINEAR, this is the freezing potential temperature at S=0,</span>
<span id="L357">                                ! P=0.</span>
<span id="L358">DTFREEZE_DS = -0.054            !   [degC ppt-1] default = -0.054</span>
<span id="L359">                                ! When TFREEZE_FORM=LINEAR, this is the derivative of the freezing potential</span>
<span id="L360">                                ! temperature with salinity.</span>
<span id="L361">DTFREEZE_DP = 0.0               !   [degC Pa-1] default = 0.0</span>
<span id="L362">                                ! When TFREEZE_FORM=LINEAR, this is the derivative of the freezing potential</span>
<span id="L363">                                ! temperature with pressure.</span>
<span id="L364">TFREEZE_S_IS_PRACS = True       !   [Boolean] default = True</span>
<span id="L365">                                ! When True, the model will check if the model internal salinity is practical</span>
<span id="L366">                                ! salinity.  If the model uses absolute salinity, a conversion will be applied.</span>
<span id="L367">TFREEZE_T_IS_POTT = True        !   [Boolean] default = True</span>
<span id="L368">                                ! When True, the model will check if the model internal temperature is potential</span>
<span id="L369">                                ! temperature.  If the model uses conservative temperature, a conversion will be</span>
<span id="L370">                                ! applied.</span>
<span id="L371"></span>
<span id="L372">! === module MOM_restart ===</span>
<span id="L373">PARALLEL_RESTARTFILES = False   !   [Boolean] default = False</span>
<span id="L374">                                ! If true, the IO layout is used to group processors that write to the same</span>
<span id="L375">                                ! restart file or each processor writes its own (numbered) restart file. If</span>
<span id="L376">                                ! false, a single restart file is generated combining output from all PEs.</span>
<span id="L377">RESTARTFILE = &quot;MOM.res&quot;         ! default = &quot;MOM.res&quot;</span>
<span id="L378">                                ! The name-root of the restart file.</span>
<span id="L379">MAX_FIELDS = 100                ! default = 100</span>
<span id="L380">                                ! The maximum number of restart fields that can be used.</span>
<span id="L381">RESTART_CHECKSUMS_REQUIRED = True !   [Boolean] default = True</span>
<span id="L382">                                ! If true, require the restart checksums to match and error out otherwise. Users</span>
<span id="L383">                                ! may want to avoid this comparison if for example the restarts are made from a</span>
<span id="L384">                                ! run with a different mask_table than the current run, in which case the</span>
<span id="L385">                                ! checksums will not match and cause crash.</span>
<span id="L386">RESTART_SYMMETRIC_CHECKSUMS = False !   [Boolean] default = False</span>
<span id="L387">                                ! If true, do the restart checksums on all the edge points for a non-reentrant</span>
<span id="L388">                                ! grid.  This requires that SYMMETRIC_MEMORY_ is defined at compile time.</span>
<span id="L389">RESTART_UNSIGNED_ZEROS = False  !   [Boolean] default = False</span>
<span id="L390">                                ! If true, convert any negative zeros that would be written to the restart file</span>
<span id="L391">                                ! into ordinary unsigned zeros.  This does not change answers, but it can be</span>
<span id="L392">                                ! helpful in comparing restart files after grid rotation, for example.</span>
<span id="L393">USE_FILTER = False              !   [Boolean] default = False</span>
<span id="L394">                                ! If true, use streaming band-pass filters to detect the instantaneous tidal</span>
<span id="L395">                                ! signals in the simulation.</span>
<span id="L396"></span>
<span id="L397">! === module MOM_tracer_flow_control ===</span>
<span id="L398">USE_USER_TRACER_EXAMPLE = False !   [Boolean] default = False</span>
<span id="L399">                                ! If true, use the USER_tracer_example tracer package.</span>
<span id="L400">USE_DOME_TRACER = False         !   [Boolean] default = False</span>
<span id="L401">                                ! If true, use the DOME_tracer tracer package.</span>
<span id="L402">USE_ISOMIP_TRACER = False       !   [Boolean] default = False</span>
<span id="L403">                                ! If true, use the ISOMIP_tracer tracer package.</span>
<span id="L404">USE_RGC_TRACER = False          !   [Boolean] default = False</span>
<span id="L405">                                ! If true, use the RGC_tracer tracer package.</span>
<span id="L406">USE_IDEAL_AGE_TRACER = True     !   [Boolean] default = False</span>
<span id="L407">                                ! If true, use the ideal_age_example tracer package.</span>
<span id="L408">USE_MARBL_TRACERS = False       !   [Boolean] default = False</span>
<span id="L409">                                ! If true, use the MARBL tracer package.</span>
<span id="L410">USE_REGIONAL_DYES = False       !   [Boolean] default = False</span>
<span id="L411">                                ! If true, use the regional_dyes tracer package.</span>
<span id="L412">USE_FILE_DYES = False           !   [Boolean] default = False</span>
<span id="L413">                                ! If true, use the file dyes tracer package.</span>
<span id="L414">USE_OIL_TRACER = False          !   [Boolean] default = False</span>
<span id="L415">                                ! If true, use the oil_tracer tracer package.</span>
<span id="L416">USE_ADVECTION_TEST_TRACER = False !   [Boolean] default = False</span>
<span id="L417">                                ! If true, use the advection_test_tracer tracer package.</span>
<span id="L418">USE_OCMIP2_CFC = False          !   [Boolean] default = False</span>
<span id="L419">                                ! If true, use the MOM_OCMIP2_CFC tracer package.</span>
<span id="L420">USE_CFC_CAP = False             !   [Boolean] default = False</span>
<span id="L421">                                ! If true, use the MOM_CFC_cap tracer package.</span>
<span id="L422">USE_generic_tracer = False      !   [Boolean] default = False</span>
<span id="L423">                                ! If true and _USE_GENERIC_TRACER is defined as a preprocessor macro, use the</span>
<span id="L424">                                ! MOM_generic_tracer packages.</span>
<span id="L425">USE_PSEUDO_SALT_TRACER = False  !   [Boolean] default = False</span>
<span id="L426">                                ! If true, use the pseudo salt tracer, typically run as a diagnostic.</span>
<span id="L427">USE_BOUNDARY_IMPULSE_TRACER = False !   [Boolean] default = False</span>
<span id="L428">                                ! If true, use the boundary impulse tracer.</span>
<span id="L429">USE_DYED_OBC_TRACER = False     !   [Boolean] default = False</span>
<span id="L430">                                ! If true, use the dyed_obc_tracer tracer package.</span>
<span id="L431">USE_NW2_TRACERS = False         !   [Boolean] default = False</span>
<span id="L432">                                ! If true, use the NeverWorld2 tracers.</span>
<span id="L433"></span>
<span id="L434">! === module ideal_age_example ===</span>
<span id="L435">DO_IDEAL_AGE = True             !   [Boolean] default = True</span>
<span id="L436">                                ! If true, use an ideal age tracer that is set to 0 age in the boundary layer</span>
<span id="L437">                                ! and ages at unit rate in the interior.</span>
<span id="L438">DO_IDEAL_VINTAGE = False        !   [Boolean] default = False</span>
<span id="L439">                                ! If true, use an ideal vintage tracer that is set to an exponentially</span>
<span id="L440">                                ! increasing value in the boundary layer and is conserved thereafter.</span>
<span id="L441">DO_IDEAL_AGE_DATED = False      !   [Boolean] default = False</span>
<span id="L442">                                ! If true, use an ideal age tracer that is everywhere 0 before</span>
<span id="L443">                                ! IDEAL_AGE_DATED_START_YEAR, but the behaves like the standard ideal age tracer</span>
<span id="L444">                                ! - i.e. is set to 0 age in the boundary layer and ages at unit rate in the</span>
<span id="L445">                                ! interior.</span>
<span id="L446">DO_BL_RESIDENCE = False         !   [Boolean] default = False</span>
<span id="L447">                                ! If true, use a residence tracer that is set to 0 age in the interior and ages</span>
<span id="L448">                                ! at unit rate in the boundary layer.</span>
<span id="L449">USE_REAL_BL_DEPTH = False       !   [Boolean] default = False</span>
<span id="L450">                                ! If true, the ideal age tracers will use the boundary layer depth diagnosed</span>
<span id="L451">                                ! from the BL or bulkmixedlayer scheme.</span>
<span id="L452">AGE_IC_FILE = &quot;&quot;                ! default = &quot;&quot;</span>
<span id="L453">                                ! The file in which the age-tracer initial values can be found, or an empty</span>
<span id="L454">                                ! string for internal initialization.</span>
<span id="L455">AGE_IC_FILE_IS_Z = False        !   [Boolean] default = False</span>
<span id="L456">                                ! If true, AGE_IC_FILE is in depth space, not layer space</span>
<span id="L457">TRACERS_MAY_REINIT = False      !   [Boolean] default = False</span>
<span id="L458">                                ! If true, tracers may go through the initialization code if they are not found</span>
<span id="L459">                                ! in the restart files.  Otherwise it is a fatal error if the tracers are not</span>
<span id="L460">                                ! found in the restart files of a restarted run.</span>
<span id="L461"></span>
<span id="L462">! === module MOM_coord_initialization ===</span>
<span id="L463">COORD_CONFIG = &quot;file&quot;           ! default = &quot;none&quot;</span>
<span id="L464">                                ! This specifies how layers are to be defined:</span>
<span id="L465">                                !     ALE or none - used to avoid defining layers in ALE mode</span>
<span id="L466">                                !     file - read coordinate information from the file</span>
<span id="L467">                                !       specified by (COORD_FILE).</span>
<span id="L468">                                !     BFB - Custom coords for buoyancy-forced basin case</span>
<span id="L469">                                !       based on SST_S, T_BOT and DRHO_DT.</span>
<span id="L470">                                !     linear - linear based on interfaces not layers</span>
<span id="L471">                                !     layer_ref - linear based on layer densities</span>
<span id="L472">                                !     ts_ref - use reference temperature and salinity</span>
<span id="L473">                                !     ts_range - use range of temperature and salinity</span>
<span id="L474">                                !       (T_REF and S_REF) to determine surface density</span>
<span id="L475">                                !       and GINT calculate internal densities.</span>
<span id="L476">                                !     gprime - use reference density (RHO_0) for surface</span>
<span id="L477">                                !       density and GINT calculate internal densities.</span>
<span id="L478">                                !     ts_profile - use temperature and salinity profiles</span>
<span id="L479">                                !       (read from COORD_FILE) to set layer densities.</span>
<span id="L480">                                !     USER - call a user modified routine.</span>
<span id="L481">GFS = 9.8                       !   [m s-2] default = 9.8</span>
<span id="L482">                                ! The reduced gravity at the free surface.</span>
<span id="L483">COORD_FILE = &quot;GOLD_IC.2010.11.15.nc&quot; !</span>
<span id="L484">                                ! The file from which the coordinate densities are read.</span>
<span id="L485">COORD_VAR = &quot;Layer&quot;             ! default = &quot;Layer&quot;</span>
<span id="L486">                                ! The variable in COORD_FILE that is to be used for the coordinate densities.</span>
<span id="L487"></span>
<span id="L488">! === module MOM_state_initialization ===</span>
<span id="L489">FATAL_INCONSISTENT_RESTART_TIME = False !   [Boolean] default = False</span>
<span id="L490">                                ! If true and a time_in value is provided to MOM_initialize_state, verify that</span>
<span id="L491">                                ! the time read from a restart file is the same as time_in, and issue a fatal</span>
<span id="L492">                                ! error if it is not.  Otherwise, simply set the time to time_in if present.</span>
<span id="L493">INIT_LAYERS_FROM_Z_FILE = False !   [Boolean] default = False</span>
<span id="L494">                                ! If true, initialize the layer thicknesses, temperatures, and salinities from a</span>
<span id="L495">                                ! Z-space file on a latitude-longitude grid.</span>
<span id="L496">THICKNESS_CONFIG = &quot;file&quot;       ! default = &quot;uniform&quot;</span>
<span id="L497">                                ! A string that determines how the initial layer thicknesses are specified for a</span>
<span id="L498">                                ! new run:</span>
<span id="L499">                                !     file - read interface heights from the file specified</span>
<span id="L500">                                !       by (THICKNESS_FILE).</span>
<span id="L501">                                !     thickness_file - read thicknesses from the file specified</span>
<span id="L502">                                !       by (THICKNESS_FILE).</span>
<span id="L503">                                !     mass_file - read thicknesses in units of mass per unit area from the file</span>
<span id="L504">                                !       specified by (THICKNESS_FILE).</span>
<span id="L505">                                !     coord - determined by ALE coordinate.</span>
<span id="L506">                                !     uniform - uniform thickness layers evenly distributed</span>
<span id="L507">                                !       between the surface and MAXIMUM_DEPTH.</span>
<span id="L508">                                !     list - read a list of positive interface depths.</span>
<span id="L509">                                !     param - use thicknesses from parameter THICKNESS_INIT_VALUES.</span>
<span id="L510">                                !     DOME - use a slope and channel configuration for the</span>
<span id="L511">                                !       DOME sill-overflow test case.</span>
<span id="L512">                                !     ISOMIP - use a configuration for the</span>
<span id="L513">                                !       ISOMIP test case.</span>
<span id="L514">                                !     benchmark - use the benchmark test case thicknesses.</span>
<span id="L515">                                !     Neverworld - use the Neverworld test case thicknesses.</span>
<span id="L516">                                !     search - search a density profile for the interface</span>
<span id="L517">                                !       densities. This is not yet implemented.</span>
<span id="L518">                                !     circle_obcs - the circle_obcs test case is used.</span>
<span id="L519">                                !     DOME2D - 2D version of DOME initialization.</span>
<span id="L520">                                !     adjustment2d - 2D lock exchange thickness ICs.</span>
<span id="L521">                                !     sloshing - sloshing gravity thickness ICs.</span>
<span id="L522">                                !     seamount - no motion test with seamount ICs.</span>
<span id="L523">                                !     dumbbell - sloshing channel ICs.</span>
<span id="L524">                                !     soliton - Equatorial Rossby soliton.</span>
<span id="L525">                                !     rossby_front - a mixed layer front in thermal wind balance.</span>
<span id="L526">                                !     USER - call a user modified routine.</span>
<span id="L527">THICKNESS_FILE = &quot;GOLD_IC.2010.11.15.nc&quot; !</span>
<span id="L528">                                ! The name of the thickness file.</span>
<span id="L529">ADJUST_THICKNESS = True         !   [Boolean] default = False</span>
<span id="L530">                                ! If true, all mass below the bottom removed if the topography is shallower than</span>
<span id="L531">                                ! the thickness input file would indicate.</span>
<span id="L532">THICKNESS_TOLERANCE = 0.1       !   [m] default = 0.1</span>
<span id="L533">                                ! A parameter that controls the tolerance when adjusting the thickness to fit</span>
<span id="L534">                                ! the bathymetry. Used when ADJUST_THICKNESS=True.</span>
<span id="L535">INTERFACE_IC_VAR = &quot;eta&quot;        ! default = &quot;eta&quot;</span>
<span id="L536">                                ! The variable name for initial conditions for interface heights relative to</span>
<span id="L537">                                ! mean sea level, positive upward unless otherwise rescaled.</span>
<span id="L538">INTERFACE_IC_RESCALE = 1.0      !   [various] default = 1.0</span>
<span id="L539">                                ! A factor by which to rescale the initial interface heights to convert them to</span>
<span id="L540">                                ! units of m or correct sign conventions to positive upward.</span>
<span id="L541">TS_CONFIG = &quot;file&quot;              !</span>
<span id="L542">                                ! A string that determines how the initial temperatures and salinities are</span>
<span id="L543">                                ! specified for a new run:</span>
<span id="L544">                                !     file - read velocities from the file specified</span>
<span id="L545">                                !       by (TS_FILE).</span>
<span id="L546">                                !     fit - find the temperatures that are consistent with</span>
<span id="L547">                                !       the layer densities and salinity S_REF.</span>
<span id="L548">                                !     TS_profile - use temperature and salinity profiles</span>
<span id="L549">                                !       (read from TS_FILE) to set layer densities.</span>
<span id="L550">                                !     benchmark - use the benchmark test case T &amp; S.</span>
<span id="L551">                                !     linear - linear in logical layer space.</span>
<span id="L552">                                !     DOME2D - 2D DOME initialization.</span>
<span id="L553">                                !     ISOMIP - ISOMIP initialization.</span>
<span id="L554">                                !     adjustment2d - 2d lock exchange T/S ICs.</span>
<span id="L555">                                !     sloshing - sloshing mode T/S ICs.</span>
<span id="L556">                                !     seamount - no motion test with seamount ICs.</span>
<span id="L557">                                !     dumbbell - sloshing channel ICs.</span>
<span id="L558">                                !     rossby_front - a mixed layer front in thermal wind balance.</span>
<span id="L559">                                !     SCM_CVMix_tests - used in the SCM CVMix tests.</span>
<span id="L560">                                !     USER - call a user modified routine.</span>
<span id="L561">TS_FILE = &quot;GOLD_IC.2010.11.15.nc&quot; !</span>
<span id="L562">                                ! The initial condition file for temperature.</span>
<span id="L563">TEMP_IC_VAR = &quot;PTEMP&quot;           ! default = &quot;PTEMP&quot;</span>
<span id="L564">                                ! The initial condition variable for potential temperature.</span>
<span id="L565">SALT_IC_VAR = &quot;SALT&quot;            ! default = &quot;SALT&quot;</span>
<span id="L566">                                ! The initial condition variable for salinity.</span>
<span id="L567">SALT_FILE = &quot;GOLD_IC.2010.11.15.nc&quot; ! default = &quot;GOLD_IC.2010.11.15.nc&quot;</span>
<span id="L568">                                ! The initial condition file for salinity.</span>
<span id="L569">DEPRESS_INITIAL_SURFACE = False !   [Boolean] default = False</span>
<span id="L570">                                ! If true,  depress the initial surface to avoid huge tsunamis when a large</span>
<span id="L571">                                ! surface pressure is applied.</span>
<span id="L572">TRIM_IC_FOR_P_SURF = False      !   [Boolean] default = False</span>
<span id="L573">                                ! If true, cuts way the top of the column for initial conditions at the depth</span>
<span id="L574">                                ! where the hydrostatic pressure matches the imposed surface pressure which is</span>
<span id="L575">                                ! read from file.</span>
<span id="L576">VELOCITY_CONFIG = &quot;zero&quot;        ! default = &quot;zero&quot;</span>
<span id="L577">                                ! A string that determines how the initial velocities are specified for a new</span>
<span id="L578">                                ! run:</span>
<span id="L579">                                !     file - read velocities from the file specified</span>
<span id="L580">                                !       by (VELOCITY_FILE).</span>
<span id="L581">                                !     zero - the fluid is initially at rest.</span>
<span id="L582">                                !     uniform - the flow is uniform (determined by</span>
<span id="L583">                                !       parameters INITIAL_U_CONST and INITIAL_V_CONST).</span>
<span id="L584">                                !     rossby_front - a mixed layer front in thermal wind balance.</span>
<span id="L585">                                !     soliton - Equatorial Rossby soliton.</span>
<span id="L586">                                !     USER - call a user modified routine.</span>
<span id="L587">ODA_INCUPD = False              !   [Boolean] default = False</span>
<span id="L588">                                ! If true, oda incremental updates will be applied everywhere in the domain.</span>
<span id="L589">SPONGE = False                  !   [Boolean] default = False</span>
<span id="L590">                                ! If true, sponges may be applied anywhere in the domain. The exact location and</span>
<span id="L591">                                ! properties of those sponges are specified via SPONGE_CONFIG.</span>
<span id="L592"></span>
<span id="L593">! === module MOM_diag_mediator ===</span>
<span id="L594">NUM_DIAG_COORDS = 1             ! default = 1</span>
<span id="L595">                                ! The number of diagnostic vertical coordinates to use. For each coordinate, an</span>
<span id="L596">                                ! entry in DIAG_COORDS must be provided.</span>
<span id="L597">DIAG_REMAPPING_USE_OM4_SUBCELLS = True !   [Boolean] default = True</span>
<span id="L598">                                ! If true, use the OM4 remapping-via-subcells algorithm for diagnostics. See</span>
<span id="L599">                                ! REMAPPING_USE_OM4_SUBCELLS for details. We recommend setting this option to</span>
<span id="L600">                                ! false.</span>
<span id="L601">REMAPPING_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L602">                                ! The vintage of the expressions and order of arithmetic to use for remapping.</span>
<span id="L603">                                ! Values below 20190101 result in the use of older, less accurate expressions</span>
<span id="L604">                                ! that were in use at the end of 2018.  Higher values result in the use of more</span>
<span id="L605">                                ! robust and accurate forms of mathematically equivalent expressions.</span>
<span id="L606">USE_INDEX_DIAGNOSTIC_AXES = False !   [Boolean] default = False</span>
<span id="L607">                                ! If true, use a grid index coordinate convention for diagnostic axes.</span>
<span id="L608">DIAG_COORDS = &quot;z Z ZSTAR&quot;       ! default = &quot;z Z ZSTAR&quot;</span>
<span id="L609">                                ! A list of string tuples associating diag_table modules to a coordinate</span>
<span id="L610">                                ! definition used for diagnostics. Each string is of the form &quot;MODULE_SUFFIX</span>
<span id="L611">                                ! PARAMETER_SUFFIX COORDINATE_NAME&quot;.</span>
<span id="L612">DIAG_MISVAL = 1.0E+20           !   [various] default = 1.0E+20</span>
<span id="L613">                                ! Set the default missing value to use for diagnostics.</span>
<span id="L614">DIAG_AS_CHKSUM = False          !   [Boolean] default = False</span>
<span id="L615">                                ! Instead of writing diagnostics to the diag manager, write a text file</span>
<span id="L616">                                ! containing the checksum (bitcount) of the array.</span>
<span id="L617">AVAILABLE_DIAGS_FILE = &quot;available_diags.000000&quot; ! default = &quot;available_diags.000000&quot;</span>
<span id="L618">                                ! A file into which to write a list of all available ocean diagnostics that can</span>
<span id="L619">                                ! be included in a diag_table.</span>
<span id="L620">DIAG_COORD_DEF_Z = &quot;WOA09&quot;      ! default = &quot;WOA09&quot;</span>
<span id="L621">                                ! Determines how to specify the coordinate resolution. Valid options are:</span>
<span id="L622">                                !  PARAM       - use the vector-parameter DIAG_COORD_RES_Z</span>
<span id="L623">                                !  UNIFORM[:N] - uniformly distributed</span>
<span id="L624">                                !  FILE:string - read from a file. The string specifies</span>
<span id="L625">                                !                the filename and variable name, separated</span>
<span id="L626">                                !                by a comma or space, e.g. FILE:lev.nc,dz</span>
<span id="L627">                                !                or FILE:lev.nc,interfaces=zw</span>
<span id="L628">                                !  WOA09[:N]   - the WOA09 vertical grid (approximately)</span>
<span id="L629">                                !  WOA09INT[:N] - layers spanned by the WOA09 depths</span>
<span id="L630">                                !  WOA23INT[:N] - layers spanned by the WOA23 depths</span>
<span id="L631">                                !  FNC1:string - FNC1:dz_min,H_total,power,precision</span>
<span id="L632">                                !  HYBRID:string - read from a file. The string specifies</span>
<span id="L633">                                !                the filename and two variable names, separated</span>
<span id="L634">                                !                by a comma or space, for sigma-2 and dz.</span>
<span id="L635">                                !                e.g. HYBRID:vgrid.nc,sigma2,dz</span>
<span id="L636">                                !  HYBRID_3D:string - read from a file. The string specifies</span>
<span id="L637">                                !                the filename and two 3D variable names, separated</span>
<span id="L638">                                !                by a comma or space, for sigma-2 and dz. The</span>
<span id="L639">                                !                latter can be FNC1:string which is used everywhere.</span>
<span id="L640">                                !                e.g. HYBRID_3D:vgrid.nc,sigma2,dz</span>
<span id="L641">                                !  HYBRID_MAP:string - read from a file. The string specifies</span>
<span id="L642">                                !                the filename and three variable names, separated</span>
<span id="L643">                                !                by a comma or space, for map, sigma-2 and dz.</span>
<span id="L644">                                !                Map is a spatial index array with, maxval(map)=N,</span>
<span id="L645">                                !                and the others are 2D arrays containing N profiles.</span>
<span id="L646">                                !                Map typically contains integer values, but it can</span>
<span id="L647">                                !                contain real values, I+w, which imply using</span>
<span id="L648">                                !                the weighted sum of profiles I and I+1.</span>
<span id="L649">                                !                Dz can be FNC1:string which is used everywhere.</span>
<span id="L650">                                !                e.g. HYBRID_MAP:vgrid.nc,map,sigma2,dz</span>
<span id="L651"></span>
<span id="L652">! === module MOM_MEKE ===</span>
<span id="L653">USE_MEKE = True                 !   [Boolean] default = False</span>
<span id="L654">                                ! If true, turns on the MEKE scheme which calculates a sub-grid mesoscale eddy</span>
<span id="L655">                                ! kinetic energy budget.</span>
<span id="L656">MEKE_IN_DYNAMICS = True         !   [Boolean] default = True</span>
<span id="L657">                                ! If true, step MEKE forward with the dynamicsotherwise with the tracer</span>
<span id="L658">                                ! timestep.</span>
<span id="L659">EKE_SOURCE = &quot;prog&quot;             ! default = &quot;prog&quot;</span>
<span id="L660">                                ! Determine the where EKE comes from:</span>
<span id="L661">                                !   &#x27;prog&#x27;: Calculated solving EKE equation</span>
<span id="L662">                                !   &#x27;file&#x27;: Read in from a file</span>
<span id="L663">                                !   &#x27;dbclient&#x27;: Retrieved from ML-database</span>
<span id="L664">MEKE_DAMPING = 0.0              !   [s-1] default = 0.0</span>
<span id="L665">                                ! The local depth-independent MEKE dissipation rate.</span>
<span id="L666">MEKE_CD_SCALE = 0.0             !   [nondim] default = 0.0</span>
<span id="L667">                                ! The ratio of the bottom eddy velocity to the column mean eddy velocity, i.e.</span>
<span id="L668">                                ! sqrt(2*MEKE). This should be less than 1 to account for the surface</span>
<span id="L669">                                ! intensification of MEKE.</span>
<span id="L670">MEKE_CB = 25.0                  !   [nondim] default = 25.0</span>
<span id="L671">                                ! A coefficient in the expression for the ratio of bottom projected eddy energy</span>
<span id="L672">                                ! and mean column energy (see Jansen et al. 2015).</span>
<span id="L673">MEKE_MIN_GAMMA2 = 1.0E-04       !   [nondim] default = 1.0E-04</span>
<span id="L674">                                ! The minimum allowed value of gamma_b^2.</span>
<span id="L675">MEKE_CT = 50.0                  !   [nondim] default = 50.0</span>
<span id="L676">                                ! A coefficient in the expression for the ratio of barotropic eddy energy and</span>
<span id="L677">                                ! mean column energy (see Jansen et al. 2015).</span>
<span id="L678">MEKE_GMCOEFF = 1.0              !   [nondim] default = -1.0</span>
<span id="L679">                                ! The efficiency of the conversion of potential energy into MEKE by the</span>
<span id="L680">                                ! thickness mixing parameterization. If MEKE_GMCOEFF is negative, this</span>
<span id="L681">                                ! conversion is not used or calculated.</span>
<span id="L682">MEKE_GEOMETRIC = False          !   [Boolean] default = False</span>
<span id="L683">                                ! If MEKE_GEOMETRIC is true, uses the GM coefficient formulation from the</span>
<span id="L684">                                ! GEOMETRIC framework (Marshall et al., 2012).</span>
<span id="L685">MEKE_GEOMETRIC_ALPHA = 0.05     !   [nondim] default = 0.05</span>
<span id="L686">                                ! The nondimensional coefficient governing the efficiency of the GEOMETRIC</span>
<span id="L687">                                ! thickness diffusion.</span>
<span id="L688">MEKE_EQUILIBRIUM_ALT = False    !   [Boolean] default = False</span>
<span id="L689">                                ! If true, use an alternative formula for computing the (equilibrium)initial</span>
<span id="L690">                                ! value of MEKE.</span>
<span id="L691">MEKE_EQUILIBRIUM_RESTORING = False !   [Boolean] default = False</span>
<span id="L692">                                ! If true, restore MEKE back to its equilibrium value, which is calculated at</span>
<span id="L693">                                ! each time step.</span>
<span id="L694">MEKE_FRCOEFF = -1.0             !   [nondim] default = -1.0</span>
<span id="L695">                                ! The efficiency of the conversion of mean energy into MEKE.  If MEKE_FRCOEFF is</span>
<span id="L696">                                ! negative, this conversion is not used or calculated.</span>
<span id="L697">MEKE_BHFRCOEFF = -1.0           !   [nondim] default = -1.0</span>
<span id="L698">                                ! The efficiency of the conversion of mean energy into MEKE by the biharmonic</span>
<span id="L699">                                ! dissipation.  If MEKE_bhFRCOEFF is negative, this conversion is not used or</span>
<span id="L700">                                ! calculated.</span>
<span id="L701">MEKE_GMECOEFF = -1.0            !   [nondim] default = -1.0</span>
<span id="L702">                                ! The efficiency of the conversion of MEKE into mean energy by GME.  If</span>
<span id="L703">                                ! MEKE_GMECOEFF is negative, this conversion is not used or calculated.</span>
<span id="L704">MEKE_BGSRC = 0.0                !   [W kg-1] default = 0.0</span>
<span id="L705">                                ! A background energy source for MEKE.</span>
<span id="L706">MEKE_KH = -1.0                  !   [m2 s-1] default = -1.0</span>
<span id="L707">                                ! A background lateral diffusivity of MEKE. Use a negative value to not apply</span>
<span id="L708">                                ! lateral diffusion to MEKE.</span>
<span id="L709">MEKE_K4 = -1.0                  !   [m4 s-1] default = -1.0</span>
<span id="L710">                                ! A lateral bi-harmonic diffusivity of MEKE. Use a negative value to not apply</span>
<span id="L711">                                ! bi-harmonic diffusion to MEKE.</span>
<span id="L712">MEKE_DTSCALE = 1.0              !   [nondim] default = 1.0</span>
<span id="L713">                                ! A scaling factor to accelerate the time evolution of MEKE.</span>
<span id="L714">MEKE_POSITIVE = False           !   [Boolean] default = False</span>
<span id="L715">                                ! If true, it guarantees that MEKE will always be &gt;= 0.</span>
<span id="L716">MEKE_KHCOEFF = 1.0              !   [nondim] default = 1.0</span>
<span id="L717">                                ! A scaling factor in the expression for eddy diffusivity which is otherwise</span>
<span id="L718">                                ! proportional to the MEKE velocity- scale times an eddy mixing-length. This</span>
<span id="L719">                                ! factor must be &gt;0 for MEKE to contribute to the thickness/ and tracer</span>
<span id="L720">                                ! diffusivity in the rest of the model.</span>
<span id="L721">MEKE_USCALE = 0.0               !   [m s-1] default = 0.0</span>
<span id="L722">                                ! The background velocity that is combined with MEKE to calculate the bottom</span>
<span id="L723">                                ! drag.</span>
<span id="L724">MEKE_GM_SRC_ALT = False         !   [Boolean] default = False</span>
<span id="L725">                                ! If true, use the GM energy conversion form S^2*N^2*kappa rather than the</span>
<span id="L726">                                ! streamfunction for the MEKE GM source term.</span>
<span id="L727">MEKE_VISC_DRAG = True           !   [Boolean] default = True</span>
<span id="L728">                                ! If true, use the vertvisc_type to calculate the bottom drag acting on MEKE.</span>
<span id="L729">MEKE_KHTH_FAC = 0.0             !   [nondim] default = 0.0</span>
<span id="L730">                                ! A factor that maps MEKE%Kh to KhTh.</span>
<span id="L731">MEKE_KHTR_FAC = 0.0             !   [nondim] default = 0.0</span>
<span id="L732">                                ! A factor that maps MEKE%Kh to KhTr.</span>
<span id="L733">MEKE_KHMEKE_FAC = 0.0           !   [nondim] default = 0.0</span>
<span id="L734">                                ! A factor that maps MEKE%Kh to Kh for MEKE itself.</span>
<span id="L735">MEKE_OLD_LSCALE = False         !   [Boolean] default = False</span>
<span id="L736">                                ! If true, use the old formula for length scale which is a function of grid</span>
<span id="L737">                                ! spacing and deformation radius.</span>
<span id="L738">MEKE_MIN_LSCALE = False         !   [Boolean] default = False</span>
<span id="L739">                                ! If true, use a strict minimum of provided length scales rather than harmonic</span>
<span id="L740">                                ! mean.</span>
<span id="L741">MEKE_RD_MAX_SCALE = False       !   [Boolean] default = False</span>
<span id="L742">                                ! If true, the length scale used by MEKE is the minimum of the deformation</span>
<span id="L743">                                ! radius or grid-spacing. Only used if MEKE_OLD_LSCALE=True</span>
<span id="L744">MEKE_VISCOSITY_COEFF_KU = 0.0   !   [nondim] default = 0.0</span>
<span id="L745">                                ! If non-zero, is the scaling coefficient in the expression forviscosity used to</span>
<span id="L746">                                ! parameterize harmonic lateral momentum mixing byunresolved eddies represented</span>
<span id="L747">                                ! by MEKE. Can be negative torepresent backscatter from the unresolved eddies.</span>
<span id="L748">MEKE_VISCOSITY_COEFF_AU = 0.0   !   [nondim] default = 0.0</span>
<span id="L749">                                ! If non-zero, is the scaling coefficient in the expression forviscosity used to</span>
<span id="L750">                                ! parameterize biharmonic lateral momentum mixing byunresolved eddies</span>
<span id="L751">                                ! represented by MEKE. Can be negative torepresent backscatter from the</span>
<span id="L752">                                ! unresolved eddies.</span>
<span id="L753">MEKE_FIXED_MIXING_LENGTH = 0.0  !   [m] default = 0.0</span>
<span id="L754">                                ! If positive, is a fixed length contribution to the expression for mixing</span>
<span id="L755">                                ! length used in MEKE-derived diffusivity.</span>
<span id="L756">MEKE_FIXED_TOTAL_DEPTH = True   !   [Boolean] default = True</span>
<span id="L757">                                ! If true, use the nominal bathymetric depth as the estimate of the time-varying</span>
<span id="L758">                                ! ocean depth.  Otherwise base the depth on the total ocean massper unit area.</span>
<span id="L759">MEKE_ALPHA_DEFORM = 0.0         !   [nondim] default = 0.0</span>
<span id="L760">                                ! If positive, is a coefficient weighting the deformation scale in the</span>
<span id="L761">                                ! expression for mixing length used in MEKE-derived diffusivity.</span>
<span id="L762">MEKE_ALPHA_RHINES = 0.0         !   [nondim] default = 0.0</span>
<span id="L763">                                ! If positive, is a coefficient weighting the Rhines scale in the expression for</span>
<span id="L764">                                ! mixing length used in MEKE-derived diffusivity.</span>
<span id="L765">MEKE_ALPHA_EADY = 0.0           !   [nondim] default = 0.0</span>
<span id="L766">                                ! If positive, is a coefficient weighting the Eady length scale in the</span>
<span id="L767">                                ! expression for mixing length used in MEKE-derived diffusivity.</span>
<span id="L768">MEKE_ALPHA_FRICT = 0.0          !   [nondim] default = 0.0</span>
<span id="L769">                                ! If positive, is a coefficient weighting the frictional arrest scale in the</span>
<span id="L770">                                ! expression for mixing length used in MEKE-derived diffusivity.</span>
<span id="L771">MEKE_ALPHA_GRID = 0.0           !   [nondim] default = 0.0</span>
<span id="L772">                                ! If positive, is a coefficient weighting the grid-spacing as a scale in the</span>
<span id="L773">                                ! expression for mixing length used in MEKE-derived diffusivity.</span>
<span id="L774">MEKE_COLD_START = False         !   [Boolean] default = False</span>
<span id="L775">                                ! If true, initialize EKE to zero. Otherwise a local equilibrium solution is</span>
<span id="L776">                                ! used as an initial condition for EKE.</span>
<span id="L777">MEKE_BACKSCAT_RO_C = 0.0        !   [nondim] default = 0.0</span>
<span id="L778">                                ! The coefficient in the Rossby number function for scaling the biharmonic</span>
<span id="L779">                                ! frictional energy source. Setting to non-zero enables the Rossby number</span>
<span id="L780">                                ! function.</span>
<span id="L781">MEKE_BACKSCAT_RO_POW = 0.0      !   [nondim] default = 0.0</span>
<span id="L782">                                ! The power in the Rossby number function for scaling the biharmonic frictional</span>
<span id="L783">                                ! energy source.</span>
<span id="L784">MEKE_ADVECTION_FACTOR = 0.0     !   [nondim] default = 0.0</span>
<span id="L785">                                ! A scale factor in front of advection of eddy energy. Zero turns advection off.</span>
<span id="L786">                                ! Using unity would be normal but other values could accommodate a mismatch</span>
<span id="L787">                                ! between the advecting barotropic flow and the vertical structure of MEKE.</span>
<span id="L788">MEKE_TOPOGRAPHIC_BETA = 0.0     !   [nondim] default = 0.0</span>
<span id="L789">                                ! A scale factor to determine how much topographic beta is weighed in computing</span>
<span id="L790">                                ! beta in the expression of Rhines scale. Use 1 if full topographic beta effect</span>
<span id="L791">                                ! is considered; use 0 if it&#x27;s completely ignored.</span>
<span id="L792">SQG_USE_MEKE = False            !   [Boolean] default = False</span>
<span id="L793">                                ! If true, the eddy scale of MEKE is used for the SQG vertical structure</span>
<span id="L794">CDRAG = 0.003                   !   [nondim] default = 0.003</span>
<span id="L795">                                ! CDRAG is the drag coefficient relating the magnitude of the velocity field to</span>
<span id="L796">                                ! the bottom stress.</span>
<span id="L797">MEKE_CDRAG = 0.003              !   [nondim] default = 0.003</span>
<span id="L798">                                ! Drag coefficient relating the magnitude of the velocity field to the bottom</span>
<span id="L799">                                ! stress in MEKE.</span>
<span id="L800"></span>
<span id="L801">! === module MOM_lateral_mixing_coeffs ===</span>
<span id="L802">USE_VARIABLE_MIXING = True      !   [Boolean] default = False</span>
<span id="L803">                                ! If true, the variable mixing code will be called.  This allows diagnostics to</span>
<span id="L804">                                ! be created even if the scheme is not used.  If KHTR_SLOPE_CFF&gt;0 or</span>
<span id="L805">                                ! KhTh_Slope_Cff&gt;0, this is set to true regardless of what is in the parameter</span>
<span id="L806">                                ! file.</span>
<span id="L807">USE_VISBECK = False             !   [Boolean] default = False</span>
<span id="L808">                                ! If true, use the Visbeck et al. (1997) formulation for</span>
<span id="L809">                                ! thickness diffusivity.</span>
<span id="L810">RESOLN_SCALED_KH = True         !   [Boolean] default = False</span>
<span id="L811">                                ! If true, the Laplacian lateral viscosity is scaled away when the first</span>
<span id="L812">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L813">DEPTH_SCALED_KHTH = False       !   [Boolean] default = False</span>
<span id="L814">                                ! If true, KHTH is scaled away when the depth is shallowerthan a reference</span>
<span id="L815">                                ! depth: KHTH = MIN(1,H/H0)**N * KHTH, where H0 is a reference depth, controlled</span>
<span id="L816">                                ! via DEPTH_SCALED_KHTH_H0, and the exponent (N) is controlled via</span>
<span id="L817">                                ! DEPTH_SCALED_KHTH_EXP.</span>
<span id="L818">RESOLN_SCALED_KHTH = True       !   [Boolean] default = False</span>
<span id="L819">                                ! If true, the interface depth diffusivity is scaled away when the first</span>
<span id="L820">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L821">RESOLN_SCALED_KHTR = False      !   [Boolean] default = False</span>
<span id="L822">                                ! If true, the epipycnal tracer diffusivity is scaled away when the first</span>
<span id="L823">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L824">RESOLN_USE_EBT = False          !   [Boolean] default = False</span>
<span id="L825">                                ! If true, uses the equivalent barotropic wave speed instead of first baroclinic</span>
<span id="L826">                                ! wave for calculating the resolution fn.</span>
<span id="L827">BACKSCAT_EBT_POWER = 0.0        !   [nondim] default = 0.0</span>
<span id="L828">                                ! Power to raise EBT vertical structure to when backscatter has vertical</span>
<span id="L829">                                ! structure.</span>
<span id="L830">BS_USE_SQG_STRUCT = False       !   [Boolean] default = False</span>
<span id="L831">                                ! If true, the SQG vertical structure is used for backscatter on the condition</span>
<span id="L832">                                ! that BS_EBT_power=0</span>
<span id="L833">KHTH_USE_EBT_STRUCT = False     !   [Boolean] default = False</span>
<span id="L834">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L835">                                ! thickness diffusivity.</span>
<span id="L836">KHTH_USE_SQG_STRUCT = False     !   [Boolean] default = False</span>
<span id="L837">                                ! If true, uses the surface quasigeostrophic structure as the vertical structure</span>
<span id="L838">                                ! of thickness diffusivity.</span>
<span id="L839">KHTR_USE_EBT_STRUCT = False     !   [Boolean] default = False</span>
<span id="L840">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L841">                                ! tracer diffusivity.</span>
<span id="L842">KHTR_USE_SQG_STRUCT = False     !   [Boolean] default = False</span>
<span id="L843">                                ! If true, uses the surface quasigeostrophic structure as the vertical structure</span>
<span id="L844">                                ! of tracer diffusivity.</span>
<span id="L845">KD_GL90_USE_EBT_STRUCT = False  !   [Boolean] default = False</span>
<span id="L846">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L847">                                ! diffusivity in the GL90 scheme.</span>
<span id="L848">KD_GL90_USE_SQG_STRUCT = False  !   [Boolean] default = False</span>
<span id="L849">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L850">                                ! diffusivity in the GL90 scheme.</span>
<span id="L851">KHTH_SLOPE_CFF = 0.25           !   [nondim] default = 0.0</span>
<span id="L852">                                ! The nondimensional coefficient in the Visbeck formula for the interface depth</span>
<span id="L853">                                ! diffusivity</span>
<span id="L854">KHTR_SLOPE_CFF = 0.25           !   [nondim] default = 0.0</span>
<span id="L855">                                ! The nondimensional coefficient in the Visbeck formula for the epipycnal tracer</span>
<span id="L856">                                ! diffusivity</span>
<span id="L857">USE_STORED_SLOPES = False       !   [Boolean] default = False</span>
<span id="L858">                                ! If true, the isopycnal slopes are calculated once and stored for re-use. This</span>
<span id="L859">                                ! uses more memory but avoids calling the equation of state more times than</span>
<span id="L860">                                ! should be necessary.</span>
<span id="L861">VERY_SMALL_FREQUENCY = 1.0E-17  !   [s-1] default = 1.0E-17</span>
<span id="L862">                                ! A miniscule frequency that is used to avoid division by 0.  The default value</span>
<span id="L863">                                ! is roughly (pi / (the age of the universe)).</span>
<span id="L864">USE_STANLEY_ISO = False         !   [Boolean] default = False</span>
<span id="L865">                                ! If true, turn on Stanley SGS T variance parameterization in isopycnal slope</span>
<span id="L866">                                ! code.</span>
<span id="L867">KD_SMOOTH = 1.0E-06             !   [m2 s-1] default = 1.0E-06</span>
<span id="L868">                                ! A diapycnal diffusivity that is used to interpolate more sensible values of T</span>
<span id="L869">                                ! &amp; S into thin layers.</span>
<span id="L870">USE_SIMPLER_EADY_GROWTH_RATE = False !   [Boolean] default = False</span>
<span id="L871">                                ! If true, use a simpler method to calculate the Eady growth rate that avoids</span>
<span id="L872">                                ! division by layer thickness. Recommended.</span>
<span id="L873">VARMIX_KTOP = 6                 !   [nondim] default = 2</span>
<span id="L874">                                ! The layer number at which to start vertical integration of S*N for purposes of</span>
<span id="L875">                                ! finding the Eady growth rate.</span>
<span id="L876">MIN_DZ_FOR_SLOPE_N2 = 1.0       !   [m] default = 1.0</span>
<span id="L877">                                ! The minimum vertical distance to use in the denominator of the bouyancy</span>
<span id="L878">                                ! frequency used in the slope calculation.</span>
<span id="L879">FULL_DEPTH_EADY_GROWTH_RATE = False !   [Boolean] default = False</span>
<span id="L880">                                ! If true, calculate the Eady growth rate based on average slope times</span>
<span id="L881">                                ! stratification that includes contributions from sea-level changes in its</span>
<span id="L882">                                ! denominator, rather than just the nominal depth of the bathymetry.  This only</span>
<span id="L883">                                ! applies when using the model interface heights as a proxy for isopycnal</span>
<span id="L884">                                ! slopes.</span>
<span id="L885">VISBECK_L_SCALE = 3.0E+04       !   [m or nondim] default = 0.0</span>
<span id="L886">                                ! The fixed length scale in the Visbeck formula, or if negative a nondimensional</span>
<span id="L887">                                ! scaling factor relating this length scale squared to the cell areas.</span>
<span id="L888">KH_RES_SCALE_COEF = 1.0         !   [nondim] default = 1.0</span>
<span id="L889">                                ! A coefficient that determines how KhTh is scaled away if RESOLN_SCALED_... is</span>
<span id="L890">                                ! true, as F = 1 / (1 + (KH_RES_SCALE_COEF*Rd/dx)^KH_RES_FN_POWER).</span>
<span id="L891">KH_RES_FN_POWER = 2             ! default = 2</span>
<span id="L892">                                ! The power of dx/Ld in the Kh resolution function.  Any positive integer may be</span>
<span id="L893">                                ! used, although even integers are more efficient to calculate.  Setting this</span>
<span id="L894">                                ! greater than 100 results in a step-function being used.</span>
<span id="L895">VISC_RES_SCALE_COEF = 1.0       !   [nondim] default = 1.0</span>
<span id="L896">                                ! A coefficient that determines how Kh is scaled away if RESOLN_SCALED_... is</span>
<span id="L897">                                ! true, as F = 1 / (1 + (KH_RES_SCALE_COEF*Rd/dx)^KH_RES_FN_POWER). This</span>
<span id="L898">                                ! function affects lateral viscosity, Kh, and not KhTh.</span>
<span id="L899">VISC_RES_FN_POWER = 2           ! default = 2</span>
<span id="L900">                                ! The power of dx/Ld in the Kh resolution function.  Any positive integer may be</span>
<span id="L901">                                ! used, although even integers are more efficient to calculate.  Setting this</span>
<span id="L902">                                ! greater than 100 results in a step-function being used. This function affects</span>
<span id="L903">                                ! lateral viscosity, Kh, and not KhTh.</span>
<span id="L904">INTERPOLATE_RES_FN = False      !   [Boolean] default = False</span>
<span id="L905">                                ! If true, interpolate the resolution function to the velocity points from the</span>
<span id="L906">                                ! thickness points; otherwise interpolate the wave speed and calculate the</span>
<span id="L907">                                ! resolution function independently at each point.</span>
<span id="L908">GILL_EQUATORIAL_LD = True       !   [Boolean] default = True</span>
<span id="L909">                                ! If true, uses Gill&#x27;s definition of the baroclinic equatorial deformation</span>
<span id="L910">                                ! radius, otherwise, if false, use Pedlosky&#x27;s definition. These definitions</span>
<span id="L911">                                ! differ by a factor of 2 in front of the beta term in the denominator. Gill&#x27;s</span>
<span id="L912">                                ! is the more appropriate definition.</span>
<span id="L913">INTERNAL_WAVE_SPEED_TOL = 0.001 !   [nondim] default = 0.001</span>
<span id="L914">                                ! The fractional tolerance for finding the wave speeds.</span>
<span id="L915">INTERNAL_WAVE_SPEED_MIN = 0.0   !   [m s-1] default = 0.0</span>
<span id="L916">                                ! A floor in the first mode speed below which 0 used instead.</span>
<span id="L917">INTERNAL_WAVE_SPEED_BETTER_EST = True !   [Boolean] default = True</span>
<span id="L918">                                ! If true, use a more robust estimate of the first mode wave speed as the</span>
<span id="L919">                                ! starting point for iterations.</span>
<span id="L920">EBT_REMAPPING_USE_OM4_SUBCELLS = True !   [Boolean] default = True</span>
<span id="L921">                                ! If true, use the OM4 remapping-via-subcells algorithm for calculating EBT</span>
<span id="L922">                                ! structure. See REMAPPING_USE_OM4_SUBCELLS for details. We recommend setting</span>
<span id="L923">                                ! this option to false.</span>
<span id="L924">USE_QG_LEITH_GM = False         !   [Boolean] default = False</span>
<span id="L925">                                ! If true, use the QG Leith viscosity as the GM coefficient.</span>
<span id="L926"></span>
<span id="L927">! === module MOM_set_visc ===</span>
<span id="L928">SET_VISC_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L929">                                ! The vintage of the order of arithmetic and expressions in the set viscosity</span>
<span id="L930">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L931">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L932">BOTTOMDRAGLAW = True            !   [Boolean] default = True</span>
<span id="L933">                                ! If true, the bottom stress is calculated with a drag law of the form</span>
<span id="L934">                                ! c_drag*|u|*u. The velocity magnitude may be an assumed value or it may be</span>
<span id="L935">                                ! based on the actual velocity in the bottommost HBBL, depending on LINEAR_DRAG.</span>
<span id="L936">DRAG_AS_BODY_FORCE = False      !   [Boolean] default = False</span>
<span id="L937">                                ! If true, the bottom stress is imposed as an explicit body force applied over a</span>
<span id="L938">                                ! fixed distance from the bottom, rather than as an implicit calculation based</span>
<span id="L939">                                ! on an enhanced near-bottom viscosity. The thickness of the bottom boundary</span>
<span id="L940">                                ! layer is HBBL.</span>
<span id="L941">CHANNEL_DRAG = True             !   [Boolean] default = False</span>
<span id="L942">                                ! If true, the bottom drag is exerted directly on each layer proportional to the</span>
<span id="L943">                                ! fraction of the bottom it overlies.</span>
<span id="L944">LINEAR_DRAG = False             !   [Boolean] default = False</span>
<span id="L945">                                ! If LINEAR_DRAG and BOTTOMDRAGLAW are defined the drag law is</span>
<span id="L946">                                ! cdrag*DRAG_BG_VEL*u.</span>
<span id="L947">DYNAMIC_VISCOUS_ML = True       !   [Boolean] default = False</span>
<span id="L948">                                ! If true, use a bulk Richardson number criterion to determine the mixed layer</span>
<span id="L949">                                ! thickness for viscosity.</span>
<span id="L950">BULK_RI_ML_VISC = 0.05          !   [nondim] default = 0.05</span>
<span id="L951">                                ! The efficiency with which mean kinetic energy released by mechanically forced</span>
<span id="L952">                                ! entrainment of the mixed layer is converted to turbulent kinetic energy.  By</span>
<span id="L953">                                ! default, BULK_RI_ML_VISC = BULK_RI_ML or 0.</span>
<span id="L954">TKE_DECAY_VISC = 10.0           !   [nondim] default = 10.0</span>
<span id="L955">                                ! TKE_DECAY_VISC relates the vertical rate of decay of the TKE available for</span>
<span id="L956">                                ! mechanical entrainment to the natural Ekman depth for use in calculating the</span>
<span id="L957">                                ! dynamic mixed layer viscosity.  By default, TKE_DECAY_VISC = TKE_DECAY or 0.</span>
<span id="L958">ML_OMEGA_FRAC = 1.0             !   [nondim] default = 0.0</span>
<span id="L959">                                ! When setting the decay scale for turbulence, use this fraction of the absolute</span>
<span id="L960">                                ! rotation rate blended with the local value of f, as sqrt((1-of)*f^2 +</span>
<span id="L961">                                ! of*4*omega^2).</span>
<span id="L962">HBBL = 10.0                     !   [m]</span>
<span id="L963">                                ! The thickness of a bottom boundary layer with a viscosity increased by</span>
<span id="L964">                                ! KV_EXTRA_BBL if BOTTOMDRAGLAW is not defined, or the thickness over which</span>
<span id="L965">                                ! near-bottom velocities are averaged for the drag law if BOTTOMDRAGLAW is</span>
<span id="L966">                                ! defined but LINEAR_DRAG is not.</span>
<span id="L967">BBL_USE_TIDAL_BG = False        !   [Boolean] default = False</span>
<span id="L968">                                ! Flag to use the tidal RMS amplitude in place of constant background velocity</span>
<span id="L969">                                ! for computing u* in the BBL. This flag is only used when BOTTOMDRAGLAW is true</span>
<span id="L970">                                ! and LINEAR_DRAG is false.</span>
<span id="L971">DRAG_BG_VEL = 0.1               !   [m s-1] default = 0.0</span>
<span id="L972">                                ! DRAG_BG_VEL is either the assumed bottom velocity (with LINEAR_DRAG) or an</span>
<span id="L973">                                ! unresolved  velocity that is combined with the resolved velocity to estimate</span>
<span id="L974">                                ! the velocity magnitude.  DRAG_BG_VEL is only used when BOTTOMDRAGLAW is</span>
<span id="L975">                                ! defined.</span>
<span id="L976">BBL_USE_EOS = True              !   [Boolean] default = True</span>
<span id="L977">                                ! If true, use the equation of state in determining the properties of the bottom</span>
<span id="L978">                                ! boundary layer.  Otherwise use the layer target potential densities.  The</span>
<span id="L979">                                ! default of this parameter is the value of USE_EOS.</span>
<span id="L980">BBL_THICK_MIN = 0.1             !   [m] default = 0.0</span>
<span id="L981">                                ! The minimum bottom boundary layer thickness that can be used with</span>
<span id="L982">                                ! BOTTOMDRAGLAW. This might be Kv/(cdrag*drag_bg_vel) to give Kv as the minimum</span>
<span id="L983">                                ! near-bottom viscosity.</span>
<span id="L984">HTBL_SHELF_MIN = 0.1            !   [m] default = 0.1</span>
<span id="L985">                                ! The minimum top boundary layer thickness that can be used with BOTTOMDRAGLAW.</span>
<span id="L986">                                ! This might be Kv/(cdrag*drag_bg_vel) to give Kv as the minimum near-top</span>
<span id="L987">                                ! viscosity.</span>
<span id="L988">HTBL_SHELF = 10.0               !   [m] default = 10.0</span>
<span id="L989">                                ! The thickness over which near-surface velocities are averaged for the drag law</span>
<span id="L990">                                ! under an ice shelf.  By default this is the same as HBBL</span>
<span id="L991">KV = 1.0E-04                    !   [m2 s-1]</span>
<span id="L992">                                ! The background kinematic viscosity in the interior. The molecular value, ~1e-6</span>
<span id="L993">                                ! m2 s-1, may be used.</span>
<span id="L994">KV_BBL_MIN = 1.0E-04            !   [m2 s-1] default = 1.0E-04</span>
<span id="L995">                                ! The minimum viscosities in the bottom boundary layer.</span>
<span id="L996">KV_TBL_MIN = 1.0E-04            !   [m2 s-1] default = 1.0E-04</span>
<span id="L997">                                ! The minimum viscosities in the top boundary layer.</span>
<span id="L998">CORRECT_BBL_BOUNDS = False      !   [Boolean] default = False</span>
<span id="L999">                                ! If true, uses the correct bounds on the BBL thickness and viscosity so that</span>
<span id="L1000">                                ! the bottom layer feels the intended drag.</span>
<span id="L1001">SMAG_CONST_CHANNEL = 0.15       !   [nondim] default = 0.15</span>
<span id="L1002">                                ! The nondimensional Laplacian Smagorinsky constant used in calculating the</span>
<span id="L1003">                                ! channel drag if it is enabled.  The default is to use the same value as</span>
<span id="L1004">                                ! SMAG_LAP_CONST if it is defined, or 0.15 if it is not. The value used is also</span>
<span id="L1005">                                ! 0.15 if the specified value is negative.</span>
<span id="L1006">TRIG_CHANNEL_DRAG_WIDTHS = True !   [Boolean] default = True</span>
<span id="L1007">                                ! If true, use trigonometric expressions to determine the fractional open</span>
<span id="L1008">                                ! interface lengths for concave topography.</span>
<span id="L1009">CHANNEL_DRAG_MAX_BBL_THICK = 5.0 !   [m] default = 5.0</span>
<span id="L1010">                                ! The maximum bottom boundary layer thickness over which the channel drag is</span>
<span id="L1011">                                ! exerted, or a negative value for no fixed limit, instead basing the BBL</span>
<span id="L1012">                                ! thickness on the bottom stress, rotation and stratification.  The default is</span>
<span id="L1013">                                ! proportional to HBBL if USE_JACKSON_PARAM or DRAG_AS_BODY_FORCE is true.</span>
<span id="L1014"></span>
<span id="L1015">! === module MOM_thickness_diffuse ===</span>
<span id="L1016">KHTH = 10.0                     !   [m2 s-1] default = 0.0</span>
<span id="L1017">                                ! The background horizontal thickness diffusivity.</span>
<span id="L1018">READ_KHTH = False               !   [Boolean] default = False</span>
<span id="L1019">                                ! If true, read a file (given by KHTH_FILE) containing the spatially varying</span>
<span id="L1020">                                ! horizontal isopycnal height diffusivity.</span>
<span id="L1021">KHTH_MIN = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L1022">                                ! The minimum horizontal thickness diffusivity.</span>
<span id="L1023">KHTH_MAX = 900.0                !   [m2 s-1] default = 0.0</span>
<span id="L1024">                                ! The maximum horizontal thickness diffusivity.</span>
<span id="L1025">KHTH_MAX_CFL = 0.8              !   [nondimensional] default = 0.8</span>
<span id="L1026">                                ! The maximum value of the local diffusive CFL ratio that is permitted for the</span>
<span id="L1027">                                ! thickness diffusivity. 1.0 is the marginally unstable value in a pure layered</span>
<span id="L1028">                                ! model, but much smaller numbers (e.g. 0.1) seem to work better for ALE-based</span>
<span id="L1029">                                ! models.</span>
<span id="L1030">KH_ETA_CONST = 0.0              !   [m2 s-1] default = 0.0</span>
<span id="L1031">                                ! The background horizontal diffusivity of the interface heights (without</span>
<span id="L1032">                                ! considering the layer density structure).  If diffusive CFL limits are</span>
<span id="L1033">                                ! encountered, the diffusivities of the isopycnals and the interfaces heights</span>
<span id="L1034">                                ! are scaled back proportionately.</span>
<span id="L1035">KH_ETA_VEL_SCALE = 0.0          !   [m s-1] default = 0.0</span>
<span id="L1036">                                ! A velocity scale that is multiplied by the grid spacing to give a contribution</span>
<span id="L1037">                                ! to the horizontal diffusivity of the interface heights (without considering</span>
<span id="L1038">                                ! the layer density structure).</span>
<span id="L1039">DETANGLE_INTERFACES = False     !   [Boolean] default = False</span>
<span id="L1040">                                ! If defined add 3-d structured enhanced interface height diffusivities to</span>
<span id="L1041">                                ! horizontally smooth jagged layers.</span>
<span id="L1042">KHTH_SLOPE_MAX = 0.01           !   [nondim] default = 0.01</span>
<span id="L1043">                                ! A slope beyond which the calculated isopycnal slope is not reliable and is</span>
<span id="L1044">                                ! scaled away.</span>
<span id="L1045">KHTH_USE_FGNV_STREAMFUNCTION = False !   [Boolean] default = False</span>
<span id="L1046">                                ! If true, use the streamfunction formulation of Ferrari et al., 2010, which</span>
<span id="L1047">                                ! effectively emphasizes graver vertical modes by smoothing in the vertical.</span>
<span id="L1048">USE_STANLEY_GM = False          !   [Boolean] default = False</span>
<span id="L1049">                                ! If true, turn on Stanley SGS T variance parameterization in GM code.</span>
<span id="L1050">USE_KH_IN_MEKE = False          !   [Boolean] default = False</span>
<span id="L1051">                                ! If true, uses the thickness diffusivity calculated here to diffuse MEKE.</span>
<span id="L1052">USE_GME = False                 !   [Boolean] default = False</span>
<span id="L1053">                                ! If true, use the GM+E backscatter scheme in association with the Gent and</span>
<span id="L1054">                                ! McWilliams parameterization.</span>
<span id="L1055">USE_GM_WORK_BUG = False         !   [Boolean] default = False</span>
<span id="L1056">                                ! If true, compute the top-layer work tendency on the u-grid with the incorrect</span>
<span id="L1057">                                ! sign, for legacy reproducibility.</span>
<span id="L1058">STOCH_EOS = False               !   [Boolean] default = False</span>
<span id="L1059">                                ! If true, stochastic perturbations are applied to the EOS in the PGF.</span>
<span id="L1060">STANLEY_COEFF = -1.0            !   [nondim] default = -1.0</span>
<span id="L1061">                                ! Coefficient correlating the temperature gradient and SGS T variance.</span>
<span id="L1062"></span>
<span id="L1063">! === module MOM_dynamics_split_RK2 ===</span>
<span id="L1064">TIDES = True                    !   [Boolean] default = False</span>
<span id="L1065">                                ! If true, apply tidal momentum forcing.</span>
<span id="L1066">CALCULATE_SAL = True            !   [Boolean] default = True</span>
<span id="L1067">                                ! If true, calculate self-attraction and loading.</span>
<span id="L1068">USE_HA = False                  !   [Boolean] default = False</span>
<span id="L1069">                                ! If true, perform inline harmonic analysis.</span>
<span id="L1070">BE = 0.6                        !   [nondim] default = 0.6</span>
<span id="L1071">                                ! If SPLIT is true, BE determines the relative weighting of a  2nd-order</span>
<span id="L1072">                                ! Runga-Kutta baroclinic time stepping scheme (0.5) and a backward Euler scheme</span>
<span id="L1073">                                ! (1) that is used for the Coriolis and inertial terms.  BE may be from 0.5 to</span>
<span id="L1074">                                ! 1, but instability may occur near 0.5. BE is also applicable if SPLIT is false</span>
<span id="L1075">                                ! and USE_RK2 is true.</span>
<span id="L1076">BEGW = 0.0                      !   [nondim] default = 0.0</span>
<span id="L1077">                                ! If SPLIT is true, BEGW is a number from 0 to 1 that controls the extent to</span>
<span id="L1078">                                ! which the treatment of gravity waves is forward-backward (0) or simulated</span>
<span id="L1079">                                ! backward Euler (1).  0 is almost always used. If SPLIT is false and USE_RK2 is</span>
<span id="L1080">                                ! true, BEGW can be between 0 and 0.5 to damp gravity waves.</span>
<span id="L1081">SET_DTBT_USE_BT_CONT = False    !   [Boolean] default = False</span>
<span id="L1082">                                ! If true, use BT_CONT to calculate DTBT if possible.</span>
<span id="L1083">SPLIT_BOTTOM_STRESS = False     !   [Boolean] default = False</span>
<span id="L1084">                                ! If true, provide the bottom stress calculated by the vertical viscosity to the</span>
<span id="L1085">                                ! barotropic solver.</span>
<span id="L1086">BT_USE_LAYER_FLUXES = True      !   [Boolean] default = True</span>
<span id="L1087">                                ! If true, use the summed layered fluxes plus an adjustment due to the change in</span>
<span id="L1088">                                ! the barotropic velocity in the barotropic continuity equation.</span>
<span id="L1089">BT_ADJ_CORR_MASS_SRC = True     !   [Boolean] default = True</span>
<span id="L1090">                                ! If true, recalculates the barotropic mass source after predictor step. This</span>
<span id="L1091">                                ! should make little difference in the deep ocean but appears to help for</span>
<span id="L1092">                                ! vanished layers. If false, uses the same mass source as from the predictor</span>
<span id="L1093">                                ! step.</span>
<span id="L1094">STORE_CORIOLIS_ACCEL = True     !   [Boolean] default = True</span>
<span id="L1095">                                ! If true, calculate the Coriolis accelerations at the end of each timestep for</span>
<span id="L1096">                                ! use in the predictor step of the next split RK2 timestep.</span>
<span id="L1097">FPMIX = False                   !   [Boolean] default = False</span>
<span id="L1098">                                ! If true, add non-local momentum flux increments and diffuse down the Eulerian</span>
<span id="L1099">                                ! gradient.</span>
<span id="L1100">VISC_REM_BUG = False            !   [Boolean] default = False</span>
<span id="L1101">                                ! If true, visc_rem_[uv] in split mode is incorrectly calculated or accounted</span>
<span id="L1102">                                ! for in two places. This parameter controls the defaults of two individual</span>
<span id="L1103">                                ! flags, VISC_REM_TIMESTEP_BUG in MOM_dynamics_split_RK2(b) and</span>
<span id="L1104">                                ! VISC_REM_BT_WEIGHT_BUG in MOM_barotropic.</span>
<span id="L1105">VISC_REM_TIMESTEP_BUG = False   !   [Boolean] default = False</span>
<span id="L1106">                                ! If true, recover a bug that uses dt_pred rather than dt in vertvisc_remnant()</span>
<span id="L1107">                                ! at the end of predictor stage for the following continuity() and btstep()</span>
<span id="L1108">                                ! calls in the corrector step. Default of this flag is set by VISC_REM_BUG</span>
<span id="L1109"></span>
<span id="L1110">! === module MOM_continuity_PPM ===</span>
<span id="L1111">MONOTONIC_CONTINUITY = False    !   [Boolean] default = False</span>
<span id="L1112">                                ! If true, CONTINUITY_PPM uses the Colella and Woodward monotonic limiter.  The</span>
<span id="L1113">                                ! default (false) is to use a simple positive definite limiter.</span>
<span id="L1114">SIMPLE_2ND_PPM_CONTINUITY = False !   [Boolean] default = False</span>
<span id="L1115">                                ! If true, CONTINUITY_PPM uses a simple 2nd order (arithmetic mean)</span>
<span id="L1116">                                ! interpolation of the edge values. This may give better PV conservation</span>
<span id="L1117">                                ! properties. While it formally reduces the accuracy of the continuity solver</span>
<span id="L1118">                                ! itself in the strongly advective limit, it does not reduce the overall order</span>
<span id="L1119">                                ! of accuracy of the dynamic core.</span>
<span id="L1120">UPWIND_1ST_CONTINUITY = False   !   [Boolean] default = False</span>
<span id="L1121">                                ! If true, CONTINUITY_PPM becomes a 1st-order upwind continuity solver.  This</span>
<span id="L1122">                                ! scheme is highly diffusive but may be useful for debugging or in single-column</span>
<span id="L1123">                                ! mode where its minimal stencil is useful.</span>
<span id="L1124">ETA_TOLERANCE = 1.0E-06         !   [m] default = 3.15E-09</span>
<span id="L1125">                                ! The tolerance for the differences between the barotropic and baroclinic</span>
<span id="L1126">                                ! estimates of the sea surface height due to the fluxes through each face.  The</span>
<span id="L1127">                                ! total tolerance for SSH is 4 times this value.  The default is</span>
<span id="L1128">                                ! 0.5*NK*ANGSTROM, and this should not be set less than about</span>
<span id="L1129">                                ! 10^-15*MAXIMUM_DEPTH.</span>
<span id="L1130">VELOCITY_TOLERANCE = 1.0E-04    !   [m s-1] default = 3.0E+08</span>
<span id="L1131">                                ! The tolerance for barotropic velocity discrepancies between the barotropic</span>
<span id="L1132">                                ! solution and  the sum of the layer thicknesses.</span>
<span id="L1133">CONT_PPM_AGGRESS_ADJUST = False !   [Boolean] default = False</span>
<span id="L1134">                                ! If true, allow the adjusted velocities to have a relative CFL change up to</span>
<span id="L1135">                                ! 0.5.</span>
<span id="L1136">CONT_PPM_VOLUME_BASED_CFL = False !   [Boolean] default = False</span>
<span id="L1137">                                ! If true, use the ratio of the open face lengths to the tracer cell areas when</span>
<span id="L1138">                                ! estimating CFL numbers.  The default is set by CONT_PPM_AGGRESS_ADJUST.</span>
<span id="L1139">CONTINUITY_CFL_LIMIT = 0.5      !   [nondim] default = 0.5</span>
<span id="L1140">                                ! The maximum CFL of the adjusted velocities.</span>
<span id="L1141">CONT_PPM_BETTER_ITER = True     !   [Boolean] default = True</span>
<span id="L1142">                                ! If true, stop corrective iterations using a velocity based criterion and only</span>
<span id="L1143">                                ! stop if the iteration is better than all predecessors.</span>
<span id="L1144">CONT_PPM_USE_VISC_REM_MAX = True !   [Boolean] default = True</span>
<span id="L1145">                                ! If true, use more appropriate limiting bounds for corrections in strongly</span>
<span id="L1146">                                ! viscous columns.</span>
<span id="L1147">CONT_PPM_MARGINAL_FACE_AREAS = True !   [Boolean] default = True</span>
<span id="L1148">                                ! If true, use the marginal face areas from the continuity solver for use as the</span>
<span id="L1149">                                ! weights in the barotropic solver. Otherwise use the transport averaged areas.</span>
<span id="L1150"></span>
<span id="L1151">! === module MOM_CoriolisAdv ===</span>
<span id="L1152">NOSLIP = False                  !   [Boolean] default = False</span>
<span id="L1153">                                ! If true, no slip boundary conditions are used; otherwise free slip boundary</span>
<span id="L1154">                                ! conditions are assumed. The implementation of the free slip BCs on a C-grid is</span>
<span id="L1155">                                ! much cleaner than the no slip BCs. The use of free slip BCs is strongly</span>
<span id="L1156">                                ! encouraged, and no slip BCs are not used with the biharmonic viscosity.</span>
<span id="L1157">CORIOLIS_EN_DIS = False         !   [Boolean] default = False</span>
<span id="L1158">                                ! If true, two estimates of the thickness fluxes are used to estimate the</span>
<span id="L1159">                                ! Coriolis term, and the one that dissipates energy relative to the other one is</span>
<span id="L1160">                                ! used.</span>
<span id="L1161">CORIOLIS_SCHEME = &quot;SADOURNY75_ENERGY&quot; ! default = &quot;SADOURNY75_ENERGY&quot;</span>
<span id="L1162">                                ! CORIOLIS_SCHEME selects the discretization for the Coriolis terms. Valid</span>
<span id="L1163">                                ! values are:</span>
<span id="L1164">                                !    SADOURNY75_ENERGY - Sadourny, 1975; energy cons.</span>
<span id="L1165">                                !    ARAKAWA_HSU90     - Arakawa &amp; Hsu, 1990</span>
<span id="L1166">                                !    SADOURNY75_ENSTRO - Sadourny, 1975; enstrophy cons.</span>
<span id="L1167">                                !    ARAKAWA_LAMB81    - Arakawa &amp; Lamb, 1981; En. + Enst.</span>
<span id="L1168">                                !    ARAKAWA_LAMB_BLEND - A blend of Arakawa &amp; Lamb with</span>
<span id="L1169">                                !                         Arakawa &amp; Hsu and Sadourny energy</span>
<span id="L1170">                                !    WENOVI5TH_PV_ENSTRO   - 5th-order WENO PV enstrophy</span>
<span id="L1171">                                !    WENOVI3RD_PV_ENSTRO   - 3rd-order WENO PV enstrophy</span>
<span id="L1172">                                !    WENOVI7TH_PV_ENSTRO  - 7th-order WENO PV enstrophy</span>
<span id="L1173">BOUND_CORIOLIS = True           !   [Boolean] default = False</span>
<span id="L1174">                                ! If true, the Coriolis terms at u-points are bounded by the four estimates of</span>
<span id="L1175">                                ! (f+rv)v from the four neighboring v-points, and similarly at v-points.  This</span>
<span id="L1176">                                ! option would have no effect on the SADOURNY Coriolis scheme if it were</span>
<span id="L1177">                                ! possible to use centered difference thickness fluxes.</span>
<span id="L1178">KE_SCHEME = &quot;KE_ARAKAWA&quot;        ! default = &quot;KE_ARAKAWA&quot;</span>
<span id="L1179">                                ! KE_SCHEME selects the discretization for acceleration due to the kinetic</span>
<span id="L1180">                                ! energy gradient. Valid values are:</span>
<span id="L1181">                                !    KE_ARAKAWA, KE_SIMPLE_GUDONOV, KE_GUDONOV, KE_UP3</span>
<span id="L1182">PV_ADV_SCHEME = &quot;PV_ADV_CENTERED&quot; ! default = &quot;PV_ADV_CENTERED&quot;</span>
<span id="L1183">                                ! PV_ADV_SCHEME selects the discretization for PV advection. Valid values are:</span>
<span id="L1184">                                !    PV_ADV_CENTERED - centered (aka Sadourny, 75)</span>
<span id="L1185">                                !    PV_ADV_UPWIND1  - upwind, first order</span>
<span id="L1186"></span>
<span id="L1187">! === module MOM_self_attr_load ===</span>
<span id="L1188">SAL_USE_BPA = False             !   [Boolean] default = False</span>
<span id="L1189">                                ! If true, use bottom pressure anomaly to calculate self-attraction and loading</span>
<span id="L1190">                                ! (SAL). Otherwise sea surface height anomaly is used, which is only accurate</span>
<span id="L1191">                                ! for uniform density fluid.</span>
<span id="L1192">SAL_SCALAR_APPROX = True        !   [Boolean] default = True</span>
<span id="L1193">                                ! If true, use the scalar approximation to calculate self-attraction and</span>
<span id="L1194">                                ! loading.</span>
<span id="L1195">SAL_SCALAR_VALUE = 0.094        !   [m m-1] default = 0.0</span>
<span id="L1196">                                ! The constant of proportionality between self-attraction and loading (SAL)</span>
<span id="L1197">                                ! geopotential anomaly and barotropic geopotential anomaly. This is only used if</span>
<span id="L1198">                                ! SAL_SCALAR_APPROX is true or USE_PREVIOUS_TIDES is true.</span>
<span id="L1199">SAL_HARMONICS = False           !   [Boolean] default = False</span>
<span id="L1200">                                ! If true, use the online spherical harmonics method to calculate</span>
<span id="L1201">                                ! self-attraction and loading.</span>
<span id="L1202"></span>
<span id="L1203">! === module MOM_tidal_forcing ===</span>
<span id="L1204">TIDE_M2 = True                  !   [Boolean] default = False</span>
<span id="L1205">                                ! If true, apply tidal momentum forcing at the M2 frequency. This is only used</span>
<span id="L1206">                                ! if TIDES is true.</span>
<span id="L1207">TIDE_S2 = False                 !   [Boolean] default = False</span>
<span id="L1208">                                ! If true, apply tidal momentum forcing at the S2 frequency. This is only used</span>
<span id="L1209">                                ! if TIDES is true.</span>
<span id="L1210">TIDE_N2 = False                 !   [Boolean] default = False</span>
<span id="L1211">                                ! If true, apply tidal momentum forcing at the N2 frequency. This is only used</span>
<span id="L1212">                                ! if TIDES is true.</span>
<span id="L1213">TIDE_K2 = False                 !   [Boolean] default = False</span>
<span id="L1214">                                ! If true, apply tidal momentum forcing at the K2 frequency. This is only used</span>
<span id="L1215">                                ! if TIDES is true.</span>
<span id="L1216">TIDE_K1 = False                 !   [Boolean] default = False</span>
<span id="L1217">                                ! If true, apply tidal momentum forcing at the K1 frequency. This is only used</span>
<span id="L1218">                                ! if TIDES is true.</span>
<span id="L1219">TIDE_O1 = False                 !   [Boolean] default = False</span>
<span id="L1220">                                ! If true, apply tidal momentum forcing at the O1 frequency. This is only used</span>
<span id="L1221">                                ! if TIDES is true.</span>
<span id="L1222">TIDE_P1 = False                 !   [Boolean] default = False</span>
<span id="L1223">                                ! If true, apply tidal momentum forcing at the P1 frequency. This is only used</span>
<span id="L1224">                                ! if TIDES is true.</span>
<span id="L1225">TIDE_Q1 = False                 !   [Boolean] default = False</span>
<span id="L1226">                                ! If true, apply tidal momentum forcing at the Q1 frequency. This is only used</span>
<span id="L1227">                                ! if TIDES is true.</span>
<span id="L1228">TIDE_MF = False                 !   [Boolean] default = False</span>
<span id="L1229">                                ! If true, apply tidal momentum forcing at the MF frequency. This is only used</span>
<span id="L1230">                                ! if TIDES is true.</span>
<span id="L1231">TIDE_MM = False                 !   [Boolean] default = False</span>
<span id="L1232">                                ! If true, apply tidal momentum forcing at the MM frequency. This is only used</span>
<span id="L1233">                                ! if TIDES is true.</span>
<span id="L1234">TIDAL_SAL_FROM_FILE = False     !   [Boolean] default = False</span>
<span id="L1235">                                ! If true, read the tidal self-attraction and loading from input files,</span>
<span id="L1236">                                ! specified by TIDAL_INPUT_FILE. This is only used if TIDES is true.</span>
<span id="L1237">USE_PREVIOUS_TIDES = False      !   [Boolean] default = False</span>
<span id="L1238">                                ! If true, use the SAL from the previous iteration of the tides to facilitate</span>
<span id="L1239">                                ! convergent iteration. This is only used if TIDES is true.</span>
<span id="L1240">TIDE_REF_DATE = 0, 0, 0         ! default = 0, 0, 0</span>
<span id="L1241">                                ! Year,month,day to use as reference date for tidal forcing. If not specified,</span>
<span id="L1242">                                ! defaults to 0.</span>
<span id="L1243">TIDE_USE_EQ_PHASE = False       !   [Boolean] default = False</span>
<span id="L1244">                                ! Correct phases by calculating equilibrium phase arguments for TIDE_REF_DATE.</span>
<span id="L1245">TIDE_M2_FREQ = 1.405189E-04     !   [rad s-1] default = 1.405189E-04</span>
<span id="L1246">                                ! Frequency of the M2 tidal constituent. This is only used if TIDES and TIDE_M2</span>
<span id="L1247">                                ! are true, or if OBC_TIDE_N_CONSTITUENTS &gt; 0 and M2 is in</span>
<span id="L1248">                                ! OBC_TIDE_CONSTITUENTS.</span>
<span id="L1249">TIDE_M2_AMP = 0.242334          !   [m] default = 0.242334</span>
<span id="L1250">                                ! Amplitude of the M2 tidal constituent. This is only used if TIDES and TIDE_M2</span>
<span id="L1251">                                ! are true.</span>
<span id="L1252">TIDE_M2_PHASE_T0 = 0.0          !   [radians] default = 0.0</span>
<span id="L1253">                                ! Phase of the M2 tidal constituent at time 0. This is only used if TIDES and</span>
<span id="L1254">                                ! TIDE_M2 are true.</span>
<span id="L1255">TIDE_ADD_NODAL = False          !   [Boolean] default = False</span>
<span id="L1256">                                ! If true, include 18.6 year nodal modulation in the astronomical tidal forcing.</span>
<span id="L1257">TIDE_NODAL_REF_DATE = 0, 0, 0   ! default = 0, 0, 0</span>
<span id="L1258">                                ! Fixed reference date to use for nodal modulation of astronomical tidal</span>
<span id="L1259">                                ! forcing.</span>
<span id="L1260"></span>
<span id="L1261">! === module MOM_PressureForce ===</span>
<span id="L1262">ANALYTIC_FV_PGF = True          !   [Boolean] default = True</span>
<span id="L1263">                                ! If true the pressure gradient forces are calculated with a finite volume form</span>
<span id="L1264">                                ! that analytically integrates the equations of state in pressure to avoid any</span>
<span id="L1265">                                ! possibility of numerical thermobaric instability, as described in Adcroft et</span>
<span id="L1266">                                ! al., O. Mod. (2008).</span>
<span id="L1267"></span>
<span id="L1268">! === module MOM_PressureForce_FV ===</span>
<span id="L1269">RHO_PGF_REF = 1035.0            !   [kg m-3] default = 1035.0</span>
<span id="L1270">                                ! The reference density that is subtracted off when calculating pressure</span>
<span id="L1271">                                ! gradient forces.  Its inverse is subtracted off of specific volumes when in</span>
<span id="L1272">                                ! non-Boussinesq mode.  The default is RHO_0.</span>
<span id="L1273">RHO_PGF_REF_BUG = True          !   [Boolean] default = True</span>
<span id="L1274">                                ! If true, recover a bug that RHO_0 (the mean seawater density in Boussinesq</span>
<span id="L1275">                                ! mode) and RHO_PGF_REF (the subtracted reference density in finite volume</span>
<span id="L1276">                                ! pressure gradient forces) are incorrectly interchanged in several instances in</span>
<span id="L1277">                                ! Boussinesq mode.</span>
<span id="L1278">TIDES_ANSWER_DATE = 20230630    ! default = 99991231</span>
<span id="L1279">                                ! The vintage of self-attraction and loading (SAL) and tidal forcing</span>
<span id="L1280">                                ! calculations.  Setting dates before 20230701 recovers old answers (Boussinesq</span>
<span id="L1281">                                ! and non-Boussinesq modes) when SAL is part of the tidal forcing calculation.</span>
<span id="L1282">                                ! The answer difference is only at bit level and due to a reordered summation.</span>
<span id="L1283">                                ! Setting dates before 20250201 recovers answers (Boussinesq mode) that</span>
<span id="L1284">                                ! interface heights are modified before pressure force integrals are calculated.</span>
<span id="L1285">BOUSSINESQ_SAL_TIDES = False    !   [Boolean] default = False</span>
<span id="L1286">                                ! If true, in Boussinesq mode, use an alternative method to include</span>
<span id="L1287">                                ! self-attraction and loading (SAL) and tidal forcings in pressure gradient, in</span>
<span id="L1288">                                ! which their gradients are calculated separately, instead of adding</span>
<span id="L1289">                                ! geopotential anomalies as corrections to the interface height.  This</span>
<span id="L1290">                                ! alternative method elimates a baroclinic component of the SAL and tidal</span>
<span id="L1291">                                ! forcings.</span>
<span id="L1292">SSH_IN_EOS_PRESSURE_FOR_PGF = False !   [Boolean] default = False</span>
<span id="L1293">                                ! If true, include contributions from the sea surface height in the height-based</span>
<span id="L1294">                                ! pressure used in the equation of state calculations for the Boussinesq</span>
<span id="L1295">                                ! pressure gradient forces, including adjustments for atmospheric or sea-ice</span>
<span id="L1296">                                ! pressure.</span>
<span id="L1297">MASS_WEIGHT_IN_PRESSURE_GRADIENT = False !   [Boolean] default = False</span>
<span id="L1298">                                ! If true, use mass weighting when interpolating T/S for integrals near the</span>
<span id="L1299">                                ! bathymetry in FV pressure gradient calculations.</span>
<span id="L1300">MASS_WEIGHT_IN_PRESSURE_GRADIENT_TOP = False !   [Boolean] default = False</span>
<span id="L1301">                                ! If true and MASS_WEIGHT_IN_PRESSURE_GRADIENT is true, use mass weighting when</span>
<span id="L1302">                                ! interpolating T/S for integrals near the top of the water column in FV</span>
<span id="L1303">                                ! pressure gradient calculations.</span>
<span id="L1304">MASS_WEIGHT_IN_PGF_VANISHED_ONLY = False !   [Boolean] default = False</span>
<span id="L1305">                                ! If true, use mass weighting when interpolating T/S for integrals only if one</span>
<span id="L1306">                                ! side is vanished according to RESET_INTXPA_H_NONVANISHED.</span>
<span id="L1307">CORRECTION_INTXPA = False       !   [Boolean] default = False</span>
<span id="L1308">                                ! If true, use a correction for surface pressure curvature in intx_pa.</span>
<span id="L1309">RESET_INTXPA_INTEGRAL = False   !   [Boolean] default = False</span>
<span id="L1310">                                ! If true, reset INTXPA to match pressures at first nonvanished cell. Includes</span>
<span id="L1311">                                ! pressure correction.</span>
<span id="L1312">RESET_INTXPA_INTEGRAL_FLATTEST = False !   [Boolean] default = False</span>
<span id="L1313">                                ! If true, use flattest interface as reference interface where there is no</span>
<span id="L1314">                                ! better choice for RESET_INTXPA_INTEGRAL. Otherwise, use surface interface.</span>
<span id="L1315">USE_INACCURATE_PGF_RHO_ANOM = False !   [Boolean] default = False</span>
<span id="L1316">                                ! If true, use a form of the PGF that uses the reference density in an</span>
<span id="L1317">                                ! inaccurate way. This is not recommended.</span>
<span id="L1318">RECONSTRUCT_FOR_PRESSURE = False !   [Boolean] default = False</span>
<span id="L1319">                                ! If True, use vertical reconstruction of T &amp; S within the integrals of the FV</span>
<span id="L1320">                                ! pressure gradient calculation. If False, use the constant-by-layer algorithm.</span>
<span id="L1321">                                ! The default is set by USE_REGRIDDING.</span>
<span id="L1322">PRESSURE_RECONSTRUCTION_SCHEME = 1 ! default = 1</span>
<span id="L1323">                                ! Order of vertical reconstruction of T/S to use in the integrals within the FV</span>
<span id="L1324">                                ! pressure gradient calculation.</span>
<span id="L1325">                                !  0: PCM or no reconstruction.</span>
<span id="L1326">                                !  1: PLM reconstruction.</span>
<span id="L1327">                                !  2: PPM reconstruction.</span>
<span id="L1328">BOUNDARY_EXTRAPOLATION_PRESSURE = True !   [Boolean] default = True</span>
<span id="L1329">                                ! If true, the reconstruction of T &amp; S for pressure in boundary cells is</span>
<span id="L1330">                                ! extrapolated, rather than using PCM in these cells. If true, the same order</span>
<span id="L1331">                                ! polynomial is used as is used for the interior cells.</span>
<span id="L1332">USE_STANLEY_PGF = False         !   [Boolean] default = False</span>
<span id="L1333">                                ! If true, turn on Stanley SGS T variance parameterization in PGF code.</span>
<span id="L1334"></span>
<span id="L1335">! === module MOM_Zanna_Bolton ===</span>
<span id="L1336">USE_ZB2020 = False              !   [Boolean] default = False</span>
<span id="L1337">                                ! If true, turns on Zanna-Bolton-2020 (ZB) subgrid momentum parameterization of</span>
<span id="L1338">                                ! mesoscale eddies.</span>
<span id="L1339"></span>
<span id="L1340">! === module MOM_hor_visc ===</span>
<span id="L1341">USE_CIRCULATION_IN_HORVISC = False !   [Boolean] default = False</span>
<span id="L1342">                                ! Use circulation theorem to compute vorticity in horvisc module (for ZB20 or</span>
<span id="L1343">                                ! Leith)</span>
<span id="L1344">USE_CONT_THICKNESS = False      !   [Boolean] default = False</span>
<span id="L1345">                                ! If true, use thickness at velocity points from continuity solver. This option</span>
<span id="L1346">                                ! currently only works with split mode.</span>
<span id="L1347">LAPLACIAN = True                !   [Boolean] default = False</span>
<span id="L1348">                                ! If true, use a Laplacian horizontal viscosity.</span>
<span id="L1349">KH = 0.0                        !   [m2 s-1] default = 0.0</span>
<span id="L1350">                                ! The background Laplacian horizontal viscosity.</span>
<span id="L1351">KH_BG_MIN = 0.0                 !   [m2 s-1] default = 0.0</span>
<span id="L1352">                                ! The minimum value allowed for Laplacian horizontal viscosity, KH.</span>
<span id="L1353">KH_VEL_SCALE = 0.01             !   [m s-1] default = 0.0</span>
<span id="L1354">                                ! The velocity scale which is multiplied by the grid spacing to calculate the</span>
<span id="L1355">                                ! Laplacian viscosity. The final viscosity is the largest of this scaled</span>
<span id="L1356">                                ! viscosity, the Smagorinsky and Leith viscosities, and KH.</span>
<span id="L1357">KH_SIN_LAT = 0.0                !   [m2 s-1] default = 0.0</span>
<span id="L1358">                                ! The amplitude of a latitudinally-dependent background viscosity of the form</span>
<span id="L1359">                                ! KH_SIN_LAT*(SIN(LAT)**KH_PWR_OF_SINE).</span>
<span id="L1360">SMAGORINSKY_KH = False          !   [Boolean] default = False</span>
<span id="L1361">                                ! If true, use a Smagorinsky nonlinear eddy viscosity.</span>
<span id="L1362">LEITH_KH = False                !   [Boolean] default = False</span>
<span id="L1363">                                ! If true, use a Leith nonlinear eddy viscosity.</span>
<span id="L1364">RES_SCALE_MEKE_VISC = False     !   [Boolean] default = False</span>
<span id="L1365">                                ! If true, the viscosity contribution from MEKE is scaled by the resolution</span>
<span id="L1366">                                ! function.</span>
<span id="L1367">BOUND_KH = True                 !   [Boolean] default = True</span>
<span id="L1368">                                ! If true, the Laplacian coefficient is locally limited to be stable.</span>
<span id="L1369">EY24_EBT_BS = False             !   [Boolean] default = False</span>
<span id="L1370">                                ! If true, use the the backscatter scheme (EBT mode with kill switch)developed</span>
<span id="L1371">                                ! by Yankovsky et al. (2024).</span>
<span id="L1372">ANISOTROPIC_VISCOSITY = False   !   [Boolean] default = False</span>
<span id="L1373">                                ! If true, allow anistropic viscosity in the Laplacian horizontal viscosity.</span>
<span id="L1374">ADD_LES_VISCOSITY = False       !   [Boolean] default = False</span>
<span id="L1375">                                ! If true, adds the viscosity from Smagorinsky and Leith to the background</span>
<span id="L1376">                                ! viscosity instead of taking the maximum.</span>
<span id="L1377">BIHARMONIC = True               !   [Boolean] default = True</span>
<span id="L1378">                                ! If true, use a biharmonic horizontal viscosity. BIHARMONIC may be used with</span>
<span id="L1379">                                ! LAPLACIAN.</span>
<span id="L1380">AH = 0.0                        !   [m4 s-1] default = 0.0</span>
<span id="L1381">                                ! The background biharmonic horizontal viscosity.</span>
<span id="L1382">AH_VEL_SCALE = 0.05             !   [m s-1] default = 0.0</span>
<span id="L1383">                                ! The velocity scale which is multiplied by the cube of the grid spacing to</span>
<span id="L1384">                                ! calculate the biharmonic viscosity. The final viscosity is the largest of this</span>
<span id="L1385">                                ! scaled viscosity, the Smagorinsky and Leith viscosities, and AH.</span>
<span id="L1386">AH_TIME_SCALE = 0.0             !   [s] default = 0.0</span>
<span id="L1387">                                ! A time scale whose inverse is multiplied by the fourth power of the grid</span>
<span id="L1388">                                ! spacing to calculate biharmonic viscosity. The final viscosity is the largest</span>
<span id="L1389">                                ! of all viscosity formulations in use. 0.0 means that it&#x27;s not used.</span>
<span id="L1390">SMAGORINSKY_AH = True           !   [Boolean] default = False</span>
<span id="L1391">                                ! If true, use a biharmonic Smagorinsky nonlinear eddy viscosity.</span>
<span id="L1392">LEITH_AH = False                !   [Boolean] default = False</span>
<span id="L1393">                                ! If true, use a biharmonic Leith nonlinear eddy viscosity.</span>
<span id="L1394">USE_LEITHY = False              !   [Boolean] default = False</span>
<span id="L1395">                                ! If true, use a biharmonic Leith nonlinear eddy viscosity together with a</span>
<span id="L1396">                                ! harmonic backscatter.</span>
<span id="L1397">BOUND_AH = True                 !   [Boolean] default = True</span>
<span id="L1398">                                ! If true, the biharmonic coefficient is locally limited to be stable.</span>
<span id="L1399">RE_AH = 0.0                     !   [nondim] default = 0.0</span>
<span id="L1400">                                ! If nonzero, the biharmonic coefficient is scaled so that the biharmonic</span>
<span id="L1401">                                ! Reynolds number is equal to this.</span>
<span id="L1402">BACKSCATTER_UNDERBOUND = False  !   [Boolean] default = False</span>
<span id="L1403">                                ! If true, the bounds on the biharmonic viscosity are allowed to increase where</span>
<span id="L1404">                                ! the Laplacian viscosity is negative (due to backscatter parameterizations)</span>
<span id="L1405">                                ! beyond the largest timestep-dependent stable values of biharmonic viscosity</span>
<span id="L1406">                                ! when no Laplacian viscosity is applied.  The default is true for historical</span>
<span id="L1407">                                ! reasons, but this option probably should not be used because it can contribute</span>
<span id="L1408">                                ! to numerical instabilities.</span>
<span id="L1409">SMAG_BI_CONST = 0.06            !   [nondim] default = 0.0</span>
<span id="L1410">                                ! The nondimensional biharmonic Smagorinsky constant, typically 0.015 - 0.06.</span>
<span id="L1411">BOUND_CORIOLIS_BIHARM = True    !   [Boolean] default = True</span>
<span id="L1412">                                ! If true use a viscosity that increases with the square of the velocity shears,</span>
<span id="L1413">                                ! so that the resulting viscous drag is of comparable magnitude to the Coriolis</span>
<span id="L1414">                                ! terms when the velocity differences between adjacent grid points is</span>
<span id="L1415">                                ! 0.5*BOUND_CORIOLIS_VEL.  The default is the value of BOUND_CORIOLIS (or</span>
<span id="L1416">                                ! false).</span>
<span id="L1417">BOUND_CORIOLIS_VEL = 6.0        !   [m s-1] default = 6.0</span>
<span id="L1418">                                ! The velocity scale at which BOUND_CORIOLIS_BIHARM causes the biharmonic drag</span>
<span id="L1419">                                ! to have comparable magnitude to the Coriolis acceleration.  The default is set</span>
<span id="L1420">                                ! by MAXVEL.</span>
<span id="L1421">USE_LAND_MASK_FOR_HVISC = True  !   [Boolean] default = True</span>
<span id="L1422">                                ! If true, use the land mask for the computation of thicknesses at velocity</span>
<span id="L1423">                                ! locations. This eliminates the dependence on arbitrary values over land or</span>
<span id="L1424">                                ! outside of the domain.</span>
<span id="L1425">HORVISC_BOUND_COEF = 0.8        !   [nondim] default = 0.8</span>
<span id="L1426">                                ! The nondimensional coefficient of the ratio of the viscosity bounds to the</span>
<span id="L1427">                                ! theoretical maximum for stability without considering other terms.</span>
<span id="L1428">USE_KH_BG_2D = False            !   [Boolean] default = False</span>
<span id="L1429">                                ! If true, read a file containing 2-d background harmonic viscosities. The final</span>
<span id="L1430">                                ! viscosity is the maximum of the other terms and this background value.</span>
<span id="L1431">FRICTWORK_BUG = False           !   [Boolean] default = False</span>
<span id="L1432">                                ! If true, retain an answer-changing bug in calculating the FrictWork, which</span>
<span id="L1433">                                ! cancels the h in thickness flux and the h at velocity point. This isnot</span>
<span id="L1434">                                ! recommended.</span>
<span id="L1435"></span>
<span id="L1436">! === module MOM_vert_friction ===</span>
<span id="L1437">VERT_FRICTION_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1438">                                ! The vintage of the order of arithmetic and expressions in the viscous</span>
<span id="L1439">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L1440">                                ! while higher values use expressions that do not use an arbitrary hard-coded</span>
<span id="L1441">                                ! maximum viscous coupling coefficient between layers.  Values below 20230601</span>
<span id="L1442">                                ! recover a form of the viscosity within the mixed layer that breaks up the</span>
<span id="L1443">                                ! magnitude of the wind stress in some non-Boussinesq cases.</span>
<span id="L1444">DIRECT_STRESS = False           !   [Boolean] default = False</span>
<span id="L1445">                                ! If true, the wind stress is distributed over the topmost HMIX_STRESS of fluid</span>
<span id="L1446">                                ! (like in HYCOM), and an added mixed layer viscosity or a physically based</span>
<span id="L1447">                                ! boundary layer turbulence parameterization is not needed for stability.</span>
<span id="L1448">FIXED_DEPTH_LOTW_ML = False     !   [Boolean] default = False</span>
<span id="L1449">                                ! If true, use a Law-of-the-wall prescription for the mixed layer viscosity</span>
<span id="L1450">                                ! within a boundary layer that is the lesser of HMIX_FIXED and the total depth</span>
<span id="L1451">                                ! of the ocean in a column.</span>
<span id="L1452">LOTW_VISCOUS_ML_FLOOR = False   !   [Boolean] default = False</span>
<span id="L1453">                                ! If true, use a Law-of-the-wall prescription to set a lower bound on the</span>
<span id="L1454">                                ! viscous coupling between layers within the surface boundary layer, based the</span>
<span id="L1455">                                ! distance of interfaces from the surface.  This only acts when there are large</span>
<span id="L1456">                                ! changes in the thicknesses of successive layers or when the viscosity is set</span>
<span id="L1457">                                ! externally and the wind stress has subsequently increased.</span>
<span id="L1458">VON_KARMAN_CONST = 0.41         !   [nondim] default = 0.41</span>
<span id="L1459">                                ! The value the von Karman constant as used for mixed layer viscosity.</span>
<span id="L1460">HARMONIC_VISC = False           !   [Boolean] default = False</span>
<span id="L1461">                                ! If true, use the harmonic mean thicknesses for calculating the vertical</span>
<span id="L1462">                                ! viscosity.</span>
<span id="L1463">HARMONIC_BL_SCALE = 0.0         !   [nondim] default = 0.0</span>
<span id="L1464">                                ! A scale to determine when water is in the boundary layers based solely on</span>
<span id="L1465">                                ! harmonic mean thicknesses for the purpose of determining the extent to which</span>
<span id="L1466">                                ! the thicknesses used in the viscosities are upwinded.</span>
<span id="L1467">USE_GL90_IN_SSW = False         !   [Boolean] default = False</span>
<span id="L1468">                                ! If true, use simpler method to calculate 1/N^2 in GL90 vertical viscosity</span>
<span id="L1469">                                ! coefficient. This method is valid in stacked shallow water mode.</span>
<span id="L1470">CFL_TRUNCATE = 0.5              !   [nondim] default = 0.5</span>
<span id="L1471">                                ! The value of the CFL number that will cause velocity components to be</span>
<span id="L1472">                                ! truncated; instability can occur past 0.5.</span>
<span id="L1473">CFL_REPORT = 0.5                !   [nondim] default = 0.5</span>
<span id="L1474">                                ! The value of the CFL number that causes accelerations to be reported; the</span>
<span id="L1475">                                ! default is CFL_TRUNCATE.</span>
<span id="L1476">CFL_TRUNCATE_RAMP_TIME = 0.0    !   [s] default = 0.0</span>
<span id="L1477">                                ! The time over which the CFL truncation value is ramped up at the beginning of</span>
<span id="L1478">                                ! the run.</span>
<span id="L1479">CFL_TRUNCATE_START = 0.0        !   [nondim] default = 0.0</span>
<span id="L1480">                                ! The start value of the truncation CFL number used when ramping up CFL_TRUNC.</span>
<span id="L1481">STOKES_MIXING_COMBINED = False  !   [Boolean] default = False</span>
<span id="L1482">                                ! Flag to use Stokes drift Mixing via the Lagrangian  current (Eulerian plus</span>
<span id="L1483">                                ! Stokes drift).  Still needs work and testing, so not recommended for use.</span>
<span id="L1484">VEL_UNDERFLOW = 0.0             !   [m s-1] default = 0.0</span>
<span id="L1485">                                ! A negligibly small velocity magnitude below which velocity components are set</span>
<span id="L1486">                                ! to 0.  A reasonable value might be 1e-30 m/s, which is less than an Angstrom</span>
<span id="L1487">                                ! divided by the age of the universe.</span>
<span id="L1488"></span>
<span id="L1489">! === module MOM_barotropic ===</span>
<span id="L1490">USE_BT_CONT_TYPE = True         !   [Boolean] default = True</span>
<span id="L1491">                                ! If true, use a structure with elements that describe effective face areas from</span>
<span id="L1492">                                ! the summed continuity solver as a function the barotropic flow in coupling</span>
<span id="L1493">                                ! between the barotropic and baroclinic flow.  This is only used if SPLIT is</span>
<span id="L1494">                                ! true.</span>
<span id="L1495">INTEGRAL_BT_CONTINUITY = False  !   [Boolean] default = False</span>
<span id="L1496">                                ! If true, use the time-integrated velocity over the barotropic steps to</span>
<span id="L1497">                                ! determine the integrated transports used to update the continuity equation.</span>
<span id="L1498">                                ! Otherwise the transports are the sum of the transports based on a series of</span>
<span id="L1499">                                ! instantaneous velocities and the BT_CONT_TYPE for transports.  This is only</span>
<span id="L1500">                                ! valid if USE_BT_CONT_TYPE = True.</span>
<span id="L1501">BOUND_BT_CORRECTION = True      !   [Boolean] default = False</span>
<span id="L1502">                                ! If true, the corrective pseudo mass-fluxes into the barotropic solver are</span>
<span id="L1503">                                ! limited to values that require less than maxCFL_BT_cont to be accommodated.</span>
<span id="L1504">BT_CONT_CORR_BOUNDS = True      !   [Boolean] default = True</span>
<span id="L1505">                                ! If true, and BOUND_BT_CORRECTION is true, use the BT_cont_type variables to</span>
<span id="L1506">                                ! set limits determined by MAXCFL_BT_CONT on the CFL number of the velocities</span>
<span id="L1507">                                ! that are likely to be driven by the corrective mass fluxes.</span>
<span id="L1508">ADJUST_BT_CONT = False          !   [Boolean] default = False</span>
<span id="L1509">                                ! If true, adjust the curve fit to the BT_cont type that is used by the</span>
<span id="L1510">                                ! barotropic solver to match the transport about which the flow is being</span>
<span id="L1511">                                ! linearized.</span>
<span id="L1512">GRADUAL_BT_ICS = False          !   [Boolean] default = False</span>
<span id="L1513">                                ! If true, adjust the initial conditions for the barotropic solver to the values</span>
<span id="L1514">                                ! from the layered solution over a whole timestep instead of instantly. This is</span>
<span id="L1515">                                ! a decent approximation to the inclusion of sum(u dh_dt) while also correcting</span>
<span id="L1516">                                ! for truncation errors.</span>
<span id="L1517">BT_USE_VISC_REM_U_UH0 = False   !   [Boolean] default = False</span>
<span id="L1518">                                ! If true, use the viscous remnants when estimating the barotropic velocities</span>
<span id="L1519">                                ! that were used to calculate uh0 and vh0.  False is probably the better choice.</span>
<span id="L1520">BT_PROJECT_VELOCITY = True      !   [Boolean] default = False</span>
<span id="L1521">                                ! If true, step the barotropic velocity first and project out the velocity</span>
<span id="L1522">                                ! tendency by 1+BEBT when calculating the transport.  The default (false) is to</span>
<span id="L1523">                                ! use a predictor continuity step to find the pressure field, and then to do a</span>
<span id="L1524">                                ! corrector continuity step using a weighted average of the old and new</span>
<span id="L1525">                                ! velocities, with weights of (1-BEBT) and BEBT.</span>
<span id="L1526">BT_NONLIN_STRESS = False        !   [Boolean] default = False</span>
<span id="L1527">                                ! If true, use the full depth of the ocean at the start of the barotropic step</span>
<span id="L1528">                                ! when calculating the surface stress contribution to the barotropic</span>
<span id="L1529">                                ! acclerations.  Otherwise use the depth based on bathyT.</span>
<span id="L1530">DYNAMIC_SURFACE_PRESSURE = False !   [Boolean] default = False</span>
<span id="L1531">                                ! If true, add a dynamic pressure due to a viscous ice shelf, for instance.</span>
<span id="L1532">BT_CORIOLIS_SCALE = 1.0         !   [nondim] default = 1.0</span>
<span id="L1533">                                ! A factor by which the barotropic Coriolis anomaly terms are scaled.</span>
<span id="L1534">BAROTROPIC_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1535">                                ! The vintage of the expressions in the barotropic solver. Values below 20190101</span>
<span id="L1536">                                ! recover the answers from the end of 2018, while higher values use more</span>
<span id="L1537">                                ! efficient or general expressions.</span>
<span id="L1538">VISC_REM_BT_WEIGHT_BUG = False  !   [Boolean] default = False</span>
<span id="L1539">                                ! If true, recover a bug in barotropic solver that uses an unnormalized weight</span>
<span id="L1540">                                ! function for vertical averages of baroclinic velocity and forcing. Default of</span>
<span id="L1541">                                ! this flag is set by VISC_REM_BUG.</span>
<span id="L1542">BAROTROPIC_TIDAL_SAL_BUG = False !   [Boolean] default = False</span>
<span id="L1543">                                ! If true, the tidal self-attraction and loading anomaly in the barotropic</span>
<span id="L1544">                                ! solver has the wrong sign, replicating a long-standing bug with a scalar</span>
<span id="L1545">                                ! self-attraction and loading term or the SAL term from a previous simulation.</span>
<span id="L1546">TIDAL_SAL_FLATHER = False       !   [Boolean] default = False</span>
<span id="L1547">                                ! If true, then apply adjustments to the external gravity wave speed used with</span>
<span id="L1548">                                ! the Flather OBC routine consistent with the barotropic solver. This applies to</span>
<span id="L1549">                                ! cases with  tidal forcing using the scalar self-attraction approximation. The</span>
<span id="L1550">                                ! default is currently False in order to retain previous answers but should be</span>
<span id="L1551">                                ! set to True for new experiments</span>
<span id="L1552">SADOURNY = True                 !   [Boolean] default = True</span>
<span id="L1553">                                ! If true, the Coriolis terms are discretized with the Sadourny (1975) energy</span>
<span id="L1554">                                ! conserving scheme, otherwise the Arakawa &amp; Hsu scheme is used.  If the</span>
<span id="L1555">                                ! internal deformation radius is not resolved, the Sadourny scheme should</span>
<span id="L1556">                                ! probably be used.</span>
<span id="L1557">BT_THICK_SCHEME = &quot;FROM_BT_CONT&quot; ! default = &quot;FROM_BT_CONT&quot;</span>
<span id="L1558">                                ! A string describing the scheme that is used to set the open face areas used</span>
<span id="L1559">                                ! for barotropic transport and the relative weights of the accelerations. Valid</span>
<span id="L1560">                                ! values are:</span>
<span id="L1561">                                !    ARITHMETIC - arithmetic mean layer thicknesses</span>
<span id="L1562">                                !    HARMONIC - harmonic mean layer thicknesses</span>
<span id="L1563">                                !    HYBRID (the default) - use arithmetic means for</span>
<span id="L1564">                                !       layers above the shallowest bottom, the harmonic</span>
<span id="L1565">                                !       mean for layers below, and a weighted average for</span>
<span id="L1566">                                !       layers that straddle that depth</span>
<span id="L1567">                                !    FROM_BT_CONT - use the average thicknesses kept</span>
<span id="L1568">                                !       in the h_u and h_v fields of the BT_cont_type</span>
<span id="L1569">BT_STRONG_DRAG = False          !   [Boolean] default = False</span>
<span id="L1570">                                ! If true, use a stronger estimate of the retarding effects of strong bottom</span>
<span id="L1571">                                ! drag, by making it implicit with the barotropic time-step instead of implicit</span>
<span id="L1572">                                ! with the baroclinic time-step and dividing by the number of barotropic steps.</span>
<span id="L1573">BT_LINEAR_WAVE_DRAG = False     !   [Boolean] default = False</span>
<span id="L1574">                                ! If true, apply a linear drag to the barotropic velocities, using rates set by</span>
<span id="L1575">                                ! lin_drag_u &amp; _v divided by the depth of the ocean.  This was introduced to</span>
<span id="L1576">                                ! facilitate tide modeling.</span>
<span id="L1577">BT_LINEAR_FREQ_DRAG = False     !   [Boolean] default = False</span>
<span id="L1578">                                ! If true, apply frequency-dependent drag to the tidal velocities. The streaming</span>
<span id="L1579">                                ! band-pass filter must be turned on.</span>
<span id="L1580">CLIP_BT_VELOCITY = False        !   [Boolean] default = False</span>
<span id="L1581">                                ! If true, limit any velocity components that exceed CFL_TRUNCATE.  This should</span>
<span id="L1582">                                ! only be used as a desperate debugging measure.</span>
<span id="L1583">MAXCFL_BT_CONT = 0.25           !   [nondim] default = 0.25</span>
<span id="L1584">                                ! The maximum permitted CFL number associated with the barotropic accelerations</span>
<span id="L1585">                                ! from the summed velocities times the time-derivatives of thicknesses.</span>
<span id="L1586">DT_BT_FILTER = -0.25            !   [sec or nondim] default = -0.25</span>
<span id="L1587">                                ! A time-scale over which the barotropic mode solutions are filtered, in seconds</span>
<span id="L1588">                                ! if positive, or as a fraction of DT if negative. When used this can never be</span>
<span id="L1589">                                ! taken to be longer than 2*dt.  Set this to 0 to apply no filtering.</span>
<span id="L1590">G_BT_EXTRA = 0.0                !   [nondim] default = 0.0</span>
<span id="L1591">                                ! A nondimensional factor by which gtot is enhanced.</span>
<span id="L1592">SSH_EXTRA = 10.0                !   [m] default = 10.0</span>
<span id="L1593">                                ! An estimate of how much higher SSH might get, for use in calculating the safe</span>
<span id="L1594">                                ! external wave speed. The default is the minimum of 10 m or 5% of</span>
<span id="L1595">                                ! MAXIMUM_DEPTH.</span>
<span id="L1596">LINEARIZED_BT_CORIOLIS = True   !   [Boolean] default = True</span>
<span id="L1597">                                ! If true use the bottom depth instead of the total water column thickness in</span>
<span id="L1598">                                ! the barotropic Coriolis term calculations.</span>
<span id="L1599">BEBT = 0.2                      !   [nondim] default = 0.1</span>
<span id="L1600">                                ! BEBT determines whether the barotropic time stepping uses the forward-backward</span>
<span id="L1601">                                ! time-stepping scheme or a backward Euler scheme. BEBT is valid in the range</span>
<span id="L1602">                                ! from 0 (for a forward-backward treatment of nonrotating gravity waves) to 1</span>
<span id="L1603">                                ! (for a backward Euler treatment). In practice, BEBT must be greater than about</span>
<span id="L1604">                                ! 0.05.</span>
<span id="L1605">DTBT = -0.95                    !   [s or nondim] default = -0.98</span>
<span id="L1606">                                ! The barotropic time step, in s. DTBT is only used with the split explicit time</span>
<span id="L1607">                                ! stepping. To set the time step automatically based the maximum stable value</span>
<span id="L1608">                                ! use 0, or a negative value gives the fraction of the stable value. Setting</span>
<span id="L1609">                                ! DTBT to 0 is the same as setting it to -0.98. The value of DTBT that will</span>
<span id="L1610">                                ! actually be used is an integer fraction of DT, rounding down.</span>
<span id="L1611">BT_USE_OLD_CORIOLIS_BRACKET_BUG = False !   [Boolean] default = False</span>
<span id="L1612">                                ! If True, use an order of operations that is not bitwise rotationally symmetric</span>
<span id="L1613">                                ! in the meridional Coriolis term of the barotropic solver.</span>
<span id="L1614">MASK_COASTAL_PRESSURE_FORCE = False !   [Boolean] default = False</span>
<span id="L1615">                                ! If true, use the land masks to zero out the diagnosed barotropic pressure</span>
<span id="L1616">                                ! gradient accelerations at coastal or land points.  This changes diagnostics</span>
<span id="L1617">                                ! and improves the reproducibility of certain debugging checksums, but it does</span>
<span id="L1618">                                ! not alter the solutions themselves.</span>
<span id="L1619"></span>
<span id="L1620">! === module MOM_mixed_layer_restrat ===</span>
<span id="L1621">MIXEDLAYER_RESTRAT = True       !   [Boolean] default = False</span>
<span id="L1622">                                ! If true, a density-gradient dependent re-stratifying flow is imposed in the</span>
<span id="L1623">                                ! mixed layer. Can be used in ALE mode without restriction but in layer mode can</span>
<span id="L1624">                                ! only be used if BULKMIXEDLAYER is true.</span>
<span id="L1625">MLE%</span>
<span id="L1626">%MLE</span>
<span id="L1627">FOX_KEMPER_ML_RESTRAT_COEF = 20.0 !   [nondim] default = 0.0</span>
<span id="L1628">                                ! A nondimensional coefficient that is proportional to the ratio of the</span>
<span id="L1629">                                ! deformation radius to the dominant lengthscale of the submesoscale mixed layer</span>
<span id="L1630">                                ! instabilities, times the minimum of the ratio of the mesoscale eddy kinetic</span>
<span id="L1631">                                ! energy to the large-scale geostrophic kinetic energy or 1 plus the square of</span>
<span id="L1632">                                ! the grid spacing over the deformation radius, as detailed by Fox-Kemper et al.</span>
<span id="L1633">                                ! (2011)</span>
<span id="L1634">USE_STANLEY_ML = False          !   [Boolean] default = False</span>
<span id="L1635">                                ! If true, turn on Stanley SGS T variance parameterization in ML restrat code.</span>
<span id="L1636">KV_RESTRAT = 0.0                !   [m2 s-1] default = 0.0</span>
<span id="L1637">                                ! A small viscosity that sets a floor on the momentum mixing rate during</span>
<span id="L1638">                                ! restratification.  If this is positive, it will prevent some possible</span>
<span id="L1639">                                ! divisions by zero even if ustar, RESTRAT_USTAR_MIN, and f are all 0.</span>
<span id="L1640">RESTRAT_USTAR_MIN = 1.45842E-18 !   [m s-1] default = 1.45842E-18</span>
<span id="L1641">                                ! The minimum value of ustar that will be used by the mixed layer</span>
<span id="L1642">                                ! restratification module.  This can be tiny, but if this is greater than 0, it</span>
<span id="L1643">                                ! will prevent divisions by zero when f and KV_RESTRAT are zero.</span>
<span id="L1644"></span>
<span id="L1645">! === module MOM_diagnostics ===</span>
<span id="L1646">DIAG_EBT_MONO_N2_COLUMN_FRACTION = 0.0 !   [nondim] default = 0.0</span>
<span id="L1647">                                ! The lower fraction of water column over which N2 is limited as monotonic for</span>
<span id="L1648">                                ! the purposes of calculating the equivalent barotropic wave speed.</span>
<span id="L1649">DIAG_EBT_MONO_N2_DEPTH = -1.0   !   [m] default = -1.0</span>
<span id="L1650">                                ! The depth below which N2 is limited as monotonic for the purposes of</span>
<span id="L1651">                                ! calculating the equivalent barotropic wave speed.</span>
<span id="L1652">INTWAVE_REMAPPING_USE_OM4_SUBCELLS = True !   [Boolean] default = True</span>
<span id="L1653">                                ! If true, use the OM4 remapping-via-subcells algorithm for calculating EBT</span>
<span id="L1654">                                ! structure. See REMAPPING_USE_OM4_SUBCELLS for details. We recommend setting</span>
<span id="L1655">                                ! this option to false.</span>
<span id="L1656"></span>
<span id="L1657">! === module MOM_diabatic_driver ===</span>
<span id="L1658">! The following parameters are used for diabatic processes.</span>
<span id="L1659">USE_LEGACY_DIABATIC_DRIVER = True !   [Boolean] default = True</span>
<span id="L1660">                                ! If true, use a legacy version of the diabatic subroutine. This is temporary</span>
<span id="L1661">                                ! and is needed to avoid change in answers.</span>
<span id="L1662">ENERGETICS_SFC_PBL = False      !   [Boolean] default = False</span>
<span id="L1663">                                ! If true, use an implied energetics planetary boundary layer scheme to</span>
<span id="L1664">                                ! determine the diffusivity and viscosity in the surface boundary layer.</span>
<span id="L1665">EPBL_IS_ADDITIVE = True         !   [Boolean] default = True</span>
<span id="L1666">                                ! If true, the diffusivity from ePBL is added to all other diffusivities.</span>
<span id="L1667">                                ! Otherwise, the larger of kappa-shear and ePBL diffusivities are used.</span>
<span id="L1668">ML_MIX_FIRST = 0.0              !   [nondim] default = 0.0</span>
<span id="L1669">                                ! The fraction of the mixed layer mixing that is applied before interior</span>
<span id="L1670">                                ! diapycnal mixing.  0 by default.</span>
<span id="L1671">INTERNAL_TIDES = False          !   [Boolean] default = False</span>
<span id="L1672">                                ! If true, use the code that advances a separate set of equations for the</span>
<span id="L1673">                                ! internal tide energy density.</span>
<span id="L1674">MASSLESS_MATCH_TARGETS = True   !   [Boolean] default = True</span>
<span id="L1675">                                ! If true, the temperature and salinity of massless layers are kept consistent</span>
<span id="L1676">                                ! with their target densities. Otherwise the properties of massless layers</span>
<span id="L1677">                                ! evolve diffusively to match massive neighboring layers.</span>
<span id="L1678">AGGREGATE_FW_FORCING = True     !   [Boolean] default = True</span>
<span id="L1679">                                ! If true, the net incoming and outgoing fresh water fluxes are combined and</span>
<span id="L1680">                                ! applied as either incoming or outgoing depending on the sign of the net. If</span>
<span id="L1681">                                ! false, the net incoming fresh water flux is added to the model and thereafter</span>
<span id="L1682">                                ! the net outgoing is removed from the topmost non-vanished layers of the</span>
<span id="L1683">                                ! updated state.</span>
<span id="L1684">MIX_BOUNDARY_TRACERS = True     !   [Boolean] default = True</span>
<span id="L1685">                                ! If true, mix the passive tracers in massless layers at the bottom into the</span>
<span id="L1686">                                ! interior as though a diffusivity of KD_MIN_TR were operating.</span>
<span id="L1687">KD_MIN_TR = 2.0E-06             !   [m2 s-1] default = 2.0E-06</span>
<span id="L1688">                                ! A minimal diffusivity that should always be applied to tracers, especially in</span>
<span id="L1689">                                ! massless layers near the bottom. The default is 0.1*KD.</span>
<span id="L1690">KD_BBL_TR = 0.0                 !   [m2 s-1] default = 0.0</span>
<span id="L1691">                                ! A bottom boundary layer tracer diffusivity that will allow for explicitly</span>
<span id="L1692">                                ! specified bottom fluxes. The entrainment at the bottom is at least</span>
<span id="L1693">                                ! sqrt(Kd_BBL_tr*dt) over the same distance.</span>
<span id="L1694">TRACER_TRIDIAG = False          !   [Boolean] default = False</span>
<span id="L1695">                                ! If true, use the passive tracer tridiagonal solver for T and S</span>
<span id="L1696">MINIMUM_FORCING_DEPTH = 0.001   !   [m] default = 0.001</span>
<span id="L1697">                                ! The smallest depth over which forcing can be applied. This only takes effect</span>
<span id="L1698">                                ! when near-surface layers become thin relative to this scale, in which case the</span>
<span id="L1699">                                ! forcing tendencies scaled down by distributing the forcing over this depth</span>
<span id="L1700">                                ! scale.</span>
<span id="L1701">EVAP_CFL_LIMIT = 0.8            !   [nondim] default = 0.8</span>
<span id="L1702">                                ! The largest fraction of a layer than can be lost to forcing (e.g. evaporation,</span>
<span id="L1703">                                ! sea-ice formation) in one time-step. The unused mass loss is passed down</span>
<span id="L1704">                                ! through the column.</span>
<span id="L1705">MLD_EN_VALS = 25.0, 2500.0, 2.5E+05 !   [J/m2] default = 25.0, 2500.0, 2.5E+05</span>
<span id="L1706">                                ! The energy values used to compute MLDs.  If not set (or all set to 0.), the</span>
<span id="L1707">                                ! default will overwrite to 25., 2500., 250000.</span>
<span id="L1708">BMLD_EN_VALS = 25.0, 2500.0, 2.5E+05 !   [J/m2] default = 25.0, 2500.0, 2.5E+05</span>
<span id="L1709">                                ! The energy values used to compute Bottom MLDs.  If not set (or all set to 0.),</span>
<span id="L1710">                                ! the default will overwrite to 25., 2500., 250000.</span>
<span id="L1711">DIAG_MLD_DENSITY_DIFF = 0.1     !   [kg/m3] default = 0.1</span>
<span id="L1712">                                ! The density difference used to determine a diagnostic mixed layer depth,</span>
<span id="L1713">                                ! MLD_user, following the definition of Levitus 1982. The MLD is the depth at</span>
<span id="L1714">                                ! which the density is larger than the surface density by the specified amount.</span>
<span id="L1715">DIAG_DEPTH_SUBML_N2 = 50.0      !   [m] default = 50.0</span>
<span id="L1716">                                ! The distance over which to calculate a diagnostic of the stratification at the</span>
<span id="L1717">                                ! base of the mixed layer.</span>
<span id="L1718"></span>
<span id="L1719">! === module MOM_CVMix_KPP ===</span>
<span id="L1720">! This is the MOM wrapper to CVMix:KPP</span>
<span id="L1721">! See http://cvmix.github.io/</span>
<span id="L1722">USE_KPP = False                 !   [Boolean] default = False</span>
<span id="L1723">                                ! If true, turns on the [CVMix] KPP scheme of Large et al., 1994, to calculate</span>
<span id="L1724">                                ! diffusivities and non-local transport in the OBL.</span>
<span id="L1725"></span>
<span id="L1726">! === module MOM_CVMix_conv ===</span>
<span id="L1727">! Parameterization of enhanced mixing due to convection via CVMix</span>
<span id="L1728">USE_CVMix_CONVECTION = False    !   [Boolean] default = False</span>
<span id="L1729">                                ! If true, turns on the enhanced mixing due to convection via CVMix. This scheme</span>
<span id="L1730">                                ! increases diapycnal diffs./viscs. at statically unstable interfaces. Relevant</span>
<span id="L1731">                                ! parameters are contained in the CVMix_CONVECTION% parameter block.</span>
<span id="L1732"></span>
<span id="L1733">! === module MOM_entrain_diffusive ===</span>
<span id="L1734">MAX_ENT_IT = 20                 ! default = 5</span>
<span id="L1735">                                ! The maximum number of iterations that may be used to calculate the interior</span>
<span id="L1736">                                ! diapycnal entrainment.</span>
<span id="L1737">TOLERANCE_ENT = 1.0E-05         !   [m] default = 2.683281572999748E-05</span>
<span id="L1738">                                ! The tolerance with which to solve for entrainment values.</span>
<span id="L1739">ENTRAIN_DIFFUSIVE_MAX_ENT = 1.0E+04 !   [m] default = 1.0E+04</span>
<span id="L1740">                                ! A large ceiling on the maximum permitted amount of entrainment across each</span>
<span id="L1741">                                ! interface between the mixed and buffer layers within a timestep.</span>
<span id="L1742"></span>
<span id="L1743">! === module MOM_geothermal ===</span>
<span id="L1744">GEOTHERMAL_SCALE = 0.001        !   [W m-2 or various] default = 0.0</span>
<span id="L1745">                                ! The constant geothermal heat flux, a rescaling factor for the heat flux read</span>
<span id="L1746">                                ! from GEOTHERMAL_FILE, or 0 to disable the geothermal heating.</span>
<span id="L1747">GEOTHERMAL_FILE = &quot;geothermal_heating_cm2g.nc&quot; ! default = &quot;&quot;</span>
<span id="L1748">                                ! The file from which the geothermal heating is to be read, or blank to use a</span>
<span id="L1749">                                ! constant heating rate.</span>
<span id="L1750">GEOTHERMAL_THICKNESS = 0.1      !   [m] default = 0.1</span>
<span id="L1751">                                ! The thickness over which to apply geothermal heating.</span>
<span id="L1752">GEOTHERMAL_DRHO_DT_INPLACE = -0.01 !   [kg m-3 K-1] default = -0.01</span>
<span id="L1753">                                ! The value of drho_dT above which geothermal heating simply heats water in</span>
<span id="L1754">                                ! place instead of moving it between isopycnal layers.  This must be negative.</span>
<span id="L1755">GEOTHERMAL_VARNAME = &quot;geo_heat&quot; ! default = &quot;geo_heat&quot;</span>
<span id="L1756">                                ! The name of the geothermal heating variable in GEOTHERMAL_FILE.</span>
<span id="L1757"></span>
<span id="L1758">! === module MOM_set_diffusivity ===</span>
<span id="L1759">FLUX_RI_MAX = 0.2               !   [nondim] default = 0.2</span>
<span id="L1760">                                ! The flux Richardson number where the stratification is large enough that N2 &gt;</span>
<span id="L1761">                                ! omega2.  The full expression for the Flux Richardson number is usually</span>
<span id="L1762">                                ! FLUX_RI_MAX*N2/(N2+OMEGA2).</span>
<span id="L1763">SET_DIFF_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1764">                                ! The vintage of the order of arithmetic and expressions in the set diffusivity</span>
<span id="L1765">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L1766">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L1767">                                ! Values above 20250301 also use less confusing expressions to set the</span>
<span id="L1768">                                ! bottom-drag generated diffusivity when USE_LOTW_BBL_DIFFUSIVITY is false.</span>
<span id="L1769"></span>
<span id="L1770">! === module MOM_tidal_mixing ===</span>
<span id="L1771">! Vertical Tidal Mixing Parameterization</span>
<span id="L1772">USE_CVMix_TIDAL = False         !   [Boolean] default = False</span>
<span id="L1773">                                ! If true, turns on tidal mixing via CVMix</span>
<span id="L1774">INT_TIDE_DISSIPATION = True     !   [Boolean] default = False</span>
<span id="L1775">                                ! If true, use an internal tidal dissipation scheme to drive diapycnal mixing,</span>
<span id="L1776">                                ! along the lines of St. Laurent et al. (2002) and Simmons et al. (2004).</span>
<span id="L1777">TIDAL_MIXING_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1778">                                ! The vintage of the order of arithmetic and expressions in the tidal mixing</span>
<span id="L1779">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L1780">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L1781">INT_TIDE_PROFILE = &quot;STLAURENT_02&quot; ! default = &quot;STLAURENT_02&quot;</span>
<span id="L1782">                                ! INT_TIDE_PROFILE selects the vertical profile of energy dissipation with</span>
<span id="L1783">                                ! INT_TIDE_DISSIPATION. Valid values are:</span>
<span id="L1784">                                !    STLAURENT_02 - Use the St. Laurent et al exponential</span>
<span id="L1785">                                !                   decay profile.</span>
<span id="L1786">                                !    POLZIN_09 - Use the Polzin WKB-stretched algebraic</span>
<span id="L1787">                                !                   decay profile.</span>
<span id="L1788">LEE_WAVE_DISSIPATION = False    !   [Boolean] default = False</span>
<span id="L1789">                                ! If true, use an lee wave driven dissipation scheme to drive diapycnal mixing,</span>
<span id="L1790">                                ! along the lines of Nikurashin (2010) and using the St. Laurent et al. (2002)</span>
<span id="L1791">                                ! and Simmons et al. (2004) vertical profile</span>
<span id="L1792">INT_TIDE_LOWMODE_DISSIPATION = False !   [Boolean] default = False</span>
<span id="L1793">                                ! If true, consider mixing due to breaking low modes that have been remotely</span>
<span id="L1794">                                ! generated; as with itidal drag on the barotropic tide, use an internal tidal</span>
<span id="L1795">                                ! dissipation scheme to drive diapycnal mixing, along the lines of St. Laurent</span>
<span id="L1796">                                ! et al. (2002) and Simmons et al. (2004).</span>
<span id="L1797">INT_TIDE_DECAY_SCALE = 300.0    !   [m] default = 500.0</span>
<span id="L1798">                                ! The decay scale away from the bottom for tidal TKE with the new coding when</span>
<span id="L1799">                                ! INT_TIDE_DISSIPATION is used.</span>
<span id="L1800">MU_ITIDES = 0.2                 !   [nondim] default = 0.2</span>
<span id="L1801">                                ! A dimensionless turbulent mixing efficiency used with INT_TIDE_DISSIPATION,</span>
<span id="L1802">                                ! often 0.2.</span>
<span id="L1803">GAMMA_ITIDES = 0.3333           !   [nondim] default = 0.3333</span>
<span id="L1804">                                ! The fraction of the internal tidal energy that is dissipated locally with</span>
<span id="L1805">                                ! INT_TIDE_DISSIPATION. THIS NAME COULD BE BETTER.</span>
<span id="L1806">MIN_ZBOT_ITIDES = 0.0           !   [m] default = 0.0</span>
<span id="L1807">                                ! Turn off internal tidal dissipation when the total ocean depth is less than</span>
<span id="L1808">                                ! this value.</span>
<span id="L1809">KAPPA_ITIDES = 6.28319E-04      !   [m-1] default = 6.283185307179586E-04</span>
<span id="L1810">                                ! A topographic wavenumber used with INT_TIDE_DISSIPATION. The default is 2pi/10</span>
<span id="L1811">                                ! km, as in St.Laurent et al. 2002.</span>
<span id="L1812">UTIDE = 0.0                     !   [m s-1] default = 0.0</span>
<span id="L1813">                                ! The constant tidal amplitude used with INT_TIDE_DISSIPATION.</span>
<span id="L1814">KAPPA_H2_FACTOR = 0.75          !   [nondim] default = 1.0</span>
<span id="L1815">                                ! A scaling factor for the roughness amplitude with INT_TIDE_DISSIPATION.</span>
<span id="L1816">TKE_ITIDE_MAX = 0.1             !   [W m-2] default = 1000.0</span>
<span id="L1817">                                ! The maximum internal tide energy source available to mix above the bottom</span>
<span id="L1818">                                ! boundary layer with INT_TIDE_DISSIPATION.</span>
<span id="L1819">READ_TIDEAMP = True             !   [Boolean] default = False</span>
<span id="L1820">                                ! If true, read a file (given by TIDEAMP_FILE) containing the tidal amplitude</span>
<span id="L1821">                                ! with INT_TIDE_DISSIPATION.</span>
<span id="L1822">TIDEAMP_FILE = &quot;tideamp.nc&quot;     ! default = &quot;tideamp.nc&quot;</span>
<span id="L1823">                                ! The path to the file containing the spatially varying tidal amplitudes with</span>
<span id="L1824">                                ! INT_TIDE_DISSIPATION.</span>
<span id="L1825">TIDEAMP_VARNAME = &quot;tideamp&quot;     ! default = &quot;tideamp&quot;</span>
<span id="L1826">                                ! The name of the tidal amplitude variable in the input file.</span>
<span id="L1827">H2_FILE = &quot;sgs_h2.nc&quot;           !</span>
<span id="L1828">                                ! The path to the file containing the sub-grid-scale topographic roughness</span>
<span id="L1829">                                ! amplitude with INT_TIDE_DISSIPATION.</span>
<span id="L1830">ROUGHNESS_VARNAME = &quot;h2&quot;        ! default = &quot;h2&quot;</span>
<span id="L1831">                                ! The name in the input file of the squared sub-grid-scale topographic roughness</span>
<span id="L1832">                                ! amplitude variable.</span>
<span id="L1833">FRACTIONAL_ROUGHNESS_MAX = 0.1  !   [nondim] default = 0.1</span>
<span id="L1834">                                ! The maximum topographic roughness amplitude as a fraction of the mean depth,</span>
<span id="L1835">                                ! or a negative value for no limitations on roughness.</span>
<span id="L1836">ML_RADIATION = True             !   [Boolean] default = False</span>
<span id="L1837">                                ! If true, allow a fraction of TKE available from wind work to penetrate below</span>
<span id="L1838">                                ! the base of the mixed layer with a vertical decay scale determined by the</span>
<span id="L1839">                                ! minimum of: (1) The depth of the mixed layer, (2) an Ekman length scale.</span>
<span id="L1840">ML_RAD_EFOLD_COEFF = 0.2        !   [nondim] default = 0.2</span>
<span id="L1841">                                ! A coefficient that is used to scale the penetration depth for turbulence below</span>
<span id="L1842">                                ! the base of the mixed layer. This is only used if ML_RADIATION is true.</span>
<span id="L1843">ML_RAD_BUG = False              !   [Boolean] default = False</span>
<span id="L1844">                                ! If true use code with a bug that reduces the energy available in the</span>
<span id="L1845">                                ! transition layer by a factor of the inverse of the energy deposition</span>
<span id="L1846">                                ! lenthscale (in m).</span>
<span id="L1847">ML_RAD_KD_MAX = 0.001           !   [m2 s-1] default = 0.001</span>
<span id="L1848">                                ! The maximum diapycnal diffusivity due to turbulence radiated from the base of</span>
<span id="L1849">                                ! the mixed layer. This is only used if ML_RADIATION is true.</span>
<span id="L1850">ML_RAD_COEFF = 0.1              !   [nondim] default = 0.2</span>
<span id="L1851">                                ! The coefficient which scales MSTAR*USTAR^3 to obtain the energy available for</span>
<span id="L1852">                                ! mixing below the base of the mixed layer. This is only used if ML_RADIATION is</span>
<span id="L1853">                                ! true.</span>
<span id="L1854">ML_RAD_APPLY_TKE_DECAY = True   !   [Boolean] default = True</span>
<span id="L1855">                                ! If true, apply the same exponential decay to ML_rad as is applied to the other</span>
<span id="L1856">                                ! surface sources of TKE in the mixed layer code. This is only used if</span>
<span id="L1857">                                ! ML_RADIATION is true.</span>
<span id="L1858">MSTAR = 0.3                     !   [nondim] default = 1.2</span>
<span id="L1859">                                ! The ratio of the friction velocity cubed to the TKE input to the mixed layer.</span>
<span id="L1860">TKE_DECAY = 10.0                !   [nondim] default = 2.5</span>
<span id="L1861">                                ! The ratio of the natural Ekman depth to the TKE decay scale.</span>
<span id="L1862">BBL_EFFIC = 0.2                 !   [nondim] default = 0.2</span>
<span id="L1863">                                ! The efficiency with which the energy extracted by bottom drag drives BBL</span>
<span id="L1864">                                ! diffusion.  This is only used if BOTTOMDRAGLAW is true.</span>
<span id="L1865">BBL_MIXING_MAX_DECAY = 200.0    !   [m] default = 200.0</span>
<span id="L1866">                                ! The maximum decay scale for the BBL diffusion, or 0 to allow the mixing to</span>
<span id="L1867">                                ! penetrate as far as stratification and rotation permit.  The default for now</span>
<span id="L1868">                                ! is 200 m. This is only used if BOTTOMDRAGLAW is true.</span>
<span id="L1869">BBL_MIXING_AS_MAX = False       !   [Boolean] default = True</span>
<span id="L1870">                                ! If true, take the maximum of the diffusivity from the BBL mixing and the other</span>
<span id="L1871">                                ! diffusivities. Otherwise, diffusivity from the BBL_mixing is simply added.</span>
<span id="L1872">USE_LOTW_BBL_DIFFUSIVITY = False !   [Boolean] default = False</span>
<span id="L1873">                                ! If true, uses a simple, imprecise but non-coordinate dependent, model of BBL</span>
<span id="L1874">                                ! mixing diffusivity based on Law of the Wall. Otherwise, uses the original BBL</span>
<span id="L1875">                                ! scheme.</span>
<span id="L1876">DRAG_DIFFUSIVITY_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1877">                                ! The vintage of the order of arithmetic in the drag diffusivity calculations.</span>
<span id="L1878">                                ! Values above 20250301 use less confusing expressions to set the bottom-drag</span>
<span id="L1879">                                ! generated diffusivity when USE_LOTW_BBL_DIFFUSIVITY is false.</span>
<span id="L1880">DZ_BBL_AVG_MIN = 0.0            !   [m] default = 0.0</span>
<span id="L1881">                                ! A minimal distance over which to average to determine the average bottom</span>
<span id="L1882">                                ! boundary layer density.</span>
<span id="L1883">SIMPLE_TKE_TO_KD = False        !   [Boolean] default = False</span>
<span id="L1884">                                ! If true, uses a simple estimate of Kd/TKE that will work for arbitrary</span>
<span id="L1885">                                ! vertical coordinates. If false, calculates Kd/TKE and bounds based on exact</span>
<span id="L1886">                                ! energetics for an isopycnal layer-formulation.</span>
<span id="L1887"></span>
<span id="L1888">! === module MOM_bkgnd_mixing ===</span>
<span id="L1889">! Adding static vertical background mixing coefficients</span>
<span id="L1890">KD = 2.0E-05                    !   [m2 s-1] default = 0.0</span>
<span id="L1891">                                ! The background diapycnal diffusivity of density in the interior. Zero or the</span>
<span id="L1892">                                ! molecular value, ~1e-7 m2 s-1, may be used.</span>
<span id="L1893">KD_MIN = 2.0E-06                !   [m2 s-1] default = 2.0E-07</span>
<span id="L1894">                                ! The minimum diapycnal diffusivity.</span>
<span id="L1895">BRYAN_LEWIS_DIFFUSIVITY = False !   [Boolean] default = False</span>
<span id="L1896">                                ! If true, use a Bryan &amp; Lewis (JGR 1979) like tanh profile of background</span>
<span id="L1897">                                ! diapycnal diffusivity with depth. This is done via CVMix.</span>
<span id="L1898">HORIZ_VARYING_BACKGROUND = False !   [Boolean] default = False</span>
<span id="L1899">                                ! If true, apply vertically uniform, latitude-dependent background diffusivity,</span>
<span id="L1900">                                ! as described in Danabasoglu et al., 2012</span>
<span id="L1901">PRANDTL_BKGND = 1.0             !   [nondim] default = 1.0</span>
<span id="L1902">                                ! Turbulent Prandtl number used to convert vertical background diffusivities</span>
<span id="L1903">                                ! into viscosities.</span>
<span id="L1904">HENYEY_IGW_BACKGROUND = True    !   [Boolean] default = False</span>
<span id="L1905">                                ! If true, use a latitude-dependent scaling for the near surface background</span>
<span id="L1906">                                ! diffusivity, as described in Harrison &amp; Hallberg, JPO 2008.</span>
<span id="L1907">HENYEY_N0_2OMEGA = 20.0         !   [nondim] default = 20.0</span>
<span id="L1908">                                ! The ratio of the typical Buoyancy frequency to twice the Earth&#x27;s rotation</span>
<span id="L1909">                                ! period, used with the Henyey scaling from the mixing.</span>
<span id="L1910">HENYEY_MAX_LAT = 95.0           !   [degN] default = 95.0</span>
<span id="L1911">                                ! A latitude poleward of which the Henyey profile is returned to the minimum</span>
<span id="L1912">                                ! diffusivity</span>
<span id="L1913">KD_TANH_LAT_FN = False          !   [Boolean] default = False</span>
<span id="L1914">                                ! If true, use a tanh dependence of Kd_sfc on latitude, like CM2.1/CM2M.  There</span>
<span id="L1915">                                ! is no physical justification for this form, and it can not be used with</span>
<span id="L1916">                                ! HENYEY_IGW_BACKGROUND.</span>
<span id="L1917">KD_MAX = -1.0                   !   [m2 s-1] default = -1.0</span>
<span id="L1918">                                ! The maximum permitted increment for the diapycnal diffusivity from TKE-based</span>
<span id="L1919">                                ! parameterizations, or a negative value for no limit.</span>
<span id="L1920">KD_ADD = 0.0                    !   [m2 s-1] default = 0.0</span>
<span id="L1921">                                ! A uniform diapycnal diffusivity that is added everywhere without any filtering</span>
<span id="L1922">                                ! or scaling.</span>
<span id="L1923">USER_CHANGE_DIFFUSIVITY = False !   [Boolean] default = False</span>
<span id="L1924">                                ! If true, call user-defined code to change the diffusivity.</span>
<span id="L1925">DISSIPATION_MIN = 0.0           !   [W m-3] default = 0.0</span>
<span id="L1926">                                ! The minimum dissipation by which to determine a lower bound of Kd (a floor).</span>
<span id="L1927">DISSIPATION_N0 = 1.0E-07        !   [W m-3] default = 0.0</span>
<span id="L1928">                                ! The intercept when N=0 of the N-dependent expression used to set a minimum</span>
<span id="L1929">                                ! dissipation by which to determine a lower bound of Kd (a floor): A in eps_min</span>
<span id="L1930">                                ! = A + B*N.</span>
<span id="L1931">DISSIPATION_N1 = 6.0E-04        !   [J m-3] default = 0.0</span>
<span id="L1932">                                ! The coefficient multiplying N, following Gargett, used to set a minimum</span>
<span id="L1933">                                ! dissipation by which to determine a lower bound of Kd (a floor): B in eps_min</span>
<span id="L1934">                                ! = A + B*N</span>
<span id="L1935">DISSIPATION_KD_MIN = 0.0        !   [m2 s-1] default = 0.0</span>
<span id="L1936">                                ! The minimum vertical diffusivity applied as a floor.</span>
<span id="L1937">DOUBLE_DIFFUSION = False        !   [Boolean] default = False</span>
<span id="L1938">                                ! If true, increase diffusivites for temperature or salinity based on the</span>
<span id="L1939">                                ! double-diffusive parameterization described in Large et al. (1994).</span>
<span id="L1940"></span>
<span id="L1941">! === module MOM_kappa_shear ===</span>
<span id="L1942">! Parameterization of shear-driven turbulence following Jackson, Hallberg and Legg, JPO 2008</span>
<span id="L1943">USE_JACKSON_PARAM = True        !   [Boolean] default = False</span>
<span id="L1944">                                ! If true, use the Jackson-Hallberg-Legg (JPO 2008) shear mixing</span>
<span id="L1945">                                ! parameterization.</span>
<span id="L1946">VERTEX_SHEAR = False            !   [Boolean] default = False</span>
<span id="L1947">                                ! If true, do the calculations of the shear-driven mixing at the cell vertices</span>
<span id="L1948">                                ! (i.e., the vorticity points).</span>
<span id="L1949">VERTEX_SHEAR_THICKNESS_MEAN = False !   [Boolean] default = False</span>
<span id="L1950">                                ! If true, apply thickness weighting to horizontal averagings of diffusivity to</span>
<span id="L1951">                                ! tracer points in the kappa shear solver.</span>
<span id="L1952">RINO_CRIT = 0.25                !   [nondim] default = 0.25</span>
<span id="L1953">                                ! The critical Richardson number for shear mixing.</span>
<span id="L1954">SHEARMIX_RATE = 0.089           !   [nondim] default = 0.089</span>
<span id="L1955">                                ! A nondimensional rate scale for shear-driven entrainment. Jackson et al find</span>
<span id="L1956">                                ! values in the range of 0.085-0.089.</span>
<span id="L1957">MAX_RINO_IT = 25                !   [nondim] default = 50</span>
<span id="L1958">                                ! The maximum number of iterations that may be used to estimate the Richardson</span>
<span id="L1959">                                ! number driven mixing.</span>
<span id="L1960">KD_KAPPA_SHEAR_0 = 2.0E-05      !   [m2 s-1] default = 2.0E-05</span>
<span id="L1961">                                ! The background diffusivity that is used to smooth the density and shear</span>
<span id="L1962">                                ! profiles before solving for the diffusivities.  The default is the greater of</span>
<span id="L1963">                                ! KD and 1e-7 m2 s-1.</span>
<span id="L1964">KD_SEED_KAPPA_SHEAR = 1.0       !   [m2 s-1] default = 1.0</span>
<span id="L1965">                                ! A moderately large seed value of diapycnal diffusivity that is used as a</span>
<span id="L1966">                                ! starting turbulent diffusivity in the iterations to find an energetically</span>
<span id="L1967">                                ! constrained solution for the shear-driven diffusivity.</span>
<span id="L1968">KD_TRUNC_KAPPA_SHEAR = 2.0E-07  !   [m2 s-1] default = 2.0E-07</span>
<span id="L1969">                                ! The value of shear-driven diffusivity that is considered negligible and is</span>
<span id="L1970">                                ! rounded down to 0. The default is 1% of KD_KAPPA_SHEAR_0.</span>
<span id="L1971">FRI_CURVATURE = -0.97           !   [nondim] default = -0.97</span>
<span id="L1972">                                ! The nondimensional curvature of the function of the Richardson number in the</span>
<span id="L1973">                                ! kappa source term in the Jackson et al. scheme.</span>
<span id="L1974">TKE_N_DECAY_CONST = 0.24        !   [nondim] default = 0.24</span>
<span id="L1975">                                ! The coefficient for the decay of TKE due to stratification (i.e. proportional</span>
<span id="L1976">                                ! to N*tke). The values found by Jackson et al. are 0.24-0.28.</span>
<span id="L1977">TKE_SHEAR_DECAY_CONST = 0.14    !   [nondim] default = 0.14</span>
<span id="L1978">                                ! The coefficient for the decay of TKE due to shear (i.e. proportional to</span>
<span id="L1979">                                ! |S|*tke). The values found by Jackson et al. are 0.14-0.12.</span>
<span id="L1980">KAPPA_BUOY_SCALE_COEF = 0.82    !   [nondim] default = 0.82</span>
<span id="L1981">                                ! The coefficient for the buoyancy length scale in the kappa equation.  The</span>
<span id="L1982">                                ! values found by Jackson et al. are in the range of 0.81-0.86.</span>
<span id="L1983">KAPPA_N_OVER_S_SCALE_COEF2 = 0.0 !   [nondim] default = 0.0</span>
<span id="L1984">                                ! The square of the ratio of the coefficients of the buoyancy and shear scales</span>
<span id="L1985">                                ! in the diffusivity equation, Set this to 0 (the default) to eliminate the</span>
<span id="L1986">                                ! shear scale. This is only used if USE_JACKSON_PARAM is true.</span>
<span id="L1987">LZ_RESCALE = 1.0                !   [nondim] default = 1.0</span>
<span id="L1988">                                ! A coefficient to rescale the distance to the nearest solid boundary. This</span>
<span id="L1989">                                ! adjustment is to account for regions where 3 dimensional turbulence prevents</span>
<span id="L1990">                                ! the growth of shear instabilies [nondim].</span>
<span id="L1991">KAPPA_SHEAR_TOL_ERR = 0.1       !   [nondim] default = 0.1</span>
<span id="L1992">                                ! The fractional error in kappa that is tolerated. Iteration stops when changes</span>
<span id="L1993">                                ! between subsequent iterations are smaller than this everywhere in a column.</span>
<span id="L1994">                                ! The peak diffusivities usually converge most rapidly, and have much smaller</span>
<span id="L1995">                                ! errors than this.</span>
<span id="L1996">TKE_BACKGROUND = 0.0            !   [m2 s-2] default = 0.0</span>
<span id="L1997">                                ! A background level of TKE used in the first iteration of the kappa equation.</span>
<span id="L1998">                                ! TKE_BACKGROUND could be 0.</span>
<span id="L1999">KAPPA_SHEAR_ELIM_MASSLESS = True !   [Boolean] default = True</span>
<span id="L2000">                                ! If true, massless layers are merged with neighboring massive layers in this</span>
<span id="L2001">                                ! calculation.  The default is true and I can think of no good reason why it</span>
<span id="L2002">                                ! should be false. This is only used if USE_JACKSON_PARAM is true.</span>
<span id="L2003">MAX_KAPPA_SHEAR_IT = 13         ! default = 13</span>
<span id="L2004">                                ! The maximum number of iterations that may be used to estimate the</span>
<span id="L2005">                                ! time-averaged diffusivity.</span>
<span id="L2006">PRANDTL_TURB = 1.0              !   [nondim] default = 1.0</span>
<span id="L2007">                                ! The turbulent Prandtl number applied to shear instability.</span>
<span id="L2008">KAPPA_SHEAR_MAX_KAP_SRC_CHG = 10.0 !   [nondim] default = 10.0</span>
<span id="L2009">                                ! The maximum permitted increase in the kappa source within an iteration</span>
<span id="L2010">                                ! relative to the local source; this must be greater than 1.  The lower limit</span>
<span id="L2011">                                ! for the permitted fractional decrease is (1 - 0.5/kappa_src_max_chg).  These</span>
<span id="L2012">                                ! limits could perhaps be made dynamic with an improved iterative solver.</span>
<span id="L2013">KAPPA_SHEAR_ITER_BUG = False    !   [Boolean] default = False</span>
<span id="L2014">                                ! If true, use an older, dimensionally inconsistent estimate of the derivative</span>
<span id="L2015">                                ! of diffusivity with energy in the Newton&#x27;s method iteration.  The bug causes</span>
<span id="L2016">                                ! undercorrections when dz &gt; 1 m.</span>
<span id="L2017">KAPPA_SHEAR_ALL_LAYER_TKE_BUG = False !   [Boolean] default = False</span>
<span id="L2018">                                ! If true, report back the latest estimate of TKE instead of the time average</span>
<span id="L2019">                                ! TKE when there is mass in all layers.  Otherwise always report the time</span>
<span id="L2020">                                ! averaged TKE, as is currently done when there are some massless layers.</span>
<span id="L2021">USE_RESTRICTIVE_TOLERANCE_CHECK = False !   [Boolean] default = False</span>
<span id="L2022">                                ! If true, uses the more restrictive tolerance check to determine if a timestep</span>
<span id="L2023">                                ! is acceptable for the KS_it outer iteration loop.  False uses the original</span>
<span id="L2024">                                ! less restrictive check.</span>
<span id="L2025">KAPPA_SHEAR_MERGE_ML = True     !   [Boolean] default = True</span>
<span id="L2026">                                ! If true, combine the mixed layers together before solving the kappa-shear</span>
<span id="L2027">                                ! equations.</span>
<span id="L2028"></span>
<span id="L2029">! === module MOM_CVMix_shear ===</span>
<span id="L2030">! Parameterization of shear-driven turbulence via CVMix (various options)</span>
<span id="L2031">USE_LMD94 = False               !   [Boolean] default = False</span>
<span id="L2032">                                ! If true, use the Large-McWilliams-Doney (JGR 1994) shear mixing</span>
<span id="L2033">                                ! parameterization.</span>
<span id="L2034">USE_PP81 = False                !   [Boolean] default = False</span>
<span id="L2035">                                ! If true, use the Pacanowski and Philander (JPO 1981) shear mixing</span>
<span id="L2036">                                ! parameterization.</span>
<span id="L2037"></span>
<span id="L2038">! === module MOM_CVMix_ddiff ===</span>
<span id="L2039">! Parameterization of mixing due to double diffusion processes via CVMix</span>
<span id="L2040">USE_CVMIX_DDIFF = False         !   [Boolean] default = False</span>
<span id="L2041">                                ! If true, turns on double diffusive processes via CVMix. Note that double</span>
<span id="L2042">                                ! diffusive processes on viscosity are ignored in CVMix, see</span>
<span id="L2043">                                ! http://cvmix.github.io/ for justification.</span>
<span id="L2044"></span>
<span id="L2045">! === module MOM_diabatic_aux ===</span>
<span id="L2046">! The following parameters are used for auxiliary diabatic processes.</span>
<span id="L2047">RECLAIM_FRAZIL = True           !   [Boolean] default = True</span>
<span id="L2048">                                ! If true, try to use any frazil heat deficit to cool any overlying layers down</span>
<span id="L2049">                                ! to the freezing point, thereby avoiding the creation of thin ice when the SST</span>
<span id="L2050">                                ! is above the freezing point.</span>
<span id="L2051">SALT_EXTRACTION_LIMIT = 0.9999  !   [nondim] default = 0.9999</span>
<span id="L2052">                                ! An upper limit on the fraction of the salt in a layer that can be lost to the</span>
<span id="L2053">                                ! net surface salt fluxes within a timestep.</span>
<span id="L2054">PRESSURE_DEPENDENT_FRAZIL = False !   [Boolean] default = False</span>
<span id="L2055">                                ! If true, use a pressure dependent freezing temperature when making frazil. The</span>
<span id="L2056">                                ! default is false, which will be faster but is inappropriate with ice-shelf</span>
<span id="L2057">                                ! cavities.</span>
<span id="L2058">DO_BRINE_PLUME = False          !   [Boolean] default = False</span>
<span id="L2059">                                ! If true, use a brine plume parameterization from Nguyen et al., 2009.</span>
<span id="L2060">VAR_PEN_SW = True               !   [Boolean] default = False</span>
<span id="L2061">                                ! If true, use one of the CHL_A schemes specified by OPACITY_SCHEME to determine</span>
<span id="L2062">                                ! the e-folding depth of incoming short wave radiation.</span>
<span id="L2063">CHL_FROM_FILE = True            !   [Boolean] default = True</span>
<span id="L2064">                                ! If true, chl_a is read from a file.</span>
<span id="L2065">CHL_FILE = &quot;seawifs_1998-2006_GOLD_smoothed_2X.nc&quot; !</span>
<span id="L2066">                                ! CHL_FILE is the file containing chl_a concentrations in the variable CHL_A. It</span>
<span id="L2067">                                ! is used when VAR_PEN_SW and CHL_FROM_FILE are true.</span>
<span id="L2068">CHL_VARNAME = &quot;CHL_A&quot;           ! default = &quot;CHL_A&quot;</span>
<span id="L2069">                                ! Name of CHL_A variable in CHL_FILE.</span>
<span id="L2070"></span>
<span id="L2071">! === module MOM_mixed_layer ===</span>
<span id="L2072">NSTAR = 0.15                    !   [nondim] default = 0.15</span>
<span id="L2073">                                ! The portion of the buoyant potential energy imparted by surface fluxes that is</span>
<span id="L2074">                                ! available to drive entrainment at the base of mixed layer when that energy is</span>
<span id="L2075">                                ! positive.</span>
<span id="L2076">BULK_RI_ML = 0.05               !   [nondim]</span>
<span id="L2077">                                ! The efficiency with which mean kinetic energy released by mechanically forced</span>
<span id="L2078">                                ! entrainment of the mixed layer is converted to turbulent kinetic energy.</span>
<span id="L2079">ABSORB_ALL_SW = True            !   [Boolean] default = False</span>
<span id="L2080">                                ! If true,  all shortwave radiation is absorbed by the ocean, instead of passing</span>
<span id="L2081">                                ! through to the bottom mud.</span>
<span id="L2082">NSTAR2 = 0.15                   !   [nondim] default = 0.15</span>
<span id="L2083">                                ! The portion of any potential energy released by convective adjustment that is</span>
<span id="L2084">                                ! available to drive entrainment at the base of mixed layer. By default</span>
<span id="L2085">                                ! NSTAR2=NSTAR.</span>
<span id="L2086">BULK_RI_CONVECTIVE = 0.05       !   [nondim] default = 0.05</span>
<span id="L2087">                                ! The efficiency with which convectively released mean kinetic energy is</span>
<span id="L2088">                                ! converted to turbulent kinetic energy.  By default</span>
<span id="L2089">                                ! BULK_RI_CONVECTIVE=BULK_RI_ML.</span>
<span id="L2090">HMIX_MIN = 2.0                  !   [m] default = 0.0</span>
<span id="L2091">                                ! The minimum mixed layer depth if the mixed layer depth is determined</span>
<span id="L2092">                                ! dynamically.</span>
<span id="L2093">MECH_TKE_FLOOR = 1.0E-150       !   [m3 s-2] default = 1.0E-150</span>
<span id="L2094">                                ! A tiny floor on the amount of turbulent kinetic energy that is used when the</span>
<span id="L2095">                                ! mixed layer does not yet contain HMIX_MIN fluid.  The default is so small that</span>
<span id="L2096">                                ! its actual value is irrelevant, so long as it is greater than 0.</span>
<span id="L2097">LIMIT_BUFFER_DETRAIN = True     !   [Boolean] default = False</span>
<span id="L2098">                                ! If true, limit the detrainment from the buffer layers to not be too different</span>
<span id="L2099">                                ! from the neighbors.</span>
<span id="L2100">ALLOWED_DETRAIN_TEMP_CHG = 0.5  !   [K] default = 0.5</span>
<span id="L2101">                                ! The amount by which temperature is allowed to exceed previous values during</span>
<span id="L2102">                                ! detrainment.</span>
<span id="L2103">ALLOWED_DETRAIN_SALT_CHG = 0.1  !   [ppt] default = 0.1</span>
<span id="L2104">                                ! The amount by which salinity is allowed to exceed previous values during</span>
<span id="L2105">                                ! detrainment.</span>
<span id="L2106">ML_DT_DS_WEIGHT = 6.0           !   [degC ppt-1] default = 6.0</span>
<span id="L2107">                                ! When forced to extrapolate T &amp; S to match the layer densities, this factor (in</span>
<span id="L2108">                                ! deg C / PSU) is combined with the derivatives of density with T &amp; S to</span>
<span id="L2109">                                ! determine what direction is orthogonal to density contours. It should be a</span>
<span id="L2110">                                ! typical value of (dR/dS) / (dR/dT) in oceanic profiles.</span>
<span id="L2111">BUFFER_LAYER_EXTRAP_LIMIT = -1.0 !   [nondim] default = -1.0</span>
<span id="L2112">                                ! A limit on the density range over which extrapolation can occur when</span>
<span id="L2113">                                ! detraining from the buffer layers, relative to the density range within the</span>
<span id="L2114">                                ! mixed and buffer layers, when the detrainment is going into the lightest</span>
<span id="L2115">                                ! interior layer, nondimensional, or a negative value not to apply this limit.</span>
<span id="L2116">BUFFER_LAYER_HMIN_THICK = 5.0   !   [m] default = 5.0</span>
<span id="L2117">                                ! The minimum buffer layer thickness when the mixed layer is very thick.</span>
<span id="L2118">BUFFER_LAYER_HMIN_REL = 0.05    !   [nondim] default = 0.05</span>
<span id="L2119">                                ! The minimum buffer layer thickness relative to the combined mixed land buffer</span>
<span id="L2120">                                ! ayer thicknesses when they are thin.</span>
<span id="L2121">BUFFER_LAY_DETRAIN_TIME = 1.44E+04 !   [s] default = 1.44E+04</span>
<span id="L2122">                                ! A timescale that characterizes buffer layer detrainment events.</span>
<span id="L2123">BUFFER_SPLIT_RHO_TOL = 0.1      !   [nondim] default = 0.1</span>
<span id="L2124">                                ! The fractional tolerance for matching layer target densities when splitting</span>
<span id="L2125">                                ! layers to deal with massive interior layers that are lighter than one of the</span>
<span id="L2126">                                ! mixed or buffer layers.</span>
<span id="L2127">DEPTH_LIMIT_FLUXES = 0.1        !   [m] default = 0.2</span>
<span id="L2128">                                ! The surface fluxes are scaled away when the total ocean depth is less than</span>
<span id="L2129">                                ! DEPTH_LIMIT_FLUXES.</span>
<span id="L2130">ML_RESORT = True                !   [Boolean] default = False</span>
<span id="L2131">                                ! If true, resort the topmost layers by potential density before the mixed layer</span>
<span id="L2132">                                ! calculations.</span>
<span id="L2133">ML_PRESORT_NK_CONV_ADJ = 4      !   [nondim] default = 0</span>
<span id="L2134">                                ! Convectively mix the first ML_PRESORT_NK_CONV_ADJ layers before sorting when</span>
<span id="L2135">                                ! ML_RESORT is true.</span>
<span id="L2136">BML_USTAR_MIN = 1.45842E-18     !   [m s-1] default = 1.45842E-18</span>
<span id="L2137">                                ! The minimum value of ustar that should be used by the bulk mixed layer model</span>
<span id="L2138">                                ! in setting vertical TKE decay scales. This must be greater than 0.</span>
<span id="L2139">BML_NONBOUSINESQ = False        !   [Boolean] default = False</span>
<span id="L2140">                                ! If true, use non-Boussinesq expressions for the energetic calculations used in</span>
<span id="L2141">                                ! the bulk mixed layer calculations.</span>
<span id="L2142">RESOLVE_EKMAN = False           !   [Boolean] default = False</span>
<span id="L2143">                                ! If true, the NKML&gt;1 layers in the mixed layer are chosen to optimally</span>
<span id="L2144">                                ! represent the impact of the Ekman transport on the mixed layer TKE budget.</span>
<span id="L2145">                                ! Otherwise, the sublayers are distributed uniformly through the mixed layer.</span>
<span id="L2146">CORRECT_ABSORPTION_DEPTH = True !   [Boolean] default = False</span>
<span id="L2147">                                ! If true, the average depth at which penetrating shortwave radiation is</span>
<span id="L2148">                                ! absorbed is adjusted to match the average heating depth of an exponential</span>
<span id="L2149">                                ! profile by moving some of the heating upward in the water column.</span>
<span id="L2150">DO_RIVERMIX = True              !   [Boolean] default = False</span>
<span id="L2151">                                ! If true, apply additional mixing wherever there is runoff, so that it is mixed</span>
<span id="L2152">                                ! down to RIVERMIX_DEPTH, if the ocean is that deep.</span>
<span id="L2153">RIVERMIX_DEPTH = 40.0           !   [m] default = 0.0</span>
<span id="L2154">                                ! The depth to which rivers are mixed if DO_RIVERMIX is defined.</span>
<span id="L2155">USE_RIVER_HEAT_CONTENT = False  !   [Boolean] default = False</span>
<span id="L2156">                                ! If true, use the fluxes%runoff_Hflx field to set the heat carried by runoff,</span>
<span id="L2157">                                ! instead of using SST*CP*liq_runoff.</span>
<span id="L2158">USE_CALVING_HEAT_CONTENT = False !   [Boolean] default = False</span>
<span id="L2159">                                ! If true, use the fluxes%calving_Hflx field to set the heat carried by runoff,</span>
<span id="L2160">                                ! instead of using SST*CP*froz_runoff.</span>
<span id="L2161">BULKML_CONV_MOMENTUM_BUG = False !   [Boolean] default = False</span>
<span id="L2162">                                ! If true, use code with a bug that causes a loss of momentum conservation</span>
<span id="L2163">                                ! during mixedlayer convection.</span>
<span id="L2164">LIMIT_BUFFER_DET_DH_SFC = 0.5   !   [nondim] default = 0.5</span>
<span id="L2165">                                ! The fractional limit in the change between grid points of the surface region</span>
<span id="L2166">                                ! (mixed &amp; buffer layer) thickness.</span>
<span id="L2167">LIMIT_BUFFER_DET_DH_BATHY = 0.2 !   [nondim] default = 0.2</span>
<span id="L2168">                                ! The fraction of the total depth by which the thickness of the surface region</span>
<span id="L2169">                                ! (mixed &amp; buffer layer) is allowed to change between grid points.</span>
<span id="L2170"></span>
<span id="L2171">! === module MOM_regularize_layers ===</span>
<span id="L2172">REGULARIZE_SURFACE_LAYERS = False !   [Boolean] default = False</span>
<span id="L2173">                                ! If defined, vertically restructure the near-surface layers when they have too</span>
<span id="L2174">                                ! much lateral variations to allow for sensible lateral barotropic transports.</span>
<span id="L2175"></span>
<span id="L2176">! === module MOM_opacity ===</span>
<span id="L2177">OPACITY_SCHEME = &quot;MANIZZA_05&quot;   ! default = &quot;MANIZZA_05&quot;</span>
<span id="L2178">                                ! This character string specifies how chlorophyll concentrations are translated</span>
<span id="L2179">                                ! into opacities. Currently valid options include:</span>
<span id="L2180">                                !        MANIZZA_05 - Use Manizza et al., GRL, 2005.</span>
<span id="L2181">                                !        MOREL_88 - Use Morel, JGR, 1988.</span>
<span id="L2182">                                !        OHLMANN_03 - Use Ohlmann, J Clim, 2003. (only use if dz(1)&gt;2.0m)</span>
<span id="L2183">BLUE_FRAC_SW = 0.5              !   [nondim] default = 0.5</span>
<span id="L2184">                                ! The fraction of the penetrating shortwave radiation that is in the blue band.</span>
<span id="L2185">PEN_SW_NBANDS = 3               ! default = 1</span>
<span id="L2186">                                ! The number of bands of penetrating shortwave radiation.</span>
<span id="L2187">OPTICS_ANSWER_DATE = 99991231   ! default = 99991231</span>
<span id="L2188">                                ! The vintage of the order of arithmetic and expressions in the optics</span>
<span id="L2189">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L2190">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L2191">PEN_SW_FLUX_ABSORB = 2.5E-11    !   [degC m s-1] default = 2.5E-11</span>
<span id="L2192">                                ! A minimum remaining shortwave heating rate that will be simply absorbed in the</span>
<span id="L2193">                                ! next sufficiently thick layers for computational efficiency, instead of</span>
<span id="L2194">                                ! continuing to penetrate.  The default, 2.5e-11 degC m s-1, is about 1e-4 W m-2</span>
<span id="L2195">                                ! or 0.08 degC m century-1, but 0 is also a valid value.</span>
<span id="L2196">PEN_SW_ABSORB_MINTHICK = 1.0    !   [m] default = 1.0</span>
<span id="L2197">                                ! A thickness that is used to absorb the remaining penetrating shortwave heat</span>
<span id="L2198">                                ! flux when it drops below PEN_SW_FLUX_ABSORB.</span>
<span id="L2199">OPACITY_VALUES_MANIZZA = 0.0232, 0.074, 0.225, 0.037, 2.86, 0.0 !   [m-1] default = 0.0232, 0.074, 0.225, 0.037, 2.86, 0.0</span>
<span id="L2200">                                ! Pairs of opacity coefficients for blue, red and near-infrared radiation with</span>
<span id="L2201">                                ! parameterizations following the functional form from Manizza et al., GRL 2005,</span>
<span id="L2202">                                ! namely in the form opacity = coef_1 + coef_2 * chl**pow for each band.</span>
<span id="L2203">                                ! Although coefficients are set for 3 bands, more or less bands may actually be</span>
<span id="L2204">                                ! used, with extra bands following the same properties as band 3.</span>
<span id="L2205">CHOROPHYLL_POWER_MANIZZA = 0.674, 0.629, 0.0 !   [nondim] default = 0.674, 0.629, 0.0</span>
<span id="L2206">                                ! Powers of chlorophyll for blue, red and near-infrared radiation bands in</span>
<span id="L2207">                                ! expressions for opacity of the form opacity = coef_1 + coef_2 * chl**pow.</span>
<span id="L2208">OPACITY_BAND_WAVELENGTHS = 0.0, 550.0, 700.0, 2800.0 !   [nm] default = 0.0, 550.0, 700.0, 2800.0</span>
<span id="L2209">                                ! The bounding wavelengths for the various bands of shortwave radiation, with</span>
<span id="L2210">                                ! defaults that depend on the setting for OPACITY_SCHEME.</span>
<span id="L2211">OPACITY_LAND_VALUE = 10.0       !   [m-1] default = 10.0</span>
<span id="L2212">                                ! The value to use for opacity over land. The default is 10 m-1 - a value for</span>
<span id="L2213">                                ! muddy water.</span>
<span id="L2214"></span>
<span id="L2215">! === module MOM_tracer_advect ===</span>
<span id="L2216">TRACER_ADVECTION_SCHEME = &quot;PLM&quot; ! default = &quot;PLM&quot;</span>
<span id="L2217">                                ! The horizontal transport scheme for tracers:</span>
<span id="L2218">                                !   PLM    - Piecewise Linear Method</span>
<span id="L2219">                                !   PPM:H3 - Piecewise Parabolic Method (Huyhn 3rd order)</span>
<span id="L2220">                                !   PPM    - Piecewise Parabolic Method (Colella-Woodward)</span>
<span id="L2221"></span>
<span id="L2222">! === module MOM_tracer_hor_diff ===</span>
<span id="L2223">KHTR = 10.0                     !   [m2 s-1] default = 0.0</span>
<span id="L2224">                                ! The background along-isopycnal tracer diffusivity.</span>
<span id="L2225">KHTR_MIN = 50.0                 !   [m2 s-1] default = 0.0</span>
<span id="L2226">                                ! The minimum along-isopycnal tracer diffusivity.</span>
<span id="L2227">FULL_DEPTH_KHTR_MIN = False     !   [Boolean] default = False</span>
<span id="L2228">                                ! If true, KHTR_MIN is enforced throughout the whole water column. Otherwise,</span>
<span id="L2229">                                ! KHTR_MIN is only enforced at the surface. This parameter is only available</span>
<span id="L2230">                                ! when KHTR_USE_EBT_STRUCT=True and KHTR_MIN&gt;0.</span>
<span id="L2231">KHTR_MAX = 900.0                !   [m2 s-1] default = 0.0</span>
<span id="L2232">                                ! The maximum along-isopycnal tracer diffusivity. Set to a positive value to</span>
<span id="L2233">                                ! activate.</span>
<span id="L2234">KHTR_PASSIVITY_COEFF = 3.0      !   [nondim] default = 0.0</span>
<span id="L2235">                                ! The coefficient that scales deformation radius over grid-spacing in passivity,</span>
<span id="L2236">                                ! where passivity is the ratio between along isopycnal mixing of tracers to</span>
<span id="L2237">                                ! thickness mixing. A non-zero value enables this parameterization.</span>
<span id="L2238">KHTR_PASSIVITY_MIN = 0.5        !   [nondim] default = 0.5</span>
<span id="L2239">                                ! The minimum passivity which is the ratio between along isopycnal mixing of</span>
<span id="L2240">                                ! tracers to thickness mixing.</span>
<span id="L2241">DIFFUSE_ML_TO_INTERIOR = True   !   [Boolean] default = False</span>
<span id="L2242">                                ! If true, enable epipycnal mixing between the surface boundary layer and the</span>
<span id="L2243">                                ! interior.</span>
<span id="L2244">CHECK_DIFFUSIVE_CFL = False     !   [Boolean] default = False</span>
<span id="L2245">                                ! If true, use enough iterations the diffusion to ensure that the diffusive</span>
<span id="L2246">                                ! equivalent of the CFL limit is not violated.  If false, always use the greater</span>
<span id="L2247">                                ! of 1 or MAX_TR_DIFFUSION_CFL iteration.</span>
<span id="L2248">MAX_TR_DIFFUSION_CFL = -1.0     !   [nondim] default = -1.0</span>
<span id="L2249">                                ! If positive, locally limit the along-isopycnal tracer diffusivity to keep the</span>
<span id="L2250">                                ! diffusive CFL locally at or below this value.  The number of diffusive</span>
<span id="L2251">                                ! iterations is often this value or the next greater integer.</span>
<span id="L2252">RECALC_NEUTRAL_SURF = False     !   [Boolean] default = False</span>
<span id="L2253">                                ! If true, then recalculate the neutral surfaces if the</span>
<span id="L2254">                                ! diffusive CFL is exceeded. If false, assume that the</span>
<span id="L2255">                                ! positions of the surfaces do not change</span>
<span id="L2256">HOR_DIFF_ANSWER_DATE = 20240101 ! default = 99991231</span>
<span id="L2257">                                ! The vintage of the order of arithmetic to use for the tracer diffusion.</span>
<span id="L2258">                                ! Values of 20240330 or below recover the answers from the original form of the</span>
<span id="L2259">                                ! along-isopycnal mixed layer to interior mixing code, while higher values use</span>
<span id="L2260">                                ! mathematically equivalent expressions that recover rotational symmetry when</span>
<span id="L2261">                                ! DIFFUSE_ML_TO_INTERIOR is true.</span>
<span id="L2262">HOR_DIFF_LIMIT_BUG = True       !   [Boolean] default = False</span>
<span id="L2263">                                ! If true and the answer date is 20240330 or below, use a rotational symmetry</span>
<span id="L2264">                                ! breaking bug when limiting the tracer properties in tracer_epipycnal_ML_diff.</span>
<span id="L2265">ML_KHTR_SCALE = 0.0             !   [nondim] default = 1.0</span>
<span id="L2266">                                ! With Diffuse_ML_interior, the ratio of the truly horizontal diffusivity in the</span>
<span id="L2267">                                ! mixed layer to the epipycnal diffusivity.  The valid range is 0 to 1.</span>
<span id="L2268"></span>
<span id="L2269">! === module MOM_neutral_diffusion ===</span>
<span id="L2270">! This module implements neutral diffusion of tracers</span>
<span id="L2271">USE_NEUTRAL_DIFFUSION = False   !   [Boolean] default = False</span>
<span id="L2272">                                ! If true, enables the neutral diffusion module.</span>
<span id="L2273"></span>
<span id="L2274">! === module MOM_hor_bnd_diffusion ===</span>
<span id="L2275">! This module implements horizontal diffusion of tracers near boundaries</span>
<span id="L2276">USE_HORIZONTAL_BOUNDARY_DIFFUSION = False !   [Boolean] default = False</span>
<span id="L2277">                                ! If true, enables the horizonal boundary tracer&#x27;s diffusion module.</span>
<span id="L2278">OBSOLETE_DIAGNOSTIC_IS_FATAL = True !   [Boolean] default = True</span>
<span id="L2279">                                ! If an obsolete diagnostic variable appears in the diag_table, cause a FATAL</span>
<span id="L2280">                                ! error rather than issue a WARNING.</span>
<span id="L2281"></span>
<span id="L2282">! === module MOM_sum_output ===</span>
<span id="L2283">CALCULATE_APE = True            !   [Boolean] default = True</span>
<span id="L2284">                                ! If true, calculate the available potential energy of the interfaces.  Setting</span>
<span id="L2285">                                ! this to false reduces the memory footprint of high-PE-count models</span>
<span id="L2286">                                ! dramatically.</span>
<span id="L2287">WRITE_STOCKS = True             !   [Boolean] default = True</span>
<span id="L2288">                                ! If true, write the integrated tracer amounts to stdout when the energy files</span>
<span id="L2289">                                ! are written.</span>
<span id="L2290">MAXTRUNC = 5000                 !   [truncations save_interval-1] default = 0</span>
<span id="L2291">                                ! The run will be stopped, and the day set to a very large value if the velocity</span>
<span id="L2292">                                ! is truncated more than MAXTRUNC times between energy saves.  Set MAXTRUNC to 0</span>
<span id="L2293">                                ! to stop if there is any truncation of velocities.</span>
<span id="L2294">MAX_ENERGY = 0.0                !   [m2 s-2] default = 0.0</span>
<span id="L2295">                                ! The maximum permitted average energy per unit mass; the model will be stopped</span>
<span id="L2296">                                ! if there is more energy than this.  If zero or negative, this is set to</span>
<span id="L2297">                                ! 10*MAXVEL^2.</span>
<span id="L2298">MAXVEL = 6.0                    !   [m s-1] default = 3.0E+08</span>
<span id="L2299">                                ! The maximum velocity allowed before the velocity components are truncated.</span>
<span id="L2300">ENERGYFILE = &quot;ocean.stats&quot;      ! default = &quot;ocean.stats&quot;</span>
<span id="L2301">                                ! The file to use to write the energies and globally summed diagnostics.</span>
<span id="L2302">DATE_STAMPED_STDOUT = True      !   [Boolean] default = True</span>
<span id="L2303">                                ! If true, use dates (not times) in messages to stdout</span>
<span id="L2304">ISO_DATE_STAMPED_STDOUT = False !   [Boolean] default = False</span>
<span id="L2305">                                ! If true, use ISO formatted dates in messages to stdout</span>
<span id="L2306">TIMEUNIT = 8.64E+04             !   [s] default = 8.64E+04</span>
<span id="L2307">                                ! The time unit in seconds a number of input fields</span>
<span id="L2308">READ_DEPTH_LIST = False         !   [Boolean] default = False</span>
<span id="L2309">                                ! Read the depth list from a file if it exists or create that file otherwise.</span>
<span id="L2310">DEPTH_LIST_MIN_INC = 1.0E-10    !   [m] default = 1.0E-10</span>
<span id="L2311">                                ! The minimum increment between the depths of the entries in the depth-list</span>
<span id="L2312">                                ! file.</span>
<span id="L2313">ENERGYSAVEDAYS = 0.5            !   [days] default = 1.0</span>
<span id="L2314">                                ! The interval in units of TIMEUNIT between saves of the energies of the run and</span>
<span id="L2315">                                ! other globally summed diagnostics.</span>
<span id="L2316">ENERGYSAVEDAYS_GEOMETRIC = 0.0  !   [days] default = 0.0</span>
<span id="L2317">                                ! The starting interval in units of TIMEUNIT for the first call to save the</span>
<span id="L2318">                                ! energies of the run and other globally summed diagnostics. The interval</span>
<span id="L2319">                                ! increases by a factor of 2. after each call to write_energy.</span>
<span id="L2320"></span>
<span id="L2321">! === module ocean_stochastics_init ===</span>
<span id="L2322">DO_SPPT = False                 !   [Boolean] default = False</span>
<span id="L2323">                                ! If true, then stochastically perturb the thermodynamic tendencies of T,S, amd</span>
<span id="L2324">                                ! h.  Amplitude and correlations are controlled by the nam_stoch namelist in the</span>
<span id="L2325">                                ! UFS model only.</span>
<span id="L2326">DO_SKEB = False                 !   [Boolean] default = False</span>
<span id="L2327">                                ! If true, then stochastically perturb the currents using the stochastic kinetic</span>
<span id="L2328">                                ! energy backscatter scheme.</span>
<span id="L2329">PERT_EPBL = False               !   [Boolean] default = False</span>
<span id="L2330">                                ! If true, then stochastically perturb the kinetic energy production and</span>
<span id="L2331">                                ! dissipation terms.  Amplitude and correlations are controlled by the nam_stoch</span>
<span id="L2332">                                ! namelist in the UFS model only.</span>
<span id="L2333"></span>
<span id="L2334">! === module MOM_surface_forcing ===</span>
<span id="L2335">VARIABLE_WINDS = True           !   [Boolean] default = True</span>
<span id="L2336">                                ! If true, the winds vary in time after the initialization.</span>
<span id="L2337">VARIABLE_BUOYFORCE = True       !   [Boolean] default = True</span>
<span id="L2338">                                ! If true, the buoyancy forcing varies in time after the initialization of the</span>
<span id="L2339">                                ! model.</span>
<span id="L2340">BUOY_CONFIG = &quot;file&quot;            ! default = &quot;zero&quot;</span>
<span id="L2341">                                ! The character string that indicates how buoyancy forcing is specified.  Valid</span>
<span id="L2342">                                ! options include (file), (data_override), (zero), (const), (linear), (MESO),</span>
<span id="L2343">                                ! (SCM_CVmix_tests), (BFB), (dumbbell), (USER) and (NONE).</span>
<span id="L2344">ARCHAIC_OMIP_FORCING_FILE = False !   [Boolean] default = True</span>
<span id="L2345">                                ! If true, use the forcing variable decomposition from the old German OMIP</span>
<span id="L2346">                                ! prescription that predated CORE. If false, use the variable groupings</span>
<span id="L2347">                                ! available from MOM output diagnostics of forcing variables.</span>
<span id="L2348">LONGWAVE_FILE = &quot;ocean_forcing_daily.nc&quot; !</span>
<span id="L2349">                                ! The file with the longwave heat flux, in the variable given by</span>
<span id="L2350">                                ! LONGWAVE_FORCING_VAR.</span>
<span id="L2351">LONGWAVE_FORCING_VAR = &quot;LW&quot;     ! default = &quot;LW&quot;</span>
<span id="L2352">                                ! The variable with the longwave forcing field.</span>
<span id="L2353">LONGWAVE_FILE_DAYS_PER_RECORD = 0 ! default = 0</span>
<span id="L2354">                                ! If positive the number of days of longwave fluxes per time level in</span>
<span id="L2355">                                ! LONGWAVE_FILE, or if negative the number of time levels per day.  If 31 change</span>
<span id="L2356">                                ! forcing monthly, or if 0 the model will guess the right value based on the</span>
<span id="L2357">                                ! file size.</span>
<span id="L2358">SHORTWAVE_FILE = &quot;ocean_forcing_daily.nc&quot; !</span>
<span id="L2359">                                ! The file with the shortwave heat flux, in the variable given by</span>
<span id="L2360">                                ! SHORTWAVE_FORCING_VAR.</span>
<span id="L2361">SHORTWAVE_FORCING_VAR = &quot;SW&quot;    ! default = &quot;SW&quot;</span>
<span id="L2362">                                ! The variable with the shortwave forcing field.</span>
<span id="L2363">SHORTWAVE_FILE_DAYS_PER_RECORD = 0 ! default = 0</span>
<span id="L2364">                                ! If positive the number of days of shortwave fluxes per time level in</span>
<span id="L2365">                                ! SHORTWAVE_FILE, or if negative the number of time levels per day.  If 31</span>
<span id="L2366">                                ! change forcing monthly, or if 0 the model will guess the right value based on</span>
<span id="L2367">                                ! the file size.</span>
<span id="L2368">EVAPORATION_FILE = &quot;ocean_forcing_daily.nc&quot; !</span>
<span id="L2369">                                ! The file with the evaporative moisture flux, in the variable given by</span>
<span id="L2370">                                ! EVAP_FORCING_VAR.</span>
<span id="L2371">EVAP_FORCING_VAR = &quot;evap&quot;       ! default = &quot;evap&quot;</span>
<span id="L2372">                                ! The variable with the evaporative moisture flux.</span>
<span id="L2373">EVAPORATION_FILE_DAYS_PER_RECORD = 0 ! default = 0</span>
<span id="L2374">                                ! If positive the number of days of evaporation per time level in</span>
<span id="L2375">                                ! EVAPORATION_FILE, or if negative the number of time levels per day.  If 31</span>
<span id="L2376">                                ! change forcing monthly, or if 0 the model will guess the right value based on</span>
<span id="L2377">                                ! the file size.</span>
<span id="L2378">LATENTHEAT_FILE = &quot;ocean_forcing_daily.nc&quot; !</span>
<span id="L2379">                                ! The file with the latent heat flux, in the variable given by</span>
<span id="L2380">                                ! LATENT_FORCING_VAR.</span>
<span id="L2381">LATENT_FORCING_VAR = &quot;latent&quot;   ! default = &quot;latent&quot;</span>
<span id="L2382">                                ! The variable with the latent heat flux.</span>
<span id="L2383">LATENTHEAT_FILE_DAYS_PER_RECORD = 0 ! default = 0</span>
<span id="L2384">                                ! If positive the number of days of latent heat fluxes per time level in</span>
<span id="L2385">                                ! LATENTHEAT_FILE, or if negative the number of time levels per day.  If 31</span>
<span id="L2386">                                ! change forcing monthly, or if 0 the model will guess the right value based on</span>
<span id="L2387">                                ! the file size.</span>
<span id="L2388">SENSIBLEHEAT_FILE = &quot;ocean_forcing_daily.nc&quot; !</span>
<span id="L2389">                                ! The file with the sensible heat flux, in the variable given by</span>
<span id="L2390">                                ! SENSIBLE_FORCING_VAR.</span>
<span id="L2391">SENSIBLE_FORCING_VAR = &quot;sensible&quot; ! default = &quot;sensible&quot;</span>
<span id="L2392">                                ! The variable with the sensible heat flux.</span>
<span id="L2393">SENSIBLEHEAT_FILE_DAYS_PER_RECORD = 0 ! default = 0</span>
<span id="L2394">                                ! If positive the number of days of sensible heat fluxes per time level in</span>
<span id="L2395">                                ! SENSIBLEHEAT_FILE, or if negative the number of time levels per day.  If 31</span>
<span id="L2396">                                ! change forcing monthly, or if 0 the model will guess the right value based on</span>
<span id="L2397">                                ! the file size.</span>
<span id="L2398">RAIN_FILE = &quot;ocean_precip_monthly.nc&quot; !</span>
<span id="L2399">                                ! The file with the liquid precipitation flux, in the variable given by</span>
<span id="L2400">                                ! RAIN_FORCING_VAR.</span>
<span id="L2401">RAIN_FORCING_VAR = &quot;liq_precip&quot; ! default = &quot;liq_precip&quot;</span>
<span id="L2402">                                ! The variable with the liquid precipitation flux.</span>
<span id="L2403">RAIN_FILE_DAYS_PER_RECORD = 0   ! default = 0</span>
<span id="L2404">                                ! If positive the number of days of rain fluxes per time level in RAIN_FILE, or</span>
<span id="L2405">                                ! if negative the number of time levels per day.  If 31 change forcing monthly,</span>
<span id="L2406">                                ! or if 0 the model will guess the right value based on the file size.</span>
<span id="L2407">SNOW_FILE = &quot;ocean_precip_monthly.nc&quot; !</span>
<span id="L2408">                                ! The file with the frozen precipitation flux, in the variable given by</span>
<span id="L2409">                                ! SNOW_FORCING_VAR.</span>
<span id="L2410">SNOW_FORCING_VAR = &quot;froz_precip&quot; ! default = &quot;froz_precip&quot;</span>
<span id="L2411">                                ! The variable with the frozen precipitation flux.</span>
<span id="L2412">RUNOFF_FILE = &quot;ocean_precip_monthly.nc&quot; !</span>
<span id="L2413">                                ! The file with the fresh and frozen runoff/calving fluxes, in variables given</span>
<span id="L2414">                                ! by LIQ_RUNOFF_FORCING_VAR and FROZ_RUNOFF_FORCING_VAR.</span>
<span id="L2415">LIQ_RUNOFF_FORCING_VAR = &quot;liq_runoff&quot; ! default = &quot;liq_runoff&quot;</span>
<span id="L2416">                                ! The variable with the liquid runoff flux.</span>
<span id="L2417">FROZ_RUNOFF_FORCING_VAR = &quot;froz_runoff&quot; ! default = &quot;froz_runoff&quot;</span>
<span id="L2418">                                ! The variable with the frozen runoff flux.</span>
<span id="L2419">RUNOFF_FILE_DAYS_PER_RECORD = 0 ! default = 0</span>
<span id="L2420">                                ! If positive the number of days of runoff per time level in RUNOFF_FILE, or if</span>
<span id="L2421">                                ! negative the number of time levels per day.  If 31 change forcing monthly, or</span>
<span id="L2422">                                ! if 0 the model will guess the right value based on the file size.</span>
<span id="L2423">SSTRESTORE_FILE = &quot;ocean_forcing_daily.nc&quot; !</span>
<span id="L2424">                                ! The file with the SST toward which to restore in the variable given by</span>
<span id="L2425">                                ! SST_RESTORE_VAR.</span>
<span id="L2426">SALINITYRESTORE_FILE = &quot;ocean_forcing_daily.nc&quot; !</span>
<span id="L2427">                                ! The file with the surface salinity toward which to restore in the variable</span>
<span id="L2428">                                ! given by SSS_RESTORE_VAR.</span>
<span id="L2429">SST_RESTORE_VAR = &quot;SST&quot;         ! default = &quot;SST&quot;</span>
<span id="L2430">                                ! The variable with the SST toward which to restore.</span>
<span id="L2431">SSTRESTORE_FILE_DAYS_PER_RECORD = 0 ! default = 0</span>
<span id="L2432">                                ! If positive the number of days of SST per time level in SSTRESTORE_FILE, or if</span>
<span id="L2433">                                ! negative the number of time levels per day.  If 31 change forcing monthly, or</span>
<span id="L2434">                                ! if 0 the model will guess the right value based on the file size.</span>
<span id="L2435">SSS_RESTORE_VAR = &quot;SSS&quot;         ! default = &quot;SSS&quot;</span>
<span id="L2436">                                ! The variable with the SSS toward which to restore.</span>
<span id="L2437">SALINITYRESTORE_FILE_DAYS_PER_RECORD = 0 ! default = 0</span>
<span id="L2438">                                ! If positive the number of days of salinity per time level in</span>
<span id="L2439">                                ! SALINITYRESTORE_FILE, or if negative the number of time levels per day.  If 31</span>
<span id="L2440">                                ! change forcing monthly, or if 0 the model will guess the right value based on</span>
<span id="L2441">                                ! the file size.</span>
<span id="L2442">WIND_CONFIG = &quot;file&quot;            ! default = &quot;zero&quot;</span>
<span id="L2443">                                ! The character string that indicates how wind forcing is specified.  Valid</span>
<span id="L2444">                                ! options include (file), (data_override), (2gyre), (1gyre), (gyres), (zero),</span>
<span id="L2445">                                ! (const), (Neverworld), (scurves), (ideal_hurr), (SCM_CVmix_tests) and (USER).</span>
<span id="L2446">WIND_FILE = &quot;ocean_forcing_daily.nc&quot; !</span>
<span id="L2447">                                ! The file in which the wind stresses are found in variables STRESS_X and</span>
<span id="L2448">                                ! STRESS_Y.</span>
<span id="L2449">WINDSTRESS_X_VAR = &quot;taux&quot;       ! default = &quot;STRESS_X&quot;</span>
<span id="L2450">                                ! The name of the x-wind stress variable in WIND_FILE.</span>
<span id="L2451">WINDSTRESS_Y_VAR = &quot;tauy&quot;       ! default = &quot;STRESS_Y&quot;</span>
<span id="L2452">                                ! The name of the y-wind stress variable in WIND_FILE.</span>
<span id="L2453">WIND_STAGGER = &quot;C&quot;              ! default = &quot;C&quot;</span>
<span id="L2454">                                ! A character indicating how the wind stress components are staggered in</span>
<span id="L2455">                                ! WIND_FILE.  This may be A or C for now.</span>
<span id="L2456">WINDSTRESS_SCALE = 1.0          !   [nondim] default = 1.0</span>
<span id="L2457">                                ! A value by which the wind stresses in WIND_FILE are rescaled.</span>
<span id="L2458">USTAR_FORCING_VAR = &quot;&quot;          ! default = &quot;&quot;</span>
<span id="L2459">                                ! The name of the friction velocity variable in WIND_FILE or blank to get ustar</span>
<span id="L2460">                                ! from the wind stresses plus the gustiness.</span>
<span id="L2461">WIND_FILE_DAYS_PER_RECORD = 0   ! default = 0</span>
<span id="L2462">                                ! If positive the number of days of wind stress per time level in WIND_FILE, or</span>
<span id="L2463">                                ! if negative the number of time levels per day.  If 31 change forcing monthly,</span>
<span id="L2464">                                ! or if 0 the model will guess the right value based on the file size.</span>
<span id="L2465">RESTOREBUOY = True              !   [Boolean] default = False</span>
<span id="L2466">                                ! If true, the buoyancy fluxes drive the model back toward some specified</span>
<span id="L2467">                                ! surface state with a rate given by FLUXCONST.</span>
<span id="L2468">LATENT_HEAT_FUSION = 3.34E+05   !   [J/kg] default = 3.34E+05</span>
<span id="L2469">                                ! The latent heat of fusion.</span>
<span id="L2470">LATENT_HEAT_VAPORIZATION = 2.5E+06 !   [J/kg] default = 2.5E+06</span>
<span id="L2471">                                ! The latent heat of fusion.</span>
<span id="L2472">FLUXCONST = 0.5                 !   [m day-1] default = 0.0</span>
<span id="L2473">                                ! The constant that relates the restoring surface fluxes to the relative surface</span>
<span id="L2474">                                ! anomalies (akin to a piston velocity).  Note the non-MKS units.</span>
<span id="L2475">FLUXCONST_T = 0.5               !   [m day-1] default = 0.5</span>
<span id="L2476">                                ! The constant that relates the restoring surface temperature flux to the</span>
<span id="L2477">                                ! relative surface anomaly (akin to a piston velocity).  Note the non-MKS units.</span>
<span id="L2478">FLUXCONST_S = 0.5               !   [m day-1] default = 0.5</span>
<span id="L2479">                                ! The constant that relates the restoring surface salinity flux to the relative</span>
<span id="L2480">                                ! surface anomaly (akin to a piston velocity).  Note the non-MKS units.</span>
<span id="L2481">RESTORE_FLUX_RHO = 1035.0       !   [kg m-3] default = 1035.0</span>
<span id="L2482">                                ! The density that is used to convert piston velocities into salt or heat fluxes</span>
<span id="L2483">                                ! with RESTORE_SALINITY or RESTORE_TEMPERATURE.</span>
<span id="L2484">GUST_CONST = 0.0                !   [Pa] default = 0.0</span>
<span id="L2485">                                ! The background gustiness in the winds.</span>
<span id="L2486">USTAR_GUSTLESS_BUG = False      !   [Boolean] default = False</span>
<span id="L2487">                                ! If true include a bug in the time-averaging of the gustless wind friction</span>
<span id="L2488">                                ! velocity</span>
<span id="L2489">READ_GUST_2D = True             !   [Boolean] default = False</span>
<span id="L2490">                                ! If true, use a 2-dimensional gustiness supplied from an input file</span>
<span id="L2491">GUST_2D_FILE = &quot;gustiness_qscat.nc&quot; !</span>
<span id="L2492">                                ! The file in which the wind gustiness is found in variable gustiness.</span>
<span id="L2493"></span>
<span id="L2494">! === module MOM_restart ===</span>
<span id="L2495">USE_WAVES = False               !   [Boolean] default = False</span>
<span id="L2496">                                ! If true, enables surface wave modules.</span>
<span id="L2497"></span>
<span id="L2498">! === module MOM_main (MOM_driver) ===</span>
<span id="L2499">DT_FORCING = 7200.0             !   [s] default = 3600.0</span>
<span id="L2500">                                ! The time step for changing forcing, coupling with other components, or</span>
<span id="L2501">                                ! potentially writing certain diagnostics. The default value is given by DT.</span>
<span id="L2502">DAYMAX = 2.0                    !   [days]</span>
<span id="L2503">                                ! The final time of the whole simulation, in units of TIMEUNIT seconds.  This</span>
<span id="L2504">                                ! also sets the potential end time of the present run segment if the end time is</span>
<span id="L2505">                                ! not set via ocean_solo_nml in input.nml.</span>
<span id="L2506">SINGLE_STEPPING_CALL = True     !   [Boolean] default = True</span>
<span id="L2507">                                ! If true, advance the state of MOM with a single step including both dynamics</span>
<span id="L2508">                                ! and thermodynamics.  If false the two phases are advanced with separate calls.</span>
<span id="L2509">RESTART_CONTROL = 3             ! default = 1</span>
<span id="L2510">                                ! An integer whose bits encode which restart files are written. Add 2 (bit 1)</span>
<span id="L2511">                                ! for a time-stamped file, and odd (bit 0) for a non-time-stamped file. A</span>
<span id="L2512">                                ! non-time-stamped restart file is saved at the end of the run segment for any</span>
<span id="L2513">                                ! non-negative value.</span>
<span id="L2514">RESTINT = 365.0                 !   [days] default = 0.0</span>
<span id="L2515">                                ! The interval between saves of the restart file in units of TIMEUNIT.  Use 0</span>
<span id="L2516">                                ! (the default) to not save incremental restart files at all.</span>
<span id="L2517">WRITE_CPU_STEPS = 1000          ! default = 1000</span>
<span id="L2518">                                ! The number of coupled timesteps between writing the cpu time. If this is not</span>
<span id="L2519">                                ! positive, do not check cpu time, and the segment run-length can not be set via</span>
<span id="L2520">                                ! an elapsed CPU time.</span>
<span id="L2521"></span>
<span id="L2522">! === module MOM_write_cputime ===</span>
<span id="L2523">MAXCPU = 2.88E+04               !   [wall-clock seconds] default = -1.0</span>
<span id="L2524">                                ! The maximum amount of cpu time per processor for which MOM should run before</span>
<span id="L2525">                                ! saving a restart file and quitting with a return value that indicates that a</span>
<span id="L2526">                                ! further run is required to complete the simulation. If automatic restarts are</span>
<span id="L2527">                                ! not desired, use a negative value for MAXCPU.  MAXCPU has units of wall-clock</span>
<span id="L2528">                                ! seconds, so the actual CPU time used is larger by a factor of the number of</span>
<span id="L2529">                                ! processors used.</span>
<span id="L2530">CPU_TIME_FILE = &quot;CPU_stats&quot;     ! default = &quot;CPU_stats&quot;</span>
<span id="L2531">                                ! The file into which CPU time is written.</span>
<span id="L2532"></span>
<span id="L2533">! === module MOM_file_parser ===</span>
<span id="L2534">SEND_LOG_TO_STDOUT = False      !   [Boolean] default = False</span>
<span id="L2535">                                ! If true, all log messages are also sent to stdout.</span>
<span id="L2536">DOCUMENT_FILE = &quot;MOM_parameter_doc&quot; ! default = &quot;MOM_parameter_doc&quot;</span>
<span id="L2537">                                ! The basename for files where run-time parameters, their settings, units and</span>
<span id="L2538">                                ! defaults are documented. Blank will disable all parameter documentation.</span>
<span id="L2539">COMPLETE_DOCUMENTATION = True   !   [Boolean] default = True</span>
<span id="L2540">                                ! If true, all run-time parameters are documented in MOM_parameter_doc.all .</span>
<span id="L2541">MINIMAL_DOCUMENTATION = True    !   [Boolean] default = True</span>
<span id="L2542">                                ! If true, non-default run-time parameters are documented in</span>
<span id="L2543">                                ! MOM_parameter_doc.short .</span>
</pre>
