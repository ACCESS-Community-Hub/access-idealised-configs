---
search:
  exclude: true
---

# nonBous_global: MOM_parameter_doc.all

Every MOM6 parameter of the tested run of [nonBous_global](../mom6examples/nonBous_global.md), as MOM6 wrote it to `MOM_parameter_doc.all` in the run's output folder. Line numbers match the file.

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
<span id="L320">RHO_0 = 1024.0                  !   [kg m-3] default = 1035.0</span>
<span id="L321">                                ! The mean ocean density used with BOUSSINESQ true to calculate accelerations</span>
<span id="L322">                                ! and the mass for conservation properties, or with BOUSSINSEQ false to convert</span>
<span id="L323">                                ! some parameters from vertical units of m to kg m-2.</span>
<span id="L324">BOUSSINESQ = False              !   [Boolean] default = True</span>
<span id="L325">                                ! If true, make the Boussinesq approximation.</span>
<span id="L326">SEMI_BOUSSINESQ = True          !   [Boolean] default = True</span>
<span id="L327">                                ! If true, do non-Boussinesq pressure force calculations and use mass-based</span>
<span id="L328">                                ! thicknesses, but use RHO_0 to convert layer thicknesses into certain height</span>
<span id="L329">                                ! changes.  This only applies if BOUSSINESQ is false.</span>
<span id="L330">RHO_KV_CONVERT = 1024.0         !   [kg m-3] default = 1024.0</span>
<span id="L331">                                ! The density used to convert input vertical distances into thickesses in</span>
<span id="L332">                                ! non-BOUSSINESQ mode, and to convert kinematic viscosities into dynamic</span>
<span id="L333">                                ! viscosities and similarly for vertical diffusivities.  GV%m_to_H is set using</span>
<span id="L334">                                ! this value, whereas GV%Z_to_H is set using RHO_0.  The default is RHO_0, but</span>
<span id="L335">                                ! this can be set separately to demonstrate the independence of the</span>
<span id="L336">                                ! non-Boussinesq solutions of the value of RHO_0.</span>
<span id="L337">ANGSTROM = 1.0E-10              !   [m] default = 1.0E-10</span>
<span id="L338">                                ! The minimum layer thickness, usually one-Angstrom.</span>
<span id="L339">H_TO_KG_M2 = 1.0                !   [kg m-2 H-1] default = 1.0</span>
<span id="L340">                                ! A constant that translates thicknesses from the model&#x27;s internal units of</span>
<span id="L341">                                ! thickness to kg m-2.</span>
<span id="L342">NK = 63                         !   [nondim]</span>
<span id="L343">                                ! The number of model layers.</span>
<span id="L344">ADVECTION_SCHEME_VARIANCE_UNDERFLOW = 1.0E-23 !   [Conc2 (tracer dependent)] default = 1.0E-23</span>
<span id="L345">                                ! A tiny magnitude for variance used to determine when advection scheme variance</span>
<span id="L346">                                ! production is set to 0.</span>
<span id="L347"></span>
<span id="L348">! === module MOM_tracer_registry ===</span>
<span id="L349"></span>
<span id="L350">! === module MOM_EOS ===</span>
<span id="L351">EQN_OF_STATE = &quot;WRIGHT&quot;         ! default = &quot;WRIGHT_FULL&quot;</span>
<span id="L352">                                ! EQN_OF_STATE determines which ocean equation of state should be used.</span>
<span id="L353">                                ! Currently, the valid choices are &quot;LINEAR&quot;, &quot;UNESCO&quot;, &quot;JACKETT_MCD&quot;, &quot;WRIGHT&quot;,</span>
<span id="L354">                                ! &quot;WRIGHT_REDUCED&quot;, &quot;WRIGHT_FULL&quot;, &quot;NEMO&quot;, &quot;ROQUET_RHO&quot;, &quot;ROQUET_SPV&quot; and</span>
<span id="L355">                                ! &quot;TEOS10&quot;.  This is only used if USE_EOS is true.</span>
<span id="L356">USE_WRIGHT_2ND_DERIV_BUG = False !   [Boolean] default = False</span>
<span id="L357">                                ! If true, use a bug in the calculation of the second derivatives of density</span>
<span id="L358">                                ! with temperature and with temperature and pressure that causes some terms to</span>
<span id="L359">                                ! be only 2/3 of what they should be.</span>
<span id="L360">EOS_QUADRATURE = False          !   [Boolean] default = False</span>
<span id="L361">                                ! If true, always use the generic (quadrature) code code for the integrals of</span>
<span id="L362">                                ! density.</span>
<span id="L363">TFREEZE_FORM = &quot;LINEAR&quot;         ! default = &quot;LINEAR&quot;</span>
<span id="L364">                                ! TFREEZE_FORM determines which expression should be used for the freezing</span>
<span id="L365">                                ! point.  Currently, the valid choices are &quot;LINEAR&quot;, &quot;MILLERO_78&quot;, &quot;TEOS_POLY&quot;,</span>
<span id="L366">                                ! &quot;TEOS10&quot;</span>
<span id="L367">TFREEZE_S0_P0 = 0.0             !   [degC] default = 0.0</span>
<span id="L368">                                ! When TFREEZE_FORM=LINEAR, this is the freezing potential temperature at S=0,</span>
<span id="L369">                                ! P=0.</span>
<span id="L370">DTFREEZE_DS = -0.054            !   [degC ppt-1] default = -0.054</span>
<span id="L371">                                ! When TFREEZE_FORM=LINEAR, this is the derivative of the freezing potential</span>
<span id="L372">                                ! temperature with salinity.</span>
<span id="L373">DTFREEZE_DP = 0.0               !   [degC Pa-1] default = 0.0</span>
<span id="L374">                                ! When TFREEZE_FORM=LINEAR, this is the derivative of the freezing potential</span>
<span id="L375">                                ! temperature with pressure.</span>
<span id="L376">TFREEZE_S_IS_PRACS = True       !   [Boolean] default = True</span>
<span id="L377">                                ! When True, the model will check if the model internal salinity is practical</span>
<span id="L378">                                ! salinity.  If the model uses absolute salinity, a conversion will be applied.</span>
<span id="L379">TFREEZE_T_IS_POTT = True        !   [Boolean] default = True</span>
<span id="L380">                                ! When True, the model will check if the model internal temperature is potential</span>
<span id="L381">                                ! temperature.  If the model uses conservative temperature, a conversion will be</span>
<span id="L382">                                ! applied.</span>
<span id="L383"></span>
<span id="L384">! === module MOM_restart ===</span>
<span id="L385">PARALLEL_RESTARTFILES = False   !   [Boolean] default = False</span>
<span id="L386">                                ! If true, the IO layout is used to group processors that write to the same</span>
<span id="L387">                                ! restart file or each processor writes its own (numbered) restart file. If</span>
<span id="L388">                                ! false, a single restart file is generated combining output from all PEs.</span>
<span id="L389">RESTARTFILE = &quot;MOM.res&quot;         ! default = &quot;MOM.res&quot;</span>
<span id="L390">                                ! The name-root of the restart file.</span>
<span id="L391">MAX_FIELDS = 100                ! default = 100</span>
<span id="L392">                                ! The maximum number of restart fields that can be used.</span>
<span id="L393">RESTART_CHECKSUMS_REQUIRED = True !   [Boolean] default = True</span>
<span id="L394">                                ! If true, require the restart checksums to match and error out otherwise. Users</span>
<span id="L395">                                ! may want to avoid this comparison if for example the restarts are made from a</span>
<span id="L396">                                ! run with a different mask_table than the current run, in which case the</span>
<span id="L397">                                ! checksums will not match and cause crash.</span>
<span id="L398">RESTART_SYMMETRIC_CHECKSUMS = False !   [Boolean] default = False</span>
<span id="L399">                                ! If true, do the restart checksums on all the edge points for a non-reentrant</span>
<span id="L400">                                ! grid.  This requires that SYMMETRIC_MEMORY_ is defined at compile time.</span>
<span id="L401">RESTART_UNSIGNED_ZEROS = False  !   [Boolean] default = False</span>
<span id="L402">                                ! If true, convert any negative zeros that would be written to the restart file</span>
<span id="L403">                                ! into ordinary unsigned zeros.  This does not change answers, but it can be</span>
<span id="L404">                                ! helpful in comparing restart files after grid rotation, for example.</span>
<span id="L405">USE_FILTER = False              !   [Boolean] default = False</span>
<span id="L406">                                ! If true, use streaming band-pass filters to detect the instantaneous tidal</span>
<span id="L407">                                ! signals in the simulation.</span>
<span id="L408"></span>
<span id="L409">! === module MOM_tracer_flow_control ===</span>
<span id="L410">USE_USER_TRACER_EXAMPLE = False !   [Boolean] default = False</span>
<span id="L411">                                ! If true, use the USER_tracer_example tracer package.</span>
<span id="L412">USE_DOME_TRACER = False         !   [Boolean] default = False</span>
<span id="L413">                                ! If true, use the DOME_tracer tracer package.</span>
<span id="L414">USE_ISOMIP_TRACER = False       !   [Boolean] default = False</span>
<span id="L415">                                ! If true, use the ISOMIP_tracer tracer package.</span>
<span id="L416">USE_RGC_TRACER = False          !   [Boolean] default = False</span>
<span id="L417">                                ! If true, use the RGC_tracer tracer package.</span>
<span id="L418">USE_IDEAL_AGE_TRACER = True     !   [Boolean] default = False</span>
<span id="L419">                                ! If true, use the ideal_age_example tracer package.</span>
<span id="L420">USE_MARBL_TRACERS = False       !   [Boolean] default = False</span>
<span id="L421">                                ! If true, use the MARBL tracer package.</span>
<span id="L422">USE_REGIONAL_DYES = False       !   [Boolean] default = False</span>
<span id="L423">                                ! If true, use the regional_dyes tracer package.</span>
<span id="L424">USE_FILE_DYES = False           !   [Boolean] default = False</span>
<span id="L425">                                ! If true, use the file dyes tracer package.</span>
<span id="L426">USE_OIL_TRACER = False          !   [Boolean] default = False</span>
<span id="L427">                                ! If true, use the oil_tracer tracer package.</span>
<span id="L428">USE_ADVECTION_TEST_TRACER = False !   [Boolean] default = False</span>
<span id="L429">                                ! If true, use the advection_test_tracer tracer package.</span>
<span id="L430">USE_OCMIP2_CFC = False          !   [Boolean] default = False</span>
<span id="L431">                                ! If true, use the MOM_OCMIP2_CFC tracer package.</span>
<span id="L432">USE_CFC_CAP = False             !   [Boolean] default = False</span>
<span id="L433">                                ! If true, use the MOM_CFC_cap tracer package.</span>
<span id="L434">USE_generic_tracer = False      !   [Boolean] default = False</span>
<span id="L435">                                ! If true and _USE_GENERIC_TRACER is defined as a preprocessor macro, use the</span>
<span id="L436">                                ! MOM_generic_tracer packages.</span>
<span id="L437">USE_PSEUDO_SALT_TRACER = False  !   [Boolean] default = False</span>
<span id="L438">                                ! If true, use the pseudo salt tracer, typically run as a diagnostic.</span>
<span id="L439">USE_BOUNDARY_IMPULSE_TRACER = False !   [Boolean] default = False</span>
<span id="L440">                                ! If true, use the boundary impulse tracer.</span>
<span id="L441">USE_DYED_OBC_TRACER = False     !   [Boolean] default = False</span>
<span id="L442">                                ! If true, use the dyed_obc_tracer tracer package.</span>
<span id="L443">USE_NW2_TRACERS = False         !   [Boolean] default = False</span>
<span id="L444">                                ! If true, use the NeverWorld2 tracers.</span>
<span id="L445"></span>
<span id="L446">! === module ideal_age_example ===</span>
<span id="L447">DO_IDEAL_AGE = True             !   [Boolean] default = True</span>
<span id="L448">                                ! If true, use an ideal age tracer that is set to 0 age in the boundary layer</span>
<span id="L449">                                ! and ages at unit rate in the interior.</span>
<span id="L450">DO_IDEAL_VINTAGE = False        !   [Boolean] default = False</span>
<span id="L451">                                ! If true, use an ideal vintage tracer that is set to an exponentially</span>
<span id="L452">                                ! increasing value in the boundary layer and is conserved thereafter.</span>
<span id="L453">DO_IDEAL_AGE_DATED = False      !   [Boolean] default = False</span>
<span id="L454">                                ! If true, use an ideal age tracer that is everywhere 0 before</span>
<span id="L455">                                ! IDEAL_AGE_DATED_START_YEAR, but the behaves like the standard ideal age tracer</span>
<span id="L456">                                ! - i.e. is set to 0 age in the boundary layer and ages at unit rate in the</span>
<span id="L457">                                ! interior.</span>
<span id="L458">DO_BL_RESIDENCE = False         !   [Boolean] default = False</span>
<span id="L459">                                ! If true, use a residence tracer that is set to 0 age in the interior and ages</span>
<span id="L460">                                ! at unit rate in the boundary layer.</span>
<span id="L461">USE_REAL_BL_DEPTH = False       !   [Boolean] default = False</span>
<span id="L462">                                ! If true, the ideal age tracers will use the boundary layer depth diagnosed</span>
<span id="L463">                                ! from the BL or bulkmixedlayer scheme.</span>
<span id="L464">AGE_IC_FILE = &quot;&quot;                ! default = &quot;&quot;</span>
<span id="L465">                                ! The file in which the age-tracer initial values can be found, or an empty</span>
<span id="L466">                                ! string for internal initialization.</span>
<span id="L467">AGE_IC_FILE_IS_Z = False        !   [Boolean] default = False</span>
<span id="L468">                                ! If true, AGE_IC_FILE is in depth space, not layer space</span>
<span id="L469">TRACERS_MAY_REINIT = False      !   [Boolean] default = False</span>
<span id="L470">                                ! If true, tracers may go through the initialization code if they are not found</span>
<span id="L471">                                ! in the restart files.  Otherwise it is a fatal error if the tracers are not</span>
<span id="L472">                                ! found in the restart files of a restarted run.</span>
<span id="L473"></span>
<span id="L474">! === module MOM_coord_initialization ===</span>
<span id="L475">COORD_CONFIG = &quot;file&quot;           ! default = &quot;none&quot;</span>
<span id="L476">                                ! This specifies how layers are to be defined:</span>
<span id="L477">                                !     ALE or none - used to avoid defining layers in ALE mode</span>
<span id="L478">                                !     file - read coordinate information from the file</span>
<span id="L479">                                !       specified by (COORD_FILE).</span>
<span id="L480">                                !     BFB - Custom coords for buoyancy-forced basin case</span>
<span id="L481">                                !       based on SST_S, T_BOT and DRHO_DT.</span>
<span id="L482">                                !     linear - linear based on interfaces not layers</span>
<span id="L483">                                !     layer_ref - linear based on layer densities</span>
<span id="L484">                                !     ts_ref - use reference temperature and salinity</span>
<span id="L485">                                !     ts_range - use range of temperature and salinity</span>
<span id="L486">                                !       (T_REF and S_REF) to determine surface density</span>
<span id="L487">                                !       and GINT calculate internal densities.</span>
<span id="L488">                                !     gprime - use reference density (RHO_0) for surface</span>
<span id="L489">                                !       density and GINT calculate internal densities.</span>
<span id="L490">                                !     ts_profile - use temperature and salinity profiles</span>
<span id="L491">                                !       (read from COORD_FILE) to set layer densities.</span>
<span id="L492">                                !     USER - call a user modified routine.</span>
<span id="L493">GFS = 9.8                       !   [m s-2] default = 9.8</span>
<span id="L494">                                ! The reduced gravity at the free surface.</span>
<span id="L495">COORD_FILE = &quot;GOLD_IC.2010.11.15.nc&quot; !</span>
<span id="L496">                                ! The file from which the coordinate densities are read.</span>
<span id="L497">COORD_VAR = &quot;Layer&quot;             ! default = &quot;Layer&quot;</span>
<span id="L498">                                ! The variable in COORD_FILE that is to be used for the coordinate densities.</span>
<span id="L499"></span>
<span id="L500">! === module MOM_state_initialization ===</span>
<span id="L501">FATAL_INCONSISTENT_RESTART_TIME = False !   [Boolean] default = False</span>
<span id="L502">                                ! If true and a time_in value is provided to MOM_initialize_state, verify that</span>
<span id="L503">                                ! the time read from a restart file is the same as time_in, and issue a fatal</span>
<span id="L504">                                ! error if it is not.  Otherwise, simply set the time to time_in if present.</span>
<span id="L505">INIT_LAYERS_FROM_Z_FILE = False !   [Boolean] default = False</span>
<span id="L506">                                ! If true, initialize the layer thicknesses, temperatures, and salinities from a</span>
<span id="L507">                                ! Z-space file on a latitude-longitude grid.</span>
<span id="L508">THICKNESS_CONFIG = &quot;file&quot;       ! default = &quot;uniform&quot;</span>
<span id="L509">                                ! A string that determines how the initial layer thicknesses are specified for a</span>
<span id="L510">                                ! new run:</span>
<span id="L511">                                !     file - read interface heights from the file specified</span>
<span id="L512">                                !       by (THICKNESS_FILE).</span>
<span id="L513">                                !     thickness_file - read thicknesses from the file specified</span>
<span id="L514">                                !       by (THICKNESS_FILE).</span>
<span id="L515">                                !     mass_file - read thicknesses in units of mass per unit area from the file</span>
<span id="L516">                                !       specified by (THICKNESS_FILE).</span>
<span id="L517">                                !     coord - determined by ALE coordinate.</span>
<span id="L518">                                !     uniform - uniform thickness layers evenly distributed</span>
<span id="L519">                                !       between the surface and MAXIMUM_DEPTH.</span>
<span id="L520">                                !     list - read a list of positive interface depths.</span>
<span id="L521">                                !     param - use thicknesses from parameter THICKNESS_INIT_VALUES.</span>
<span id="L522">                                !     DOME - use a slope and channel configuration for the</span>
<span id="L523">                                !       DOME sill-overflow test case.</span>
<span id="L524">                                !     ISOMIP - use a configuration for the</span>
<span id="L525">                                !       ISOMIP test case.</span>
<span id="L526">                                !     benchmark - use the benchmark test case thicknesses.</span>
<span id="L527">                                !     Neverworld - use the Neverworld test case thicknesses.</span>
<span id="L528">                                !     search - search a density profile for the interface</span>
<span id="L529">                                !       densities. This is not yet implemented.</span>
<span id="L530">                                !     circle_obcs - the circle_obcs test case is used.</span>
<span id="L531">                                !     DOME2D - 2D version of DOME initialization.</span>
<span id="L532">                                !     adjustment2d - 2D lock exchange thickness ICs.</span>
<span id="L533">                                !     sloshing - sloshing gravity thickness ICs.</span>
<span id="L534">                                !     seamount - no motion test with seamount ICs.</span>
<span id="L535">                                !     dumbbell - sloshing channel ICs.</span>
<span id="L536">                                !     soliton - Equatorial Rossby soliton.</span>
<span id="L537">                                !     rossby_front - a mixed layer front in thermal wind balance.</span>
<span id="L538">                                !     USER - call a user modified routine.</span>
<span id="L539">THICKNESS_FILE = &quot;GOLD_IC.2010.11.15.nc&quot; !</span>
<span id="L540">                                ! The name of the thickness file.</span>
<span id="L541">ADJUST_THICKNESS = True         !   [Boolean] default = False</span>
<span id="L542">                                ! If true, all mass below the bottom removed if the topography is shallower than</span>
<span id="L543">                                ! the thickness input file would indicate.</span>
<span id="L544">THICKNESS_TOLERANCE = 0.1       !   [m] default = 0.1</span>
<span id="L545">                                ! A parameter that controls the tolerance when adjusting the thickness to fit</span>
<span id="L546">                                ! the bathymetry. Used when ADJUST_THICKNESS=True.</span>
<span id="L547">INTERFACE_IC_VAR = &quot;eta&quot;        ! default = &quot;eta&quot;</span>
<span id="L548">                                ! The variable name for initial conditions for interface heights relative to</span>
<span id="L549">                                ! mean sea level, positive upward unless otherwise rescaled.</span>
<span id="L550">INTERFACE_IC_RESCALE = 1.0      !   [various] default = 1.0</span>
<span id="L551">                                ! A factor by which to rescale the initial interface heights to convert them to</span>
<span id="L552">                                ! units of m or correct sign conventions to positive upward.</span>
<span id="L553">TS_CONFIG = &quot;file&quot;              !</span>
<span id="L554">                                ! A string that determines how the initial temperatures and salinities are</span>
<span id="L555">                                ! specified for a new run:</span>
<span id="L556">                                !     file - read velocities from the file specified</span>
<span id="L557">                                !       by (TS_FILE).</span>
<span id="L558">                                !     fit - find the temperatures that are consistent with</span>
<span id="L559">                                !       the layer densities and salinity S_REF.</span>
<span id="L560">                                !     TS_profile - use temperature and salinity profiles</span>
<span id="L561">                                !       (read from TS_FILE) to set layer densities.</span>
<span id="L562">                                !     benchmark - use the benchmark test case T &amp; S.</span>
<span id="L563">                                !     linear - linear in logical layer space.</span>
<span id="L564">                                !     DOME2D - 2D DOME initialization.</span>
<span id="L565">                                !     ISOMIP - ISOMIP initialization.</span>
<span id="L566">                                !     adjustment2d - 2d lock exchange T/S ICs.</span>
<span id="L567">                                !     sloshing - sloshing mode T/S ICs.</span>
<span id="L568">                                !     seamount - no motion test with seamount ICs.</span>
<span id="L569">                                !     dumbbell - sloshing channel ICs.</span>
<span id="L570">                                !     rossby_front - a mixed layer front in thermal wind balance.</span>
<span id="L571">                                !     SCM_CVMix_tests - used in the SCM CVMix tests.</span>
<span id="L572">                                !     USER - call a user modified routine.</span>
<span id="L573">TS_FILE = &quot;GOLD_IC.2010.11.15.nc&quot; !</span>
<span id="L574">                                ! The initial condition file for temperature.</span>
<span id="L575">TEMP_IC_VAR = &quot;PTEMP&quot;           ! default = &quot;PTEMP&quot;</span>
<span id="L576">                                ! The initial condition variable for potential temperature.</span>
<span id="L577">SALT_IC_VAR = &quot;SALT&quot;            ! default = &quot;SALT&quot;</span>
<span id="L578">                                ! The initial condition variable for salinity.</span>
<span id="L579">SALT_FILE = &quot;GOLD_IC.2010.11.15.nc&quot; ! default = &quot;GOLD_IC.2010.11.15.nc&quot;</span>
<span id="L580">                                ! The initial condition file for salinity.</span>
<span id="L581">DEPRESS_INITIAL_SURFACE = False !   [Boolean] default = False</span>
<span id="L582">                                ! If true,  depress the initial surface to avoid huge tsunamis when a large</span>
<span id="L583">                                ! surface pressure is applied.</span>
<span id="L584">TRIM_IC_FOR_P_SURF = False      !   [Boolean] default = False</span>
<span id="L585">                                ! If true, cuts way the top of the column for initial conditions at the depth</span>
<span id="L586">                                ! where the hydrostatic pressure matches the imposed surface pressure which is</span>
<span id="L587">                                ! read from file.</span>
<span id="L588">VELOCITY_CONFIG = &quot;zero&quot;        ! default = &quot;zero&quot;</span>
<span id="L589">                                ! A string that determines how the initial velocities are specified for a new</span>
<span id="L590">                                ! run:</span>
<span id="L591">                                !     file - read velocities from the file specified</span>
<span id="L592">                                !       by (VELOCITY_FILE).</span>
<span id="L593">                                !     zero - the fluid is initially at rest.</span>
<span id="L594">                                !     uniform - the flow is uniform (determined by</span>
<span id="L595">                                !       parameters INITIAL_U_CONST and INITIAL_V_CONST).</span>
<span id="L596">                                !     rossby_front - a mixed layer front in thermal wind balance.</span>
<span id="L597">                                !     soliton - Equatorial Rossby soliton.</span>
<span id="L598">                                !     USER - call a user modified routine.</span>
<span id="L599">ODA_INCUPD = False              !   [Boolean] default = False</span>
<span id="L600">                                ! If true, oda incremental updates will be applied everywhere in the domain.</span>
<span id="L601">SPONGE = False                  !   [Boolean] default = False</span>
<span id="L602">                                ! If true, sponges may be applied anywhere in the domain. The exact location and</span>
<span id="L603">                                ! properties of those sponges are specified via SPONGE_CONFIG.</span>
<span id="L604"></span>
<span id="L605">! === module MOM_diag_mediator ===</span>
<span id="L606">NUM_DIAG_COORDS = 1             ! default = 1</span>
<span id="L607">                                ! The number of diagnostic vertical coordinates to use. For each coordinate, an</span>
<span id="L608">                                ! entry in DIAG_COORDS must be provided.</span>
<span id="L609">DIAG_REMAPPING_USE_OM4_SUBCELLS = True !   [Boolean] default = True</span>
<span id="L610">                                ! If true, use the OM4 remapping-via-subcells algorithm for diagnostics. See</span>
<span id="L611">                                ! REMAPPING_USE_OM4_SUBCELLS for details. We recommend setting this option to</span>
<span id="L612">                                ! false.</span>
<span id="L613">USE_INDEX_DIAGNOSTIC_AXES = False !   [Boolean] default = False</span>
<span id="L614">                                ! If true, use a grid index coordinate convention for diagnostic axes.</span>
<span id="L615">DIAG_COORDS = &quot;z Z ZSTAR&quot;       ! default = &quot;z Z ZSTAR&quot;</span>
<span id="L616">                                ! A list of string tuples associating diag_table modules to a coordinate</span>
<span id="L617">                                ! definition used for diagnostics. Each string is of the form &quot;MODULE_SUFFIX</span>
<span id="L618">                                ! PARAMETER_SUFFIX COORDINATE_NAME&quot;.</span>
<span id="L619">DIAG_MISVAL = 1.0E+20           !   [various] default = 1.0E+20</span>
<span id="L620">                                ! Set the default missing value to use for diagnostics.</span>
<span id="L621">DIAG_AS_CHKSUM = False          !   [Boolean] default = False</span>
<span id="L622">                                ! Instead of writing diagnostics to the diag manager, write a text file</span>
<span id="L623">                                ! containing the checksum (bitcount) of the array.</span>
<span id="L624">AVAILABLE_DIAGS_FILE = &quot;available_diags.000000&quot; ! default = &quot;available_diags.000000&quot;</span>
<span id="L625">                                ! A file into which to write a list of all available ocean diagnostics that can</span>
<span id="L626">                                ! be included in a diag_table.</span>
<span id="L627">DIAG_COORD_DEF_Z = &quot;WOA09&quot;      ! default = &quot;WOA09&quot;</span>
<span id="L628">                                ! Determines how to specify the coordinate resolution. Valid options are:</span>
<span id="L629">                                !  PARAM       - use the vector-parameter DIAG_COORD_RES_Z</span>
<span id="L630">                                !  UNIFORM[:N] - uniformly distributed</span>
<span id="L631">                                !  FILE:string - read from a file. The string specifies</span>
<span id="L632">                                !                the filename and variable name, separated</span>
<span id="L633">                                !                by a comma or space, e.g. FILE:lev.nc,dz</span>
<span id="L634">                                !                or FILE:lev.nc,interfaces=zw</span>
<span id="L635">                                !  WOA09[:N]   - the WOA09 vertical grid (approximately)</span>
<span id="L636">                                !  WOA09INT[:N] - layers spanned by the WOA09 depths</span>
<span id="L637">                                !  WOA23INT[:N] - layers spanned by the WOA23 depths</span>
<span id="L638">                                !  FNC1:string - FNC1:dz_min,H_total,power,precision</span>
<span id="L639">                                !  HYBRID:string - read from a file. The string specifies</span>
<span id="L640">                                !                the filename and two variable names, separated</span>
<span id="L641">                                !                by a comma or space, for sigma-2 and dz.</span>
<span id="L642">                                !                e.g. HYBRID:vgrid.nc,sigma2,dz</span>
<span id="L643">                                !  HYBRID_3D:string - read from a file. The string specifies</span>
<span id="L644">                                !                the filename and two 3D variable names, separated</span>
<span id="L645">                                !                by a comma or space, for sigma-2 and dz. The</span>
<span id="L646">                                !                latter can be FNC1:string which is used everywhere.</span>
<span id="L647">                                !                e.g. HYBRID_3D:vgrid.nc,sigma2,dz</span>
<span id="L648">                                !  HYBRID_MAP:string - read from a file. The string specifies</span>
<span id="L649">                                !                the filename and three variable names, separated</span>
<span id="L650">                                !                by a comma or space, for map, sigma-2 and dz.</span>
<span id="L651">                                !                Map is a spatial index array with, maxval(map)=N,</span>
<span id="L652">                                !                and the others are 2D arrays containing N profiles.</span>
<span id="L653">                                !                Map typically contains integer values, but it can</span>
<span id="L654">                                !                contain real values, I+w, which imply using</span>
<span id="L655">                                !                the weighted sum of profiles I and I+1.</span>
<span id="L656">                                !                Dz can be FNC1:string which is used everywhere.</span>
<span id="L657">                                !                e.g. HYBRID_MAP:vgrid.nc,map,sigma2,dz</span>
<span id="L658"></span>
<span id="L659">! === module MOM_MEKE ===</span>
<span id="L660">USE_MEKE = False                !   [Boolean] default = False</span>
<span id="L661">                                ! If true, turns on the MEKE scheme which calculates a sub-grid mesoscale eddy</span>
<span id="L662">                                ! kinetic energy budget.</span>
<span id="L663"></span>
<span id="L664">! === module MOM_lateral_mixing_coeffs ===</span>
<span id="L665">USE_VARIABLE_MIXING = True      !   [Boolean] default = False</span>
<span id="L666">                                ! If true, the variable mixing code will be called.  This allows diagnostics to</span>
<span id="L667">                                ! be created even if the scheme is not used.  If KHTR_SLOPE_CFF&gt;0 or</span>
<span id="L668">                                ! KhTh_Slope_Cff&gt;0, this is set to true regardless of what is in the parameter</span>
<span id="L669">                                ! file.</span>
<span id="L670">USE_VISBECK = True              !   [Boolean] default = False</span>
<span id="L671">                                ! If true, use the Visbeck et al. (1997) formulation for</span>
<span id="L672">                                ! thickness diffusivity.</span>
<span id="L673">RESOLN_SCALED_KH = True         !   [Boolean] default = False</span>
<span id="L674">                                ! If true, the Laplacian lateral viscosity is scaled away when the first</span>
<span id="L675">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L676">DEPTH_SCALED_KHTH = False       !   [Boolean] default = False</span>
<span id="L677">                                ! If true, KHTH is scaled away when the depth is shallowerthan a reference</span>
<span id="L678">                                ! depth: KHTH = MIN(1,H/H0)**N * KHTH, where H0 is a reference depth, controlled</span>
<span id="L679">                                ! via DEPTH_SCALED_KHTH_H0, and the exponent (N) is controlled via</span>
<span id="L680">                                ! DEPTH_SCALED_KHTH_EXP.</span>
<span id="L681">RESOLN_SCALED_KHTH = True       !   [Boolean] default = False</span>
<span id="L682">                                ! If true, the interface depth diffusivity is scaled away when the first</span>
<span id="L683">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L684">RESOLN_SCALED_KHTR = False      !   [Boolean] default = False</span>
<span id="L685">                                ! If true, the epipycnal tracer diffusivity is scaled away when the first</span>
<span id="L686">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L687">RESOLN_USE_EBT = False          !   [Boolean] default = False</span>
<span id="L688">                                ! If true, uses the equivalent barotropic wave speed instead of first baroclinic</span>
<span id="L689">                                ! wave for calculating the resolution fn.</span>
<span id="L690">BACKSCAT_EBT_POWER = 0.0        !   [nondim] default = 0.0</span>
<span id="L691">                                ! Power to raise EBT vertical structure to when backscatter has vertical</span>
<span id="L692">                                ! structure.</span>
<span id="L693">BS_USE_SQG_STRUCT = False       !   [Boolean] default = False</span>
<span id="L694">                                ! If true, the SQG vertical structure is used for backscatter on the condition</span>
<span id="L695">                                ! that BS_EBT_power=0</span>
<span id="L696">KHTH_USE_EBT_STRUCT = False     !   [Boolean] default = False</span>
<span id="L697">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L698">                                ! thickness diffusivity.</span>
<span id="L699">KHTH_USE_SQG_STRUCT = False     !   [Boolean] default = False</span>
<span id="L700">                                ! If true, uses the surface quasigeostrophic structure as the vertical structure</span>
<span id="L701">                                ! of thickness diffusivity.</span>
<span id="L702">KHTR_USE_EBT_STRUCT = False     !   [Boolean] default = False</span>
<span id="L703">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L704">                                ! tracer diffusivity.</span>
<span id="L705">KHTR_USE_SQG_STRUCT = False     !   [Boolean] default = False</span>
<span id="L706">                                ! If true, uses the surface quasigeostrophic structure as the vertical structure</span>
<span id="L707">                                ! of tracer diffusivity.</span>
<span id="L708">KD_GL90_USE_EBT_STRUCT = False  !   [Boolean] default = False</span>
<span id="L709">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L710">                                ! diffusivity in the GL90 scheme.</span>
<span id="L711">KD_GL90_USE_SQG_STRUCT = False  !   [Boolean] default = False</span>
<span id="L712">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L713">                                ! diffusivity in the GL90 scheme.</span>
<span id="L714">KHTH_SLOPE_CFF = 0.25           !   [nondim] default = 0.0</span>
<span id="L715">                                ! The nondimensional coefficient in the Visbeck formula for the interface depth</span>
<span id="L716">                                ! diffusivity</span>
<span id="L717">KHTR_SLOPE_CFF = 0.25           !   [nondim] default = 0.0</span>
<span id="L718">                                ! The nondimensional coefficient in the Visbeck formula for the epipycnal tracer</span>
<span id="L719">                                ! diffusivity</span>
<span id="L720">USE_STORED_SLOPES = False       !   [Boolean] default = False</span>
<span id="L721">                                ! If true, the isopycnal slopes are calculated once and stored for re-use. This</span>
<span id="L722">                                ! uses more memory but avoids calling the equation of state more times than</span>
<span id="L723">                                ! should be necessary.</span>
<span id="L724">VERY_SMALL_FREQUENCY = 1.0E-17  !   [s-1] default = 1.0E-17</span>
<span id="L725">                                ! A miniscule frequency that is used to avoid division by 0.  The default value</span>
<span id="L726">                                ! is roughly (pi / (the age of the universe)).</span>
<span id="L727">USE_STANLEY_ISO = False         !   [Boolean] default = False</span>
<span id="L728">                                ! If true, turn on Stanley SGS T variance parameterization in isopycnal slope</span>
<span id="L729">                                ! code.</span>
<span id="L730">KD_SMOOTH = 1.0E-06             !   [m2 s-1] default = 1.0E-06</span>
<span id="L731">                                ! A diapycnal diffusivity that is used to interpolate more sensible values of T</span>
<span id="L732">                                ! &amp; S into thin layers.</span>
<span id="L733">USE_SIMPLER_EADY_GROWTH_RATE = False !   [Boolean] default = False</span>
<span id="L734">                                ! If true, use a simpler method to calculate the Eady growth rate that avoids</span>
<span id="L735">                                ! division by layer thickness. Recommended.</span>
<span id="L736">VARMIX_KTOP = 6                 !   [nondim] default = 2</span>
<span id="L737">                                ! The layer number at which to start vertical integration of S*N for purposes of</span>
<span id="L738">                                ! finding the Eady growth rate.</span>
<span id="L739">MIN_DZ_FOR_SLOPE_N2 = 1.0       !   [m] default = 1.0</span>
<span id="L740">                                ! The minimum vertical distance to use in the denominator of the bouyancy</span>
<span id="L741">                                ! frequency used in the slope calculation.</span>
<span id="L742">FULL_DEPTH_EADY_GROWTH_RATE = False !   [Boolean] default = False</span>
<span id="L743">                                ! If true, calculate the Eady growth rate based on average slope times</span>
<span id="L744">                                ! stratification that includes contributions from sea-level changes in its</span>
<span id="L745">                                ! denominator, rather than just the nominal depth of the bathymetry.  This only</span>
<span id="L746">                                ! applies when using the model interface heights as a proxy for isopycnal</span>
<span id="L747">                                ! slopes.</span>
<span id="L748">VISBECK_L_SCALE = 3.0E+04       !   [m or nondim] default = 0.0</span>
<span id="L749">                                ! The fixed length scale in the Visbeck formula, or if negative a nondimensional</span>
<span id="L750">                                ! scaling factor relating this length scale squared to the cell areas.</span>
<span id="L751">KH_RES_SCALE_COEF = 1.0         !   [nondim] default = 1.0</span>
<span id="L752">                                ! A coefficient that determines how KhTh is scaled away if RESOLN_SCALED_... is</span>
<span id="L753">                                ! true, as F = 1 / (1 + (KH_RES_SCALE_COEF*Rd/dx)^KH_RES_FN_POWER).</span>
<span id="L754">KH_RES_FN_POWER = 2             ! default = 2</span>
<span id="L755">                                ! The power of dx/Ld in the Kh resolution function.  Any positive integer may be</span>
<span id="L756">                                ! used, although even integers are more efficient to calculate.  Setting this</span>
<span id="L757">                                ! greater than 100 results in a step-function being used.</span>
<span id="L758">VISC_RES_SCALE_COEF = 1.0       !   [nondim] default = 1.0</span>
<span id="L759">                                ! A coefficient that determines how Kh is scaled away if RESOLN_SCALED_... is</span>
<span id="L760">                                ! true, as F = 1 / (1 + (KH_RES_SCALE_COEF*Rd/dx)^KH_RES_FN_POWER). This</span>
<span id="L761">                                ! function affects lateral viscosity, Kh, and not KhTh.</span>
<span id="L762">VISC_RES_FN_POWER = 2           ! default = 2</span>
<span id="L763">                                ! The power of dx/Ld in the Kh resolution function.  Any positive integer may be</span>
<span id="L764">                                ! used, although even integers are more efficient to calculate.  Setting this</span>
<span id="L765">                                ! greater than 100 results in a step-function being used. This function affects</span>
<span id="L766">                                ! lateral viscosity, Kh, and not KhTh.</span>
<span id="L767">INTERPOLATE_RES_FN = False      !   [Boolean] default = False</span>
<span id="L768">                                ! If true, interpolate the resolution function to the velocity points from the</span>
<span id="L769">                                ! thickness points; otherwise interpolate the wave speed and calculate the</span>
<span id="L770">                                ! resolution function independently at each point.</span>
<span id="L771">GILL_EQUATORIAL_LD = True       !   [Boolean] default = True</span>
<span id="L772">                                ! If true, uses Gill&#x27;s definition of the baroclinic equatorial deformation</span>
<span id="L773">                                ! radius, otherwise, if false, use Pedlosky&#x27;s definition. These definitions</span>
<span id="L774">                                ! differ by a factor of 2 in front of the beta term in the denominator. Gill&#x27;s</span>
<span id="L775">                                ! is the more appropriate definition.</span>
<span id="L776">INTERNAL_WAVE_SPEED_TOL = 0.001 !   [nondim] default = 0.001</span>
<span id="L777">                                ! The fractional tolerance for finding the wave speeds.</span>
<span id="L778">INTERNAL_WAVE_SPEED_MIN = 0.0   !   [m s-1] default = 0.0</span>
<span id="L779">                                ! A floor in the first mode speed below which 0 used instead.</span>
<span id="L780">INTERNAL_WAVE_SPEED_BETTER_EST = False !   [Boolean] default = True</span>
<span id="L781">                                ! If true, use a more robust estimate of the first mode wave speed as the</span>
<span id="L782">                                ! starting point for iterations.</span>
<span id="L783">EBT_REMAPPING_USE_OM4_SUBCELLS = True !   [Boolean] default = True</span>
<span id="L784">                                ! If true, use the OM4 remapping-via-subcells algorithm for calculating EBT</span>
<span id="L785">                                ! structure. See REMAPPING_USE_OM4_SUBCELLS for details. We recommend setting</span>
<span id="L786">                                ! this option to false.</span>
<span id="L787">USE_QG_LEITH_GM = False         !   [Boolean] default = False</span>
<span id="L788">                                ! If true, use the QG Leith viscosity as the GM coefficient.</span>
<span id="L789"></span>
<span id="L790">! === module MOM_set_visc ===</span>
<span id="L791">BOTTOMDRAGLAW = True            !   [Boolean] default = True</span>
<span id="L792">                                ! If true, the bottom stress is calculated with a drag law of the form</span>
<span id="L793">                                ! c_drag*|u|*u. The velocity magnitude may be an assumed value or it may be</span>
<span id="L794">                                ! based on the actual velocity in the bottommost HBBL, depending on LINEAR_DRAG.</span>
<span id="L795">DRAG_AS_BODY_FORCE = False      !   [Boolean] default = False</span>
<span id="L796">                                ! If true, the bottom stress is imposed as an explicit body force applied over a</span>
<span id="L797">                                ! fixed distance from the bottom, rather than as an implicit calculation based</span>
<span id="L798">                                ! on an enhanced near-bottom viscosity. The thickness of the bottom boundary</span>
<span id="L799">                                ! layer is HBBL.</span>
<span id="L800">CHANNEL_DRAG = True             !   [Boolean] default = False</span>
<span id="L801">                                ! If true, the bottom drag is exerted directly on each layer proportional to the</span>
<span id="L802">                                ! fraction of the bottom it overlies.</span>
<span id="L803">LINEAR_DRAG = False             !   [Boolean] default = False</span>
<span id="L804">                                ! If LINEAR_DRAG and BOTTOMDRAGLAW are defined the drag law is</span>
<span id="L805">                                ! cdrag*DRAG_BG_VEL*u.</span>
<span id="L806">DYNAMIC_VISCOUS_ML = True       !   [Boolean] default = False</span>
<span id="L807">                                ! If true, use a bulk Richardson number criterion to determine the mixed layer</span>
<span id="L808">                                ! thickness for viscosity.</span>
<span id="L809">BULK_RI_ML_VISC = 0.05          !   [nondim] default = 0.05</span>
<span id="L810">                                ! The efficiency with which mean kinetic energy released by mechanically forced</span>
<span id="L811">                                ! entrainment of the mixed layer is converted to turbulent kinetic energy.  By</span>
<span id="L812">                                ! default, BULK_RI_ML_VISC = BULK_RI_ML or 0.</span>
<span id="L813">TKE_DECAY_VISC = 10.0           !   [nondim] default = 10.0</span>
<span id="L814">                                ! TKE_DECAY_VISC relates the vertical rate of decay of the TKE available for</span>
<span id="L815">                                ! mechanical entrainment to the natural Ekman depth for use in calculating the</span>
<span id="L816">                                ! dynamic mixed layer viscosity.  By default, TKE_DECAY_VISC = TKE_DECAY or 0.</span>
<span id="L817">ML_OMEGA_FRAC = 1.0             !   [nondim] default = 0.0</span>
<span id="L818">                                ! When setting the decay scale for turbulence, use this fraction of the absolute</span>
<span id="L819">                                ! rotation rate blended with the local value of f, as sqrt((1-of)*f^2 +</span>
<span id="L820">                                ! of*4*omega^2).</span>
<span id="L821">HBBL = 10.0                     !   [m]</span>
<span id="L822">                                ! The thickness of a bottom boundary layer with a viscosity increased by</span>
<span id="L823">                                ! KV_EXTRA_BBL if BOTTOMDRAGLAW is not defined, or the thickness over which</span>
<span id="L824">                                ! near-bottom velocities are averaged for the drag law if BOTTOMDRAGLAW is</span>
<span id="L825">                                ! defined but LINEAR_DRAG is not.</span>
<span id="L826">CDRAG = 0.003                   !   [nondim] default = 0.003</span>
<span id="L827">                                ! CDRAG is the drag coefficient relating the magnitude of the velocity field to</span>
<span id="L828">                                ! the bottom stress. CDRAG is only used if BOTTOMDRAGLAW is defined.</span>
<span id="L829">BBL_USE_TIDAL_BG = False        !   [Boolean] default = False</span>
<span id="L830">                                ! Flag to use the tidal RMS amplitude in place of constant background velocity</span>
<span id="L831">                                ! for computing u* in the BBL. This flag is only used when BOTTOMDRAGLAW is true</span>
<span id="L832">                                ! and LINEAR_DRAG is false.</span>
<span id="L833">DRAG_BG_VEL = 0.1               !   [m s-1] default = 0.0</span>
<span id="L834">                                ! DRAG_BG_VEL is either the assumed bottom velocity (with LINEAR_DRAG) or an</span>
<span id="L835">                                ! unresolved  velocity that is combined with the resolved velocity to estimate</span>
<span id="L836">                                ! the velocity magnitude.  DRAG_BG_VEL is only used when BOTTOMDRAGLAW is</span>
<span id="L837">                                ! defined.</span>
<span id="L838">BBL_USE_EOS = False             !   [Boolean] default = True</span>
<span id="L839">                                ! If true, use the equation of state in determining the properties of the bottom</span>
<span id="L840">                                ! boundary layer.  Otherwise use the layer target potential densities.  The</span>
<span id="L841">                                ! default of this parameter is the value of USE_EOS.</span>
<span id="L842">BBL_THICK_MIN = 0.1             !   [m] default = 0.0</span>
<span id="L843">                                ! The minimum bottom boundary layer thickness that can be used with</span>
<span id="L844">                                ! BOTTOMDRAGLAW. This might be Kv/(cdrag*drag_bg_vel) to give Kv as the minimum</span>
<span id="L845">                                ! near-bottom viscosity.</span>
<span id="L846">HTBL_SHELF_MIN = 0.1            !   [m] default = 0.1</span>
<span id="L847">                                ! The minimum top boundary layer thickness that can be used with BOTTOMDRAGLAW.</span>
<span id="L848">                                ! This might be Kv/(cdrag*drag_bg_vel) to give Kv as the minimum near-top</span>
<span id="L849">                                ! viscosity.</span>
<span id="L850">HTBL_SHELF = 10.0               !   [m] default = 10.0</span>
<span id="L851">                                ! The thickness over which near-surface velocities are averaged for the drag law</span>
<span id="L852">                                ! under an ice shelf.  By default this is the same as HBBL</span>
<span id="L853">KV = 1.0E-04                    !   [m2 s-1]</span>
<span id="L854">                                ! The background kinematic viscosity in the interior. The molecular value, ~1e-6</span>
<span id="L855">                                ! m2 s-1, may be used.</span>
<span id="L856">KV_BBL_MIN = 1.0E-04            !   [m2 s-1] default = 1.0E-04</span>
<span id="L857">                                ! The minimum viscosities in the bottom boundary layer.</span>
<span id="L858">KV_TBL_MIN = 1.0E-04            !   [m2 s-1] default = 1.0E-04</span>
<span id="L859">                                ! The minimum viscosities in the top boundary layer.</span>
<span id="L860">CORRECT_BBL_BOUNDS = False      !   [Boolean] default = False</span>
<span id="L861">                                ! If true, uses the correct bounds on the BBL thickness and viscosity so that</span>
<span id="L862">                                ! the bottom layer feels the intended drag.</span>
<span id="L863">SMAG_CONST_CHANNEL = 0.15       !   [nondim] default = 0.15</span>
<span id="L864">                                ! The nondimensional Laplacian Smagorinsky constant used in calculating the</span>
<span id="L865">                                ! channel drag if it is enabled.  The default is to use the same value as</span>
<span id="L866">                                ! SMAG_LAP_CONST if it is defined, or 0.15 if it is not. The value used is also</span>
<span id="L867">                                ! 0.15 if the specified value is negative.</span>
<span id="L868">TRIG_CHANNEL_DRAG_WIDTHS = True !   [Boolean] default = True</span>
<span id="L869">                                ! If true, use trigonometric expressions to determine the fractional open</span>
<span id="L870">                                ! interface lengths for concave topography.</span>
<span id="L871">CHANNEL_DRAG_MAX_BBL_THICK = 5.0 !   [m] default = 5.0</span>
<span id="L872">                                ! The maximum bottom boundary layer thickness over which the channel drag is</span>
<span id="L873">                                ! exerted, or a negative value for no fixed limit, instead basing the BBL</span>
<span id="L874">                                ! thickness on the bottom stress, rotation and stratification.  The default is</span>
<span id="L875">                                ! proportional to HBBL if USE_JACKSON_PARAM or DRAG_AS_BODY_FORCE is true.</span>
<span id="L876"></span>
<span id="L877">! === module MOM_thickness_diffuse ===</span>
<span id="L878">KHTH = 10.0                     !   [m2 s-1] default = 0.0</span>
<span id="L879">                                ! The background horizontal thickness diffusivity.</span>
<span id="L880">READ_KHTH = False               !   [Boolean] default = False</span>
<span id="L881">                                ! If true, read a file (given by KHTH_FILE) containing the spatially varying</span>
<span id="L882">                                ! horizontal isopycnal height diffusivity.</span>
<span id="L883">KHTH_MIN = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L884">                                ! The minimum horizontal thickness diffusivity.</span>
<span id="L885">KHTH_MAX = 900.0                !   [m2 s-1] default = 0.0</span>
<span id="L886">                                ! The maximum horizontal thickness diffusivity.</span>
<span id="L887">KHTH_MAX_CFL = 0.8              !   [nondimensional] default = 0.8</span>
<span id="L888">                                ! The maximum value of the local diffusive CFL ratio that is permitted for the</span>
<span id="L889">                                ! thickness diffusivity. 1.0 is the marginally unstable value in a pure layered</span>
<span id="L890">                                ! model, but much smaller numbers (e.g. 0.1) seem to work better for ALE-based</span>
<span id="L891">                                ! models.</span>
<span id="L892">KH_ETA_CONST = 0.0              !   [m2 s-1] default = 0.0</span>
<span id="L893">                                ! The background horizontal diffusivity of the interface heights (without</span>
<span id="L894">                                ! considering the layer density structure).  If diffusive CFL limits are</span>
<span id="L895">                                ! encountered, the diffusivities of the isopycnals and the interfaces heights</span>
<span id="L896">                                ! are scaled back proportionately.</span>
<span id="L897">KH_ETA_VEL_SCALE = 0.0          !   [m s-1] default = 0.0</span>
<span id="L898">                                ! A velocity scale that is multiplied by the grid spacing to give a contribution</span>
<span id="L899">                                ! to the horizontal diffusivity of the interface heights (without considering</span>
<span id="L900">                                ! the layer density structure).</span>
<span id="L901">DETANGLE_INTERFACES = False     !   [Boolean] default = False</span>
<span id="L902">                                ! If defined add 3-d structured enhanced interface height diffusivities to</span>
<span id="L903">                                ! horizontally smooth jagged layers.</span>
<span id="L904">KHTH_SLOPE_MAX = 0.01           !   [nondim] default = 0.01</span>
<span id="L905">                                ! A slope beyond which the calculated isopycnal slope is not reliable and is</span>
<span id="L906">                                ! scaled away.</span>
<span id="L907">KHTH_USE_FGNV_STREAMFUNCTION = False !   [Boolean] default = False</span>
<span id="L908">                                ! If true, use the streamfunction formulation of Ferrari et al., 2010, which</span>
<span id="L909">                                ! effectively emphasizes graver vertical modes by smoothing in the vertical.</span>
<span id="L910">USE_STANLEY_GM = False          !   [Boolean] default = False</span>
<span id="L911">                                ! If true, turn on Stanley SGS T variance parameterization in GM code.</span>
<span id="L912">MEKE_GM_SRC_ALT = False         !   [Boolean] default = False</span>
<span id="L913">                                ! If true, use the GM energy conversion form S^2*N^2*kappa rather than the</span>
<span id="L914">                                ! streamfunction for the GM source term.</span>
<span id="L915">MEKE_GEOMETRIC = False          !   [Boolean] default = False</span>
<span id="L916">                                ! If true, uses the GM coefficient formulation from the GEOMETRIC framework</span>
<span id="L917">                                ! (Marshall et al., 2012).</span>
<span id="L918">USE_GME = False                 !   [Boolean] default = False</span>
<span id="L919">                                ! If true, use the GM+E backscatter scheme in association with the Gent and</span>
<span id="L920">                                ! McWilliams parameterization.</span>
<span id="L921">USE_GM_WORK_BUG = False         !   [Boolean] default = False</span>
<span id="L922">                                ! If true, compute the top-layer work tendency on the u-grid with the incorrect</span>
<span id="L923">                                ! sign, for legacy reproducibility.</span>
<span id="L924">STOCH_EOS = False               !   [Boolean] default = False</span>
<span id="L925">                                ! If true, stochastic perturbations are applied to the EOS in the PGF.</span>
<span id="L926">STANLEY_COEFF = -1.0            !   [nondim] default = -1.0</span>
<span id="L927">                                ! Coefficient correlating the temperature gradient and SGS T variance.</span>
<span id="L928"></span>
<span id="L929">! === module MOM_dynamics_split_RK2 ===</span>
<span id="L930">TIDES = True                    !   [Boolean] default = False</span>
<span id="L931">                                ! If true, apply tidal momentum forcing.</span>
<span id="L932">CALCULATE_SAL = True            !   [Boolean] default = True</span>
<span id="L933">                                ! If true, calculate self-attraction and loading.</span>
<span id="L934">USE_HA = False                  !   [Boolean] default = False</span>
<span id="L935">                                ! If true, perform inline harmonic analysis.</span>
<span id="L936">BE = 0.6                        !   [nondim] default = 0.6</span>
<span id="L937">                                ! If SPLIT is true, BE determines the relative weighting of a  2nd-order</span>
<span id="L938">                                ! Runga-Kutta baroclinic time stepping scheme (0.5) and a backward Euler scheme</span>
<span id="L939">                                ! (1) that is used for the Coriolis and inertial terms.  BE may be from 0.5 to</span>
<span id="L940">                                ! 1, but instability may occur near 0.5. BE is also applicable if SPLIT is false</span>
<span id="L941">                                ! and USE_RK2 is true.</span>
<span id="L942">BEGW = 0.0                      !   [nondim] default = 0.0</span>
<span id="L943">                                ! If SPLIT is true, BEGW is a number from 0 to 1 that controls the extent to</span>
<span id="L944">                                ! which the treatment of gravity waves is forward-backward (0) or simulated</span>
<span id="L945">                                ! backward Euler (1).  0 is almost always used. If SPLIT is false and USE_RK2 is</span>
<span id="L946">                                ! true, BEGW can be between 0 and 0.5 to damp gravity waves.</span>
<span id="L947">SET_DTBT_USE_BT_CONT = False    !   [Boolean] default = False</span>
<span id="L948">                                ! If true, use BT_CONT to calculate DTBT if possible.</span>
<span id="L949">SPLIT_BOTTOM_STRESS = False     !   [Boolean] default = False</span>
<span id="L950">                                ! If true, provide the bottom stress calculated by the vertical viscosity to the</span>
<span id="L951">                                ! barotropic solver.</span>
<span id="L952">BT_USE_LAYER_FLUXES = True      !   [Boolean] default = True</span>
<span id="L953">                                ! If true, use the summed layered fluxes plus an adjustment due to the change in</span>
<span id="L954">                                ! the barotropic velocity in the barotropic continuity equation.</span>
<span id="L955">BT_ADJ_CORR_MASS_SRC = True     !   [Boolean] default = True</span>
<span id="L956">                                ! If true, recalculates the barotropic mass source after predictor step. This</span>
<span id="L957">                                ! should make little difference in the deep ocean but appears to help for</span>
<span id="L958">                                ! vanished layers. If false, uses the same mass source as from the predictor</span>
<span id="L959">                                ! step.</span>
<span id="L960">STORE_CORIOLIS_ACCEL = True     !   [Boolean] default = True</span>
<span id="L961">                                ! If true, calculate the Coriolis accelerations at the end of each timestep for</span>
<span id="L962">                                ! use in the predictor step of the next split RK2 timestep.</span>
<span id="L963">FPMIX = False                   !   [Boolean] default = False</span>
<span id="L964">                                ! If true, add non-local momentum flux increments and diffuse down the Eulerian</span>
<span id="L965">                                ! gradient.</span>
<span id="L966">VISC_REM_BUG = True             !   [Boolean] default = False</span>
<span id="L967">                                ! If true, visc_rem_[uv] in split mode is incorrectly calculated or accounted</span>
<span id="L968">                                ! for in two places. This parameter controls the defaults of two individual</span>
<span id="L969">                                ! flags, VISC_REM_TIMESTEP_BUG in MOM_dynamics_split_RK2(b) and</span>
<span id="L970">                                ! VISC_REM_BT_WEIGHT_BUG in MOM_barotropic.</span>
<span id="L971">VISC_REM_TIMESTEP_BUG = True    !   [Boolean] default = True</span>
<span id="L972">                                ! If true, recover a bug that uses dt_pred rather than dt in vertvisc_remnant()</span>
<span id="L973">                                ! at the end of predictor stage for the following continuity() and btstep()</span>
<span id="L974">                                ! calls in the corrector step. Default of this flag is set by VISC_REM_BUG</span>
<span id="L975"></span>
<span id="L976">! === module MOM_continuity_PPM ===</span>
<span id="L977">MONOTONIC_CONTINUITY = False    !   [Boolean] default = False</span>
<span id="L978">                                ! If true, CONTINUITY_PPM uses the Colella and Woodward monotonic limiter.  The</span>
<span id="L979">                                ! default (false) is to use a simple positive definite limiter.</span>
<span id="L980">SIMPLE_2ND_PPM_CONTINUITY = False !   [Boolean] default = False</span>
<span id="L981">                                ! If true, CONTINUITY_PPM uses a simple 2nd order (arithmetic mean)</span>
<span id="L982">                                ! interpolation of the edge values. This may give better PV conservation</span>
<span id="L983">                                ! properties. While it formally reduces the accuracy of the continuity solver</span>
<span id="L984">                                ! itself in the strongly advective limit, it does not reduce the overall order</span>
<span id="L985">                                ! of accuracy of the dynamic core.</span>
<span id="L986">UPWIND_1ST_CONTINUITY = False   !   [Boolean] default = False</span>
<span id="L987">                                ! If true, CONTINUITY_PPM becomes a 1st-order upwind continuity solver.  This</span>
<span id="L988">                                ! scheme is highly diffusive but may be useful for debugging or in single-column</span>
<span id="L989">                                ! mode where its minimal stencil is useful.</span>
<span id="L990">ETA_TOLERANCE = 1.0E-06         !   [m] default = 3.15E-09</span>
<span id="L991">                                ! The tolerance for the differences between the barotropic and baroclinic</span>
<span id="L992">                                ! estimates of the sea surface height due to the fluxes through each face.  The</span>
<span id="L993">                                ! total tolerance for SSH is 4 times this value.  The default is</span>
<span id="L994">                                ! 0.5*NK*ANGSTROM, and this should not be set less than about</span>
<span id="L995">                                ! 10^-15*MAXIMUM_DEPTH.</span>
<span id="L996">VELOCITY_TOLERANCE = 1.0E-04    !   [m s-1] default = 3.0E+08</span>
<span id="L997">                                ! The tolerance for barotropic velocity discrepancies between the barotropic</span>
<span id="L998">                                ! solution and  the sum of the layer thicknesses.</span>
<span id="L999">CONT_PPM_AGGRESS_ADJUST = False !   [Boolean] default = False</span>
<span id="L1000">                                ! If true, allow the adjusted velocities to have a relative CFL change up to</span>
<span id="L1001">                                ! 0.5.</span>
<span id="L1002">CONT_PPM_VOLUME_BASED_CFL = False !   [Boolean] default = False</span>
<span id="L1003">                                ! If true, use the ratio of the open face lengths to the tracer cell areas when</span>
<span id="L1004">                                ! estimating CFL numbers.  The default is set by CONT_PPM_AGGRESS_ADJUST.</span>
<span id="L1005">CONTINUITY_CFL_LIMIT = 0.5      !   [nondim] default = 0.5</span>
<span id="L1006">                                ! The maximum CFL of the adjusted velocities.</span>
<span id="L1007">CONT_PPM_BETTER_ITER = True     !   [Boolean] default = True</span>
<span id="L1008">                                ! If true, stop corrective iterations using a velocity based criterion and only</span>
<span id="L1009">                                ! stop if the iteration is better than all predecessors.</span>
<span id="L1010">CONT_PPM_USE_VISC_REM_MAX = True !   [Boolean] default = True</span>
<span id="L1011">                                ! If true, use more appropriate limiting bounds for corrections in strongly</span>
<span id="L1012">                                ! viscous columns.</span>
<span id="L1013">CONT_PPM_MARGINAL_FACE_AREAS = True !   [Boolean] default = True</span>
<span id="L1014">                                ! If true, use the marginal face areas from the continuity solver for use as the</span>
<span id="L1015">                                ! weights in the barotropic solver. Otherwise use the transport averaged areas.</span>
<span id="L1016"></span>
<span id="L1017">! === module MOM_CoriolisAdv ===</span>
<span id="L1018">NOSLIP = False                  !   [Boolean] default = False</span>
<span id="L1019">                                ! If true, no slip boundary conditions are used; otherwise free slip boundary</span>
<span id="L1020">                                ! conditions are assumed. The implementation of the free slip BCs on a C-grid is</span>
<span id="L1021">                                ! much cleaner than the no slip BCs. The use of free slip BCs is strongly</span>
<span id="L1022">                                ! encouraged, and no slip BCs are not used with the biharmonic viscosity.</span>
<span id="L1023">CORIOLIS_EN_DIS = False         !   [Boolean] default = False</span>
<span id="L1024">                                ! If true, two estimates of the thickness fluxes are used to estimate the</span>
<span id="L1025">                                ! Coriolis term, and the one that dissipates energy relative to the other one is</span>
<span id="L1026">                                ! used.</span>
<span id="L1027">CORIOLIS_SCHEME = &quot;SADOURNY75_ENERGY&quot; ! default = &quot;SADOURNY75_ENERGY&quot;</span>
<span id="L1028">                                ! CORIOLIS_SCHEME selects the discretization for the Coriolis terms. Valid</span>
<span id="L1029">                                ! values are:</span>
<span id="L1030">                                !    SADOURNY75_ENERGY - Sadourny, 1975; energy cons.</span>
<span id="L1031">                                !    ARAKAWA_HSU90     - Arakawa &amp; Hsu, 1990</span>
<span id="L1032">                                !    SADOURNY75_ENSTRO - Sadourny, 1975; enstrophy cons.</span>
<span id="L1033">                                !    ARAKAWA_LAMB81    - Arakawa &amp; Lamb, 1981; En. + Enst.</span>
<span id="L1034">                                !    ARAKAWA_LAMB_BLEND - A blend of Arakawa &amp; Lamb with</span>
<span id="L1035">                                !                         Arakawa &amp; Hsu and Sadourny energy</span>
<span id="L1036">                                !    WENOVI5TH_PV_ENSTRO   - 5th-order WENO PV enstrophy</span>
<span id="L1037">                                !    WENOVI3RD_PV_ENSTRO   - 3rd-order WENO PV enstrophy</span>
<span id="L1038">                                !    WENOVI7TH_PV_ENSTRO  - 7th-order WENO PV enstrophy</span>
<span id="L1039">BOUND_CORIOLIS = True           !   [Boolean] default = False</span>
<span id="L1040">                                ! If true, the Coriolis terms at u-points are bounded by the four estimates of</span>
<span id="L1041">                                ! (f+rv)v from the four neighboring v-points, and similarly at v-points.  This</span>
<span id="L1042">                                ! option would have no effect on the SADOURNY Coriolis scheme if it were</span>
<span id="L1043">                                ! possible to use centered difference thickness fluxes.</span>
<span id="L1044">KE_SCHEME = &quot;KE_ARAKAWA&quot;        ! default = &quot;KE_ARAKAWA&quot;</span>
<span id="L1045">                                ! KE_SCHEME selects the discretization for acceleration due to the kinetic</span>
<span id="L1046">                                ! energy gradient. Valid values are:</span>
<span id="L1047">                                !    KE_ARAKAWA, KE_SIMPLE_GUDONOV, KE_GUDONOV, KE_UP3</span>
<span id="L1048">PV_ADV_SCHEME = &quot;PV_ADV_CENTERED&quot; ! default = &quot;PV_ADV_CENTERED&quot;</span>
<span id="L1049">                                ! PV_ADV_SCHEME selects the discretization for PV advection. Valid values are:</span>
<span id="L1050">                                !    PV_ADV_CENTERED - centered (aka Sadourny, 75)</span>
<span id="L1051">                                !    PV_ADV_UPWIND1  - upwind, first order</span>
<span id="L1052"></span>
<span id="L1053">! === module MOM_self_attr_load ===</span>
<span id="L1054">SAL_USE_BPA = False             !   [Boolean] default = False</span>
<span id="L1055">                                ! If true, use bottom pressure anomaly to calculate self-attraction and loading</span>
<span id="L1056">                                ! (SAL). Otherwise sea surface height anomaly is used, which is only accurate</span>
<span id="L1057">                                ! for uniform density fluid.</span>
<span id="L1058">SAL_SCALAR_APPROX = True        !   [Boolean] default = True</span>
<span id="L1059">                                ! If true, use the scalar approximation to calculate self-attraction and</span>
<span id="L1060">                                ! loading.</span>
<span id="L1061">SAL_SCALAR_VALUE = 0.094        !   [m m-1] default = 0.0</span>
<span id="L1062">                                ! The constant of proportionality between self-attraction and loading (SAL)</span>
<span id="L1063">                                ! geopotential anomaly and barotropic geopotential anomaly. This is only used if</span>
<span id="L1064">                                ! SAL_SCALAR_APPROX is true or USE_PREVIOUS_TIDES is true.</span>
<span id="L1065">SAL_HARMONICS = False           !   [Boolean] default = False</span>
<span id="L1066">                                ! If true, use the online spherical harmonics method to calculate</span>
<span id="L1067">                                ! self-attraction and loading.</span>
<span id="L1068"></span>
<span id="L1069">! === module MOM_tidal_forcing ===</span>
<span id="L1070">TIDE_M2 = True                  !   [Boolean] default = False</span>
<span id="L1071">                                ! If true, apply tidal momentum forcing at the M2 frequency. This is only used</span>
<span id="L1072">                                ! if TIDES is true.</span>
<span id="L1073">TIDE_S2 = False                 !   [Boolean] default = False</span>
<span id="L1074">                                ! If true, apply tidal momentum forcing at the S2 frequency. This is only used</span>
<span id="L1075">                                ! if TIDES is true.</span>
<span id="L1076">TIDE_N2 = False                 !   [Boolean] default = False</span>
<span id="L1077">                                ! If true, apply tidal momentum forcing at the N2 frequency. This is only used</span>
<span id="L1078">                                ! if TIDES is true.</span>
<span id="L1079">TIDE_K2 = False                 !   [Boolean] default = False</span>
<span id="L1080">                                ! If true, apply tidal momentum forcing at the K2 frequency. This is only used</span>
<span id="L1081">                                ! if TIDES is true.</span>
<span id="L1082">TIDE_K1 = False                 !   [Boolean] default = False</span>
<span id="L1083">                                ! If true, apply tidal momentum forcing at the K1 frequency. This is only used</span>
<span id="L1084">                                ! if TIDES is true.</span>
<span id="L1085">TIDE_O1 = False                 !   [Boolean] default = False</span>
<span id="L1086">                                ! If true, apply tidal momentum forcing at the O1 frequency. This is only used</span>
<span id="L1087">                                ! if TIDES is true.</span>
<span id="L1088">TIDE_P1 = False                 !   [Boolean] default = False</span>
<span id="L1089">                                ! If true, apply tidal momentum forcing at the P1 frequency. This is only used</span>
<span id="L1090">                                ! if TIDES is true.</span>
<span id="L1091">TIDE_Q1 = False                 !   [Boolean] default = False</span>
<span id="L1092">                                ! If true, apply tidal momentum forcing at the Q1 frequency. This is only used</span>
<span id="L1093">                                ! if TIDES is true.</span>
<span id="L1094">TIDE_MF = False                 !   [Boolean] default = False</span>
<span id="L1095">                                ! If true, apply tidal momentum forcing at the MF frequency. This is only used</span>
<span id="L1096">                                ! if TIDES is true.</span>
<span id="L1097">TIDE_MM = False                 !   [Boolean] default = False</span>
<span id="L1098">                                ! If true, apply tidal momentum forcing at the MM frequency. This is only used</span>
<span id="L1099">                                ! if TIDES is true.</span>
<span id="L1100">TIDAL_SAL_FROM_FILE = False     !   [Boolean] default = False</span>
<span id="L1101">                                ! If true, read the tidal self-attraction and loading from input files,</span>
<span id="L1102">                                ! specified by TIDAL_INPUT_FILE. This is only used if TIDES is true.</span>
<span id="L1103">USE_PREVIOUS_TIDES = False      !   [Boolean] default = False</span>
<span id="L1104">                                ! If true, use the SAL from the previous iteration of the tides to facilitate</span>
<span id="L1105">                                ! convergent iteration. This is only used if TIDES is true.</span>
<span id="L1106">TIDE_REF_DATE = 0, 0, 0         ! default = 0, 0, 0</span>
<span id="L1107">                                ! Year,month,day to use as reference date for tidal forcing. If not specified,</span>
<span id="L1108">                                ! defaults to 0.</span>
<span id="L1109">TIDE_USE_EQ_PHASE = False       !   [Boolean] default = False</span>
<span id="L1110">                                ! Correct phases by calculating equilibrium phase arguments for TIDE_REF_DATE.</span>
<span id="L1111">TIDE_M2_FREQ = 1.405189E-04     !   [rad s-1] default = 1.405189E-04</span>
<span id="L1112">                                ! Frequency of the M2 tidal constituent. This is only used if TIDES and TIDE_M2</span>
<span id="L1113">                                ! are true, or if OBC_TIDE_N_CONSTITUENTS &gt; 0 and M2 is in</span>
<span id="L1114">                                ! OBC_TIDE_CONSTITUENTS.</span>
<span id="L1115">TIDE_M2_AMP = 0.242334          !   [m] default = 0.242334</span>
<span id="L1116">                                ! Amplitude of the M2 tidal constituent. This is only used if TIDES and TIDE_M2</span>
<span id="L1117">                                ! are true.</span>
<span id="L1118">TIDE_M2_PHASE_T0 = 0.0          !   [radians] default = 0.0</span>
<span id="L1119">                                ! Phase of the M2 tidal constituent at time 0. This is only used if TIDES and</span>
<span id="L1120">                                ! TIDE_M2 are true.</span>
<span id="L1121">TIDE_ADD_NODAL = False          !   [Boolean] default = False</span>
<span id="L1122">                                ! If true, include 18.6 year nodal modulation in the astronomical tidal forcing.</span>
<span id="L1123">TIDE_NODAL_REF_DATE = 0, 0, 0   ! default = 0, 0, 0</span>
<span id="L1124">                                ! Fixed reference date to use for nodal modulation of astronomical tidal</span>
<span id="L1125">                                ! forcing.</span>
<span id="L1126"></span>
<span id="L1127">! === module MOM_PressureForce ===</span>
<span id="L1128">ANALYTIC_FV_PGF = True          !   [Boolean] default = True</span>
<span id="L1129">                                ! If true the pressure gradient forces are calculated with a finite volume form</span>
<span id="L1130">                                ! that analytically integrates the equations of state in pressure to avoid any</span>
<span id="L1131">                                ! possibility of numerical thermobaric instability, as described in Adcroft et</span>
<span id="L1132">                                ! al., O. Mod. (2008).</span>
<span id="L1133"></span>
<span id="L1134">! === module MOM_PressureForce_FV ===</span>
<span id="L1135">RHO_PGF_REF = 1024.0            !   [kg m-3] default = 1024.0</span>
<span id="L1136">                                ! The reference density that is subtracted off when calculating pressure</span>
<span id="L1137">                                ! gradient forces.  Its inverse is subtracted off of specific volumes when in</span>
<span id="L1138">                                ! non-Boussinesq mode.  The default is RHO_0.</span>
<span id="L1139">RHO_PGF_REF_BUG = True          !   [Boolean] default = True</span>
<span id="L1140">                                ! If true, recover a bug that RHO_0 (the mean seawater density in Boussinesq</span>
<span id="L1141">                                ! mode) and RHO_PGF_REF (the subtracted reference density in finite volume</span>
<span id="L1142">                                ! pressure gradient forces) are incorrectly interchanged in several instances in</span>
<span id="L1143">                                ! Boussinesq mode.</span>
<span id="L1144">TIDES_ANSWER_DATE = 20230630    ! default = 99991231</span>
<span id="L1145">                                ! The vintage of self-attraction and loading (SAL) and tidal forcing</span>
<span id="L1146">                                ! calculations.  Setting dates before 20230701 recovers old answers (Boussinesq</span>
<span id="L1147">                                ! and non-Boussinesq modes) when SAL is part of the tidal forcing calculation.</span>
<span id="L1148">                                ! The answer difference is only at bit level and due to a reordered summation.</span>
<span id="L1149">                                ! Setting dates before 20250201 recovers answers (Boussinesq mode) that</span>
<span id="L1150">                                ! interface heights are modified before pressure force integrals are calculated.</span>
<span id="L1151">MASS_WEIGHT_IN_PRESSURE_GRADIENT = False !   [Boolean] default = False</span>
<span id="L1152">                                ! If true, use mass weighting when interpolating T/S for integrals near the</span>
<span id="L1153">                                ! bathymetry in FV pressure gradient calculations.</span>
<span id="L1154">MASS_WEIGHT_IN_PRESSURE_GRADIENT_TOP = False !   [Boolean] default = False</span>
<span id="L1155">                                ! If true and MASS_WEIGHT_IN_PRESSURE_GRADIENT is true, use mass weighting when</span>
<span id="L1156">                                ! interpolating T/S for integrals near the top of the water column in FV</span>
<span id="L1157">                                ! pressure gradient calculations.</span>
<span id="L1158">MASS_WEIGHT_IN_PGF_VANISHED_ONLY = False !   [Boolean] default = False</span>
<span id="L1159">                                ! If true, use mass weighting when interpolating T/S for integrals only if one</span>
<span id="L1160">                                ! side is vanished according to RESET_INTXPA_H_NONVANISHED.</span>
<span id="L1161">CORRECTION_INTXPA = False       !   [Boolean] default = False</span>
<span id="L1162">                                ! If true, use a correction for surface pressure curvature in intx_pa.</span>
<span id="L1163">RESET_INTXPA_INTEGRAL = False   !   [Boolean] default = False</span>
<span id="L1164">                                ! If true, reset INTXPA to match pressures at first nonvanished cell. Includes</span>
<span id="L1165">                                ! pressure correction.</span>
<span id="L1166">RESET_INTXPA_INTEGRAL_FLATTEST = False !   [Boolean] default = False</span>
<span id="L1167">                                ! If true, use flattest interface as reference interface where there is no</span>
<span id="L1168">                                ! better choice for RESET_INTXPA_INTEGRAL. Otherwise, use surface interface.</span>
<span id="L1169">USE_INACCURATE_PGF_RHO_ANOM = False !   [Boolean] default = False</span>
<span id="L1170">                                ! If true, use a form of the PGF that uses the reference density in an</span>
<span id="L1171">                                ! inaccurate way. This is not recommended.</span>
<span id="L1172">RECONSTRUCT_FOR_PRESSURE = False !   [Boolean] default = False</span>
<span id="L1173">                                ! If True, use vertical reconstruction of T &amp; S within the integrals of the FV</span>
<span id="L1174">                                ! pressure gradient calculation. If False, use the constant-by-layer algorithm.</span>
<span id="L1175">                                ! The default is set by USE_REGRIDDING.</span>
<span id="L1176">PRESSURE_RECONSTRUCTION_SCHEME = 1 ! default = 1</span>
<span id="L1177">                                ! Order of vertical reconstruction of T/S to use in the integrals within the FV</span>
<span id="L1178">                                ! pressure gradient calculation.</span>
<span id="L1179">                                !  0: PCM or no reconstruction.</span>
<span id="L1180">                                !  1: PLM reconstruction.</span>
<span id="L1181">                                !  2: PPM reconstruction.</span>
<span id="L1182">BOUNDARY_EXTRAPOLATION_PRESSURE = True !   [Boolean] default = True</span>
<span id="L1183">                                ! If true, the reconstruction of T &amp; S for pressure in boundary cells is</span>
<span id="L1184">                                ! extrapolated, rather than using PCM in these cells. If true, the same order</span>
<span id="L1185">                                ! polynomial is used as is used for the interior cells.</span>
<span id="L1186">USE_STANLEY_PGF = False         !   [Boolean] default = False</span>
<span id="L1187">                                ! If true, turn on Stanley SGS T variance parameterization in PGF code.</span>
<span id="L1188"></span>
<span id="L1189">! === module MOM_Zanna_Bolton ===</span>
<span id="L1190">USE_ZB2020 = False              !   [Boolean] default = False</span>
<span id="L1191">                                ! If true, turns on Zanna-Bolton-2020 (ZB) subgrid momentum parameterization of</span>
<span id="L1192">                                ! mesoscale eddies.</span>
<span id="L1193"></span>
<span id="L1194">! === module MOM_hor_visc ===</span>
<span id="L1195">USE_CIRCULATION_IN_HORVISC = False !   [Boolean] default = False</span>
<span id="L1196">                                ! Use circulation theorem to compute vorticity in horvisc module (for ZB20 or</span>
<span id="L1197">                                ! Leith)</span>
<span id="L1198">USE_CONT_THICKNESS = False      !   [Boolean] default = False</span>
<span id="L1199">                                ! If true, use thickness at velocity points from continuity solver. This option</span>
<span id="L1200">                                ! currently only works with split mode.</span>
<span id="L1201">LAPLACIAN = True                !   [Boolean] default = False</span>
<span id="L1202">                                ! If true, use a Laplacian horizontal viscosity.</span>
<span id="L1203">KH = 0.0                        !   [m2 s-1] default = 0.0</span>
<span id="L1204">                                ! The background Laplacian horizontal viscosity.</span>
<span id="L1205">KH_BG_MIN = 0.0                 !   [m2 s-1] default = 0.0</span>
<span id="L1206">                                ! The minimum value allowed for Laplacian horizontal viscosity, KH.</span>
<span id="L1207">KH_VEL_SCALE = 0.01             !   [m s-1] default = 0.0</span>
<span id="L1208">                                ! The velocity scale which is multiplied by the grid spacing to calculate the</span>
<span id="L1209">                                ! Laplacian viscosity. The final viscosity is the largest of this scaled</span>
<span id="L1210">                                ! viscosity, the Smagorinsky and Leith viscosities, and KH.</span>
<span id="L1211">KH_SIN_LAT = 0.0                !   [m2 s-1] default = 0.0</span>
<span id="L1212">                                ! The amplitude of a latitudinally-dependent background viscosity of the form</span>
<span id="L1213">                                ! KH_SIN_LAT*(SIN(LAT)**KH_PWR_OF_SINE).</span>
<span id="L1214">SMAGORINSKY_KH = False          !   [Boolean] default = False</span>
<span id="L1215">                                ! If true, use a Smagorinsky nonlinear eddy viscosity.</span>
<span id="L1216">LEITH_KH = False                !   [Boolean] default = False</span>
<span id="L1217">                                ! If true, use a Leith nonlinear eddy viscosity.</span>
<span id="L1218">BOUND_KH = True                 !   [Boolean] default = True</span>
<span id="L1219">                                ! If true, the Laplacian coefficient is locally limited to be stable.</span>
<span id="L1220">EY24_EBT_BS = False             !   [Boolean] default = False</span>
<span id="L1221">                                ! If true, use the the backscatter scheme (EBT mode with kill switch)developed</span>
<span id="L1222">                                ! by Yankovsky et al. (2024).</span>
<span id="L1223">ANISOTROPIC_VISCOSITY = False   !   [Boolean] default = False</span>
<span id="L1224">                                ! If true, allow anistropic viscosity in the Laplacian horizontal viscosity.</span>
<span id="L1225">ADD_LES_VISCOSITY = False       !   [Boolean] default = False</span>
<span id="L1226">                                ! If true, adds the viscosity from Smagorinsky and Leith to the background</span>
<span id="L1227">                                ! viscosity instead of taking the maximum.</span>
<span id="L1228">BIHARMONIC = True               !   [Boolean] default = True</span>
<span id="L1229">                                ! If true, use a biharmonic horizontal viscosity. BIHARMONIC may be used with</span>
<span id="L1230">                                ! LAPLACIAN.</span>
<span id="L1231">AH = 0.0                        !   [m4 s-1] default = 0.0</span>
<span id="L1232">                                ! The background biharmonic horizontal viscosity.</span>
<span id="L1233">AH_VEL_SCALE = 0.05             !   [m s-1] default = 0.0</span>
<span id="L1234">                                ! The velocity scale which is multiplied by the cube of the grid spacing to</span>
<span id="L1235">                                ! calculate the biharmonic viscosity. The final viscosity is the largest of this</span>
<span id="L1236">                                ! scaled viscosity, the Smagorinsky and Leith viscosities, and AH.</span>
<span id="L1237">AH_TIME_SCALE = 0.0             !   [s] default = 0.0</span>
<span id="L1238">                                ! A time scale whose inverse is multiplied by the fourth power of the grid</span>
<span id="L1239">                                ! spacing to calculate biharmonic viscosity. The final viscosity is the largest</span>
<span id="L1240">                                ! of all viscosity formulations in use. 0.0 means that it&#x27;s not used.</span>
<span id="L1241">SMAGORINSKY_AH = True           !   [Boolean] default = False</span>
<span id="L1242">                                ! If true, use a biharmonic Smagorinsky nonlinear eddy viscosity.</span>
<span id="L1243">LEITH_AH = False                !   [Boolean] default = False</span>
<span id="L1244">                                ! If true, use a biharmonic Leith nonlinear eddy viscosity.</span>
<span id="L1245">USE_LEITHY = False              !   [Boolean] default = False</span>
<span id="L1246">                                ! If true, use a biharmonic Leith nonlinear eddy viscosity together with a</span>
<span id="L1247">                                ! harmonic backscatter.</span>
<span id="L1248">BOUND_AH = True                 !   [Boolean] default = True</span>
<span id="L1249">                                ! If true, the biharmonic coefficient is locally limited to be stable.</span>
<span id="L1250">RE_AH = 0.0                     !   [nondim] default = 0.0</span>
<span id="L1251">                                ! If nonzero, the biharmonic coefficient is scaled so that the biharmonic</span>
<span id="L1252">                                ! Reynolds number is equal to this.</span>
<span id="L1253">BACKSCATTER_UNDERBOUND = False  !   [Boolean] default = False</span>
<span id="L1254">                                ! If true, the bounds on the biharmonic viscosity are allowed to increase where</span>
<span id="L1255">                                ! the Laplacian viscosity is negative (due to backscatter parameterizations)</span>
<span id="L1256">                                ! beyond the largest timestep-dependent stable values of biharmonic viscosity</span>
<span id="L1257">                                ! when no Laplacian viscosity is applied.  The default is true for historical</span>
<span id="L1258">                                ! reasons, but this option probably should not be used because it can contribute</span>
<span id="L1259">                                ! to numerical instabilities.</span>
<span id="L1260">SMAG_BI_CONST = 0.06            !   [nondim] default = 0.0</span>
<span id="L1261">                                ! The nondimensional biharmonic Smagorinsky constant, typically 0.015 - 0.06.</span>
<span id="L1262">BOUND_CORIOLIS_BIHARM = True    !   [Boolean] default = True</span>
<span id="L1263">                                ! If true use a viscosity that increases with the square of the velocity shears,</span>
<span id="L1264">                                ! so that the resulting viscous drag is of comparable magnitude to the Coriolis</span>
<span id="L1265">                                ! terms when the velocity differences between adjacent grid points is</span>
<span id="L1266">                                ! 0.5*BOUND_CORIOLIS_VEL.  The default is the value of BOUND_CORIOLIS (or</span>
<span id="L1267">                                ! false).</span>
<span id="L1268">BOUND_CORIOLIS_VEL = 6.0        !   [m s-1] default = 6.0</span>
<span id="L1269">                                ! The velocity scale at which BOUND_CORIOLIS_BIHARM causes the biharmonic drag</span>
<span id="L1270">                                ! to have comparable magnitude to the Coriolis acceleration.  The default is set</span>
<span id="L1271">                                ! by MAXVEL.</span>
<span id="L1272">USE_LAND_MASK_FOR_HVISC = True  !   [Boolean] default = True</span>
<span id="L1273">                                ! If true, use the land mask for the computation of thicknesses at velocity</span>
<span id="L1274">                                ! locations. This eliminates the dependence on arbitrary values over land or</span>
<span id="L1275">                                ! outside of the domain.</span>
<span id="L1276">HORVISC_BOUND_COEF = 0.8        !   [nondim] default = 0.8</span>
<span id="L1277">                                ! The nondimensional coefficient of the ratio of the viscosity bounds to the</span>
<span id="L1278">                                ! theoretical maximum for stability without considering other terms.</span>
<span id="L1279">USE_KH_BG_2D = False            !   [Boolean] default = False</span>
<span id="L1280">                                ! If true, read a file containing 2-d background harmonic viscosities. The final</span>
<span id="L1281">                                ! viscosity is the maximum of the other terms and this background value.</span>
<span id="L1282">FRICTWORK_BUG = False           !   [Boolean] default = False</span>
<span id="L1283">                                ! If true, retain an answer-changing bug in calculating the FrictWork, which</span>
<span id="L1284">                                ! cancels the h in thickness flux and the h at velocity point. This isnot</span>
<span id="L1285">                                ! recommended.</span>
<span id="L1286"></span>
<span id="L1287">! === module MOM_vert_friction ===</span>
<span id="L1288">DIRECT_STRESS = False           !   [Boolean] default = False</span>
<span id="L1289">                                ! If true, the wind stress is distributed over the topmost HMIX_STRESS of fluid</span>
<span id="L1290">                                ! (like in HYCOM), and an added mixed layer viscosity or a physically based</span>
<span id="L1291">                                ! boundary layer turbulence parameterization is not needed for stability.</span>
<span id="L1292">FIXED_DEPTH_LOTW_ML = False     !   [Boolean] default = False</span>
<span id="L1293">                                ! If true, use a Law-of-the-wall prescription for the mixed layer viscosity</span>
<span id="L1294">                                ! within a boundary layer that is the lesser of HMIX_FIXED and the total depth</span>
<span id="L1295">                                ! of the ocean in a column.</span>
<span id="L1296">LOTW_VISCOUS_ML_FLOOR = False   !   [Boolean] default = False</span>
<span id="L1297">                                ! If true, use a Law-of-the-wall prescription to set a lower bound on the</span>
<span id="L1298">                                ! viscous coupling between layers within the surface boundary layer, based the</span>
<span id="L1299">                                ! distance of interfaces from the surface.  This only acts when there are large</span>
<span id="L1300">                                ! changes in the thicknesses of successive layers or when the viscosity is set</span>
<span id="L1301">                                ! externally and the wind stress has subsequently increased.</span>
<span id="L1302">VON_KARMAN_CONST = 0.41         !   [nondim] default = 0.41</span>
<span id="L1303">                                ! The value the von Karman constant as used for mixed layer viscosity.</span>
<span id="L1304">HARMONIC_VISC = False           !   [Boolean] default = False</span>
<span id="L1305">                                ! If true, use the harmonic mean thicknesses for calculating the vertical</span>
<span id="L1306">                                ! viscosity.</span>
<span id="L1307">HARMONIC_BL_SCALE = 0.0         !   [nondim] default = 0.0</span>
<span id="L1308">                                ! A scale to determine when water is in the boundary layers based solely on</span>
<span id="L1309">                                ! harmonic mean thicknesses for the purpose of determining the extent to which</span>
<span id="L1310">                                ! the thicknesses used in the viscosities are upwinded.</span>
<span id="L1311">USE_GL90_IN_SSW = False         !   [Boolean] default = False</span>
<span id="L1312">                                ! If true, use simpler method to calculate 1/N^2 in GL90 vertical viscosity</span>
<span id="L1313">                                ! coefficient. This method is valid in stacked shallow water mode.</span>
<span id="L1314">CFL_TRUNCATE = 0.5              !   [nondim] default = 0.5</span>
<span id="L1315">                                ! The value of the CFL number that will cause velocity components to be</span>
<span id="L1316">                                ! truncated; instability can occur past 0.5.</span>
<span id="L1317">CFL_REPORT = 0.5                !   [nondim] default = 0.5</span>
<span id="L1318">                                ! The value of the CFL number that causes accelerations to be reported; the</span>
<span id="L1319">                                ! default is CFL_TRUNCATE.</span>
<span id="L1320">CFL_TRUNCATE_RAMP_TIME = 0.0    !   [s] default = 0.0</span>
<span id="L1321">                                ! The time over which the CFL truncation value is ramped up at the beginning of</span>
<span id="L1322">                                ! the run.</span>
<span id="L1323">CFL_TRUNCATE_START = 0.0        !   [nondim] default = 0.0</span>
<span id="L1324">                                ! The start value of the truncation CFL number used when ramping up CFL_TRUNC.</span>
<span id="L1325">STOKES_MIXING_COMBINED = False  !   [Boolean] default = False</span>
<span id="L1326">                                ! Flag to use Stokes drift Mixing via the Lagrangian  current (Eulerian plus</span>
<span id="L1327">                                ! Stokes drift).  Still needs work and testing, so not recommended for use.</span>
<span id="L1328">VEL_UNDERFLOW = 0.0             !   [m s-1] default = 0.0</span>
<span id="L1329">                                ! A negligibly small velocity magnitude below which velocity components are set</span>
<span id="L1330">                                ! to 0.  A reasonable value might be 1e-30 m/s, which is less than an Angstrom</span>
<span id="L1331">                                ! divided by the age of the universe.</span>
<span id="L1332"></span>
<span id="L1333">! === module MOM_barotropic ===</span>
<span id="L1334">USE_BT_CONT_TYPE = True         !   [Boolean] default = True</span>
<span id="L1335">                                ! If true, use a structure with elements that describe effective face areas from</span>
<span id="L1336">                                ! the summed continuity solver as a function the barotropic flow in coupling</span>
<span id="L1337">                                ! between the barotropic and baroclinic flow.  This is only used if SPLIT is</span>
<span id="L1338">                                ! true.</span>
<span id="L1339">INTEGRAL_BT_CONTINUITY = False  !   [Boolean] default = False</span>
<span id="L1340">                                ! If true, use the time-integrated velocity over the barotropic steps to</span>
<span id="L1341">                                ! determine the integrated transports used to update the continuity equation.</span>
<span id="L1342">                                ! Otherwise the transports are the sum of the transports based on a series of</span>
<span id="L1343">                                ! instantaneous velocities and the BT_CONT_TYPE for transports.  This is only</span>
<span id="L1344">                                ! valid if USE_BT_CONT_TYPE = True.</span>
<span id="L1345">BOUND_BT_CORRECTION = True      !   [Boolean] default = False</span>
<span id="L1346">                                ! If true, the corrective pseudo mass-fluxes into the barotropic solver are</span>
<span id="L1347">                                ! limited to values that require less than maxCFL_BT_cont to be accommodated.</span>
<span id="L1348">BT_CONT_CORR_BOUNDS = True      !   [Boolean] default = True</span>
<span id="L1349">                                ! If true, and BOUND_BT_CORRECTION is true, use the BT_cont_type variables to</span>
<span id="L1350">                                ! set limits determined by MAXCFL_BT_CONT on the CFL number of the velocities</span>
<span id="L1351">                                ! that are likely to be driven by the corrective mass fluxes.</span>
<span id="L1352">ADJUST_BT_CONT = False          !   [Boolean] default = False</span>
<span id="L1353">                                ! If true, adjust the curve fit to the BT_cont type that is used by the</span>
<span id="L1354">                                ! barotropic solver to match the transport about which the flow is being</span>
<span id="L1355">                                ! linearized.</span>
<span id="L1356">GRADUAL_BT_ICS = False          !   [Boolean] default = False</span>
<span id="L1357">                                ! If true, adjust the initial conditions for the barotropic solver to the values</span>
<span id="L1358">                                ! from the layered solution over a whole timestep instead of instantly. This is</span>
<span id="L1359">                                ! a decent approximation to the inclusion of sum(u dh_dt) while also correcting</span>
<span id="L1360">                                ! for truncation errors.</span>
<span id="L1361">BT_USE_VISC_REM_U_UH0 = False   !   [Boolean] default = False</span>
<span id="L1362">                                ! If true, use the viscous remnants when estimating the barotropic velocities</span>
<span id="L1363">                                ! that were used to calculate uh0 and vh0.  False is probably the better choice.</span>
<span id="L1364">BT_PROJECT_VELOCITY = True      !   [Boolean] default = False</span>
<span id="L1365">                                ! If true, step the barotropic velocity first and project out the velocity</span>
<span id="L1366">                                ! tendency by 1+BEBT when calculating the transport.  The default (false) is to</span>
<span id="L1367">                                ! use a predictor continuity step to find the pressure field, and then to do a</span>
<span id="L1368">                                ! corrector continuity step using a weighted average of the old and new</span>
<span id="L1369">                                ! velocities, with weights of (1-BEBT) and BEBT.</span>
<span id="L1370">BT_NONLIN_STRESS = False        !   [Boolean] default = False</span>
<span id="L1371">                                ! If true, use the full depth of the ocean at the start of the barotropic step</span>
<span id="L1372">                                ! when calculating the surface stress contribution to the barotropic</span>
<span id="L1373">                                ! acclerations.  Otherwise use the depth based on bathyT.</span>
<span id="L1374">BT_RHO_LINEARIZED = 1024.0      !   [kg m-3] default = 1024.0</span>
<span id="L1375">                                ! A density that is used to convert total water column thicknesses into mass in</span>
<span id="L1376">                                ! non-Boussinesq mode with linearized options in the barotropic solver or when</span>
<span id="L1377">                                ! estimating the stable barotropic timestep without access to the full</span>
<span id="L1378">                                ! baroclinic model state.</span>
<span id="L1379">DYNAMIC_SURFACE_PRESSURE = False !   [Boolean] default = False</span>
<span id="L1380">                                ! If true, add a dynamic pressure due to a viscous ice shelf, for instance.</span>
<span id="L1381">BT_CORIOLIS_SCALE = 1.0         !   [nondim] default = 1.0</span>
<span id="L1382">                                ! A factor by which the barotropic Coriolis anomaly terms are scaled.</span>
<span id="L1383">VISC_REM_BT_WEIGHT_BUG = True   !   [Boolean] default = True</span>
<span id="L1384">                                ! If true, recover a bug in barotropic solver that uses an unnormalized weight</span>
<span id="L1385">                                ! function for vertical averages of baroclinic velocity and forcing. Default of</span>
<span id="L1386">                                ! this flag is set by VISC_REM_BUG.</span>
<span id="L1387">BAROTROPIC_TIDAL_SAL_BUG = False !   [Boolean] default = False</span>
<span id="L1388">                                ! If true, the tidal self-attraction and loading anomaly in the barotropic</span>
<span id="L1389">                                ! solver has the wrong sign, replicating a long-standing bug with a scalar</span>
<span id="L1390">                                ! self-attraction and loading term or the SAL term from a previous simulation.</span>
<span id="L1391">TIDAL_SAL_FLATHER = False       !   [Boolean] default = False</span>
<span id="L1392">                                ! If true, then apply adjustments to the external gravity wave speed used with</span>
<span id="L1393">                                ! the Flather OBC routine consistent with the barotropic solver. This applies to</span>
<span id="L1394">                                ! cases with  tidal forcing using the scalar self-attraction approximation. The</span>
<span id="L1395">                                ! default is currently False in order to retain previous answers but should be</span>
<span id="L1396">                                ! set to True for new experiments</span>
<span id="L1397">SADOURNY = True                 !   [Boolean] default = True</span>
<span id="L1398">                                ! If true, the Coriolis terms are discretized with the Sadourny (1975) energy</span>
<span id="L1399">                                ! conserving scheme, otherwise the Arakawa &amp; Hsu scheme is used.  If the</span>
<span id="L1400">                                ! internal deformation radius is not resolved, the Sadourny scheme should</span>
<span id="L1401">                                ! probably be used.</span>
<span id="L1402">BT_THICK_SCHEME = &quot;FROM_BT_CONT&quot; ! default = &quot;FROM_BT_CONT&quot;</span>
<span id="L1403">                                ! A string describing the scheme that is used to set the open face areas used</span>
<span id="L1404">                                ! for barotropic transport and the relative weights of the accelerations. Valid</span>
<span id="L1405">                                ! values are:</span>
<span id="L1406">                                !    ARITHMETIC - arithmetic mean layer thicknesses</span>
<span id="L1407">                                !    HARMONIC - harmonic mean layer thicknesses</span>
<span id="L1408">                                !    HYBRID (the default) - use arithmetic means for</span>
<span id="L1409">                                !       layers above the shallowest bottom, the harmonic</span>
<span id="L1410">                                !       mean for layers below, and a weighted average for</span>
<span id="L1411">                                !       layers that straddle that depth</span>
<span id="L1412">                                !    FROM_BT_CONT - use the average thicknesses kept</span>
<span id="L1413">                                !       in the h_u and h_v fields of the BT_cont_type</span>
<span id="L1414">BT_STRONG_DRAG = False          !   [Boolean] default = False</span>
<span id="L1415">                                ! If true, use a stronger estimate of the retarding effects of strong bottom</span>
<span id="L1416">                                ! drag, by making it implicit with the barotropic time-step instead of implicit</span>
<span id="L1417">                                ! with the baroclinic time-step and dividing by the number of barotropic steps.</span>
<span id="L1418">BT_LINEAR_WAVE_DRAG = False     !   [Boolean] default = False</span>
<span id="L1419">                                ! If true, apply a linear drag to the barotropic velocities, using rates set by</span>
<span id="L1420">                                ! lin_drag_u &amp; _v divided by the depth of the ocean.  This was introduced to</span>
<span id="L1421">                                ! facilitate tide modeling.</span>
<span id="L1422">BT_LINEAR_FREQ_DRAG = False     !   [Boolean] default = False</span>
<span id="L1423">                                ! If true, apply frequency-dependent drag to the tidal velocities. The streaming</span>
<span id="L1424">                                ! band-pass filter must be turned on.</span>
<span id="L1425">CLIP_BT_VELOCITY = False        !   [Boolean] default = False</span>
<span id="L1426">                                ! If true, limit any velocity components that exceed CFL_TRUNCATE.  This should</span>
<span id="L1427">                                ! only be used as a desperate debugging measure.</span>
<span id="L1428">MAXCFL_BT_CONT = 0.25           !   [nondim] default = 0.25</span>
<span id="L1429">                                ! The maximum permitted CFL number associated with the barotropic accelerations</span>
<span id="L1430">                                ! from the summed velocities times the time-derivatives of thicknesses.</span>
<span id="L1431">DT_BT_FILTER = -0.25            !   [sec or nondim] default = -0.25</span>
<span id="L1432">                                ! A time-scale over which the barotropic mode solutions are filtered, in seconds</span>
<span id="L1433">                                ! if positive, or as a fraction of DT if negative. When used this can never be</span>
<span id="L1434">                                ! taken to be longer than 2*dt.  Set this to 0 to apply no filtering.</span>
<span id="L1435">G_BT_EXTRA = 0.0                !   [nondim] default = 0.0</span>
<span id="L1436">                                ! A nondimensional factor by which gtot is enhanced.</span>
<span id="L1437">SSH_EXTRA = 10.0                !   [m] default = 10.0</span>
<span id="L1438">                                ! An estimate of how much higher SSH might get, for use in calculating the safe</span>
<span id="L1439">                                ! external wave speed. The default is the minimum of 10 m or 5% of</span>
<span id="L1440">                                ! MAXIMUM_DEPTH.</span>
<span id="L1441">LINEARIZED_BT_CORIOLIS = True   !   [Boolean] default = True</span>
<span id="L1442">                                ! If true use the bottom depth instead of the total water column thickness in</span>
<span id="L1443">                                ! the barotropic Coriolis term calculations.</span>
<span id="L1444">BEBT = 0.2                      !   [nondim] default = 0.1</span>
<span id="L1445">                                ! BEBT determines whether the barotropic time stepping uses the forward-backward</span>
<span id="L1446">                                ! time-stepping scheme or a backward Euler scheme. BEBT is valid in the range</span>
<span id="L1447">                                ! from 0 (for a forward-backward treatment of nonrotating gravity waves) to 1</span>
<span id="L1448">                                ! (for a backward Euler treatment). In practice, BEBT must be greater than about</span>
<span id="L1449">                                ! 0.05.</span>
<span id="L1450">DTBT = -0.95                    !   [s or nondim] default = -0.98</span>
<span id="L1451">                                ! The barotropic time step, in s. DTBT is only used with the split explicit time</span>
<span id="L1452">                                ! stepping. To set the time step automatically based the maximum stable value</span>
<span id="L1453">                                ! use 0, or a negative value gives the fraction of the stable value. Setting</span>
<span id="L1454">                                ! DTBT to 0 is the same as setting it to -0.98. The value of DTBT that will</span>
<span id="L1455">                                ! actually be used is an integer fraction of DT, rounding down.</span>
<span id="L1456">BT_USE_OLD_CORIOLIS_BRACKET_BUG = False !   [Boolean] default = False</span>
<span id="L1457">                                ! If True, use an order of operations that is not bitwise rotationally symmetric</span>
<span id="L1458">                                ! in the meridional Coriolis term of the barotropic solver.</span>
<span id="L1459">MASK_COASTAL_PRESSURE_FORCE = False !   [Boolean] default = False</span>
<span id="L1460">                                ! If true, use the land masks to zero out the diagnosed barotropic pressure</span>
<span id="L1461">                                ! gradient accelerations at coastal or land points.  This changes diagnostics</span>
<span id="L1462">                                ! and improves the reproducibility of certain debugging checksums, but it does</span>
<span id="L1463">                                ! not alter the solutions themselves.</span>
<span id="L1464"></span>
<span id="L1465">! === module MOM_mixed_layer_restrat ===</span>
<span id="L1466">MIXEDLAYER_RESTRAT = True       !   [Boolean] default = False</span>
<span id="L1467">                                ! If true, a density-gradient dependent re-stratifying flow is imposed in the</span>
<span id="L1468">                                ! mixed layer. Can be used in ALE mode without restriction but in layer mode can</span>
<span id="L1469">                                ! only be used if BULKMIXEDLAYER is true.</span>
<span id="L1470">MLE%</span>
<span id="L1471">%MLE</span>
<span id="L1472">FOX_KEMPER_ML_RESTRAT_COEF = 20.0 !   [nondim] default = 0.0</span>
<span id="L1473">                                ! A nondimensional coefficient that is proportional to the ratio of the</span>
<span id="L1474">                                ! deformation radius to the dominant lengthscale of the submesoscale mixed layer</span>
<span id="L1475">                                ! instabilities, times the minimum of the ratio of the mesoscale eddy kinetic</span>
<span id="L1476">                                ! energy to the large-scale geostrophic kinetic energy or 1 plus the square of</span>
<span id="L1477">                                ! the grid spacing over the deformation radius, as detailed by Fox-Kemper et al.</span>
<span id="L1478">                                ! (2011)</span>
<span id="L1479">USE_STANLEY_ML = False          !   [Boolean] default = False</span>
<span id="L1480">                                ! If true, turn on Stanley SGS T variance parameterization in ML restrat code.</span>
<span id="L1481">KV_RESTRAT = 0.0                !   [m2 s-1] default = 0.0</span>
<span id="L1482">                                ! A small viscosity that sets a floor on the momentum mixing rate during</span>
<span id="L1483">                                ! restratification.  If this is positive, it will prevent some possible</span>
<span id="L1484">                                ! divisions by zero even if ustar, RESTRAT_USTAR_MIN, and f are all 0.</span>
<span id="L1485">RESTRAT_USTAR_MIN = 1.45842E-18 !   [m s-1] default = 1.45842E-18</span>
<span id="L1486">                                ! The minimum value of ustar that will be used by the mixed layer</span>
<span id="L1487">                                ! restratification module.  This can be tiny, but if this is greater than 0, it</span>
<span id="L1488">                                ! will prevent divisions by zero when f and KV_RESTRAT are zero.</span>
<span id="L1489"></span>
<span id="L1490">! === module MOM_diagnostics ===</span>
<span id="L1491">DIAG_EBT_MONO_N2_COLUMN_FRACTION = 0.0 !   [nondim] default = 0.0</span>
<span id="L1492">                                ! The lower fraction of water column over which N2 is limited as monotonic for</span>
<span id="L1493">                                ! the purposes of calculating the equivalent barotropic wave speed.</span>
<span id="L1494">DIAG_EBT_MONO_N2_DEPTH = -1.0   !   [m] default = -1.0</span>
<span id="L1495">                                ! The depth below which N2 is limited as monotonic for the purposes of</span>
<span id="L1496">                                ! calculating the equivalent barotropic wave speed.</span>
<span id="L1497">INTWAVE_REMAPPING_USE_OM4_SUBCELLS = True !   [Boolean] default = True</span>
<span id="L1498">                                ! If true, use the OM4 remapping-via-subcells algorithm for calculating EBT</span>
<span id="L1499">                                ! structure. See REMAPPING_USE_OM4_SUBCELLS for details. We recommend setting</span>
<span id="L1500">                                ! this option to false.</span>
<span id="L1501"></span>
<span id="L1502">! === module MOM_diabatic_driver ===</span>
<span id="L1503">! The following parameters are used for diabatic processes.</span>
<span id="L1504">USE_LEGACY_DIABATIC_DRIVER = True !   [Boolean] default = True</span>
<span id="L1505">                                ! If true, use a legacy version of the diabatic subroutine. This is temporary</span>
<span id="L1506">                                ! and is needed to avoid change in answers.</span>
<span id="L1507">ENERGETICS_SFC_PBL = False      !   [Boolean] default = False</span>
<span id="L1508">                                ! If true, use an implied energetics planetary boundary layer scheme to</span>
<span id="L1509">                                ! determine the diffusivity and viscosity in the surface boundary layer.</span>
<span id="L1510">EPBL_IS_ADDITIVE = True         !   [Boolean] default = True</span>
<span id="L1511">                                ! If true, the diffusivity from ePBL is added to all other diffusivities.</span>
<span id="L1512">                                ! Otherwise, the larger of kappa-shear and ePBL diffusivities are used.</span>
<span id="L1513">ML_MIX_FIRST = 0.0              !   [nondim] default = 0.0</span>
<span id="L1514">                                ! The fraction of the mixed layer mixing that is applied before interior</span>
<span id="L1515">                                ! diapycnal mixing.  0 by default.</span>
<span id="L1516">INTERNAL_TIDES = False          !   [Boolean] default = False</span>
<span id="L1517">                                ! If true, use the code that advances a separate set of equations for the</span>
<span id="L1518">                                ! internal tide energy density.</span>
<span id="L1519">MASSLESS_MATCH_TARGETS = True   !   [Boolean] default = True</span>
<span id="L1520">                                ! If true, the temperature and salinity of massless layers are kept consistent</span>
<span id="L1521">                                ! with their target densities. Otherwise the properties of massless layers</span>
<span id="L1522">                                ! evolve diffusively to match massive neighboring layers.</span>
<span id="L1523">AGGREGATE_FW_FORCING = True     !   [Boolean] default = True</span>
<span id="L1524">                                ! If true, the net incoming and outgoing fresh water fluxes are combined and</span>
<span id="L1525">                                ! applied as either incoming or outgoing depending on the sign of the net. If</span>
<span id="L1526">                                ! false, the net incoming fresh water flux is added to the model and thereafter</span>
<span id="L1527">                                ! the net outgoing is removed from the topmost non-vanished layers of the</span>
<span id="L1528">                                ! updated state.</span>
<span id="L1529">MIX_BOUNDARY_TRACERS = True     !   [Boolean] default = True</span>
<span id="L1530">                                ! If true, mix the passive tracers in massless layers at the bottom into the</span>
<span id="L1531">                                ! interior as though a diffusivity of KD_MIN_TR were operating.</span>
<span id="L1532">KD_MIN_TR = 2.0E-06             !   [m2 s-1] default = 2.0E-06</span>
<span id="L1533">                                ! A minimal diffusivity that should always be applied to tracers, especially in</span>
<span id="L1534">                                ! massless layers near the bottom. The default is 0.1*KD.</span>
<span id="L1535">KD_BBL_TR = 0.0                 !   [m2 s-1] default = 0.0</span>
<span id="L1536">                                ! A bottom boundary layer tracer diffusivity that will allow for explicitly</span>
<span id="L1537">                                ! specified bottom fluxes. The entrainment at the bottom is at least</span>
<span id="L1538">                                ! sqrt(Kd_BBL_tr*dt) over the same distance.</span>
<span id="L1539">TRACER_TRIDIAG = False          !   [Boolean] default = False</span>
<span id="L1540">                                ! If true, use the passive tracer tridiagonal solver for T and S</span>
<span id="L1541">MINIMUM_FORCING_DEPTH = 0.001   !   [m] default = 0.001</span>
<span id="L1542">                                ! The smallest depth over which forcing can be applied. This only takes effect</span>
<span id="L1543">                                ! when near-surface layers become thin relative to this scale, in which case the</span>
<span id="L1544">                                ! forcing tendencies scaled down by distributing the forcing over this depth</span>
<span id="L1545">                                ! scale.</span>
<span id="L1546">EVAP_CFL_LIMIT = 0.8            !   [nondim] default = 0.8</span>
<span id="L1547">                                ! The largest fraction of a layer than can be lost to forcing (e.g. evaporation,</span>
<span id="L1548">                                ! sea-ice formation) in one time-step. The unused mass loss is passed down</span>
<span id="L1549">                                ! through the column.</span>
<span id="L1550">MLD_EN_VALS = 25.0, 2500.0, 2.5E+05 !   [J/m2] default = 25.0, 2500.0, 2.5E+05</span>
<span id="L1551">                                ! The energy values used to compute MLDs.  If not set (or all set to 0.), the</span>
<span id="L1552">                                ! default will overwrite to 25., 2500., 250000.</span>
<span id="L1553">BMLD_EN_VALS = 25.0, 2500.0, 2.5E+05 !   [J/m2] default = 25.0, 2500.0, 2.5E+05</span>
<span id="L1554">                                ! The energy values used to compute Bottom MLDs.  If not set (or all set to 0.),</span>
<span id="L1555">                                ! the default will overwrite to 25., 2500., 250000.</span>
<span id="L1556">DIAG_MLD_DENSITY_DIFF = 0.1     !   [kg/m3] default = 0.1</span>
<span id="L1557">                                ! The density difference used to determine a diagnostic mixed layer depth,</span>
<span id="L1558">                                ! MLD_user, following the definition of Levitus 1982. The MLD is the depth at</span>
<span id="L1559">                                ! which the density is larger than the surface density by the specified amount.</span>
<span id="L1560">DIAG_DEPTH_SUBML_N2 = 50.0      !   [m] default = 50.0</span>
<span id="L1561">                                ! The distance over which to calculate a diagnostic of the stratification at the</span>
<span id="L1562">                                ! base of the mixed layer.</span>
<span id="L1563"></span>
<span id="L1564">! === module MOM_CVMix_KPP ===</span>
<span id="L1565">! This is the MOM wrapper to CVMix:KPP</span>
<span id="L1566">! See http://cvmix.github.io/</span>
<span id="L1567">USE_KPP = False                 !   [Boolean] default = False</span>
<span id="L1568">                                ! If true, turns on the [CVMix] KPP scheme of Large et al., 1994, to calculate</span>
<span id="L1569">                                ! diffusivities and non-local transport in the OBL.</span>
<span id="L1570"></span>
<span id="L1571">! === module MOM_CVMix_conv ===</span>
<span id="L1572">! Parameterization of enhanced mixing due to convection via CVMix</span>
<span id="L1573">USE_CVMix_CONVECTION = False    !   [Boolean] default = False</span>
<span id="L1574">                                ! If true, turns on the enhanced mixing due to convection via CVMix. This scheme</span>
<span id="L1575">                                ! increases diapycnal diffs./viscs. at statically unstable interfaces. Relevant</span>
<span id="L1576">                                ! parameters are contained in the CVMix_CONVECTION% parameter block.</span>
<span id="L1577"></span>
<span id="L1578">! === module MOM_entrain_diffusive ===</span>
<span id="L1579">MAX_ENT_IT = 20                 ! default = 5</span>
<span id="L1580">                                ! The maximum number of iterations that may be used to calculate the interior</span>
<span id="L1581">                                ! diapycnal entrainment.</span>
<span id="L1582">TOLERANCE_ENT = 1.0E-05         !   [m] default = 2.683281572999748E-05</span>
<span id="L1583">                                ! The tolerance with which to solve for entrainment values.</span>
<span id="L1584">ENTRAIN_DIFFUSIVE_MAX_ENT = 1.0E+04 !   [m] default = 1.0E+04</span>
<span id="L1585">                                ! A large ceiling on the maximum permitted amount of entrainment across each</span>
<span id="L1586">                                ! interface between the mixed and buffer layers within a timestep.</span>
<span id="L1587"></span>
<span id="L1588">! === module MOM_geothermal ===</span>
<span id="L1589">GEOTHERMAL_SCALE = 0.001        !   [W m-2 or various] default = 0.0</span>
<span id="L1590">                                ! The constant geothermal heat flux, a rescaling factor for the heat flux read</span>
<span id="L1591">                                ! from GEOTHERMAL_FILE, or 0 to disable the geothermal heating.</span>
<span id="L1592">GEOTHERMAL_FILE = &quot;geothermal_heating_cm2g.nc&quot; ! default = &quot;&quot;</span>
<span id="L1593">                                ! The file from which the geothermal heating is to be read, or blank to use a</span>
<span id="L1594">                                ! constant heating rate.</span>
<span id="L1595">GEOTHERMAL_THICKNESS = 0.1      !   [m] default = 0.1</span>
<span id="L1596">                                ! The thickness over which to apply geothermal heating.</span>
<span id="L1597">GEOTHERMAL_DRHO_DT_INPLACE = -0.01 !   [kg m-3 K-1] default = -0.01</span>
<span id="L1598">                                ! The value of drho_dT above which geothermal heating simply heats water in</span>
<span id="L1599">                                ! place instead of moving it between isopycnal layers.  This must be negative.</span>
<span id="L1600">GEOTHERMAL_VARNAME = &quot;geo_heat&quot; ! default = &quot;geo_heat&quot;</span>
<span id="L1601">                                ! The name of the geothermal heating variable in GEOTHERMAL_FILE.</span>
<span id="L1602"></span>
<span id="L1603">! === module MOM_set_diffusivity ===</span>
<span id="L1604">FLUX_RI_MAX = 0.2               !   [nondim] default = 0.2</span>
<span id="L1605">                                ! The flux Richardson number where the stratification is large enough that N2 &gt;</span>
<span id="L1606">                                ! omega2.  The full expression for the Flux Richardson number is usually</span>
<span id="L1607">                                ! FLUX_RI_MAX*N2/(N2+OMEGA2).</span>
<span id="L1608"></span>
<span id="L1609">! === module MOM_tidal_mixing ===</span>
<span id="L1610">! Vertical Tidal Mixing Parameterization</span>
<span id="L1611">USE_CVMix_TIDAL = False         !   [Boolean] default = False</span>
<span id="L1612">                                ! If true, turns on tidal mixing via CVMix</span>
<span id="L1613">INT_TIDE_DISSIPATION = True     !   [Boolean] default = False</span>
<span id="L1614">                                ! If true, use an internal tidal dissipation scheme to drive diapycnal mixing,</span>
<span id="L1615">                                ! along the lines of St. Laurent et al. (2002) and Simmons et al. (2004).</span>
<span id="L1616">INT_TIDE_PROFILE = &quot;STLAURENT_02&quot; ! default = &quot;STLAURENT_02&quot;</span>
<span id="L1617">                                ! INT_TIDE_PROFILE selects the vertical profile of energy dissipation with</span>
<span id="L1618">                                ! INT_TIDE_DISSIPATION. Valid values are:</span>
<span id="L1619">                                !    STLAURENT_02 - Use the St. Laurent et al exponential</span>
<span id="L1620">                                !                   decay profile.</span>
<span id="L1621">                                !    POLZIN_09 - Use the Polzin WKB-stretched algebraic</span>
<span id="L1622">                                !                   decay profile.</span>
<span id="L1623">LEE_WAVE_DISSIPATION = False    !   [Boolean] default = False</span>
<span id="L1624">                                ! If true, use an lee wave driven dissipation scheme to drive diapycnal mixing,</span>
<span id="L1625">                                ! along the lines of Nikurashin (2010) and using the St. Laurent et al. (2002)</span>
<span id="L1626">                                ! and Simmons et al. (2004) vertical profile</span>
<span id="L1627">INT_TIDE_LOWMODE_DISSIPATION = False !   [Boolean] default = False</span>
<span id="L1628">                                ! If true, consider mixing due to breaking low modes that have been remotely</span>
<span id="L1629">                                ! generated; as with itidal drag on the barotropic tide, use an internal tidal</span>
<span id="L1630">                                ! dissipation scheme to drive diapycnal mixing, along the lines of St. Laurent</span>
<span id="L1631">                                ! et al. (2002) and Simmons et al. (2004).</span>
<span id="L1632">INT_TIDE_DECAY_SCALE = 300.3003003003003 !   [m] default = 500.0</span>
<span id="L1633">                                ! The decay scale away from the bottom for tidal TKE with the new coding when</span>
<span id="L1634">                                ! INT_TIDE_DISSIPATION is used.</span>
<span id="L1635">MU_ITIDES = 0.2                 !   [nondim] default = 0.2</span>
<span id="L1636">                                ! A dimensionless turbulent mixing efficiency used with INT_TIDE_DISSIPATION,</span>
<span id="L1637">                                ! often 0.2.</span>
<span id="L1638">GAMMA_ITIDES = 0.3333           !   [nondim] default = 0.3333</span>
<span id="L1639">                                ! The fraction of the internal tidal energy that is dissipated locally with</span>
<span id="L1640">                                ! INT_TIDE_DISSIPATION. THIS NAME COULD BE BETTER.</span>
<span id="L1641">MIN_ZBOT_ITIDES = 0.0           !   [m] default = 0.0</span>
<span id="L1642">                                ! Turn off internal tidal dissipation when the total ocean depth is less than</span>
<span id="L1643">                                ! this value.</span>
<span id="L1644">KAPPA_ITIDES = 6.28319E-04      !   [m-1] default = 6.283185307179586E-04</span>
<span id="L1645">                                ! A topographic wavenumber used with INT_TIDE_DISSIPATION. The default is 2pi/10</span>
<span id="L1646">                                ! km, as in St.Laurent et al. 2002.</span>
<span id="L1647">UTIDE = 0.0                     !   [m s-1] default = 0.0</span>
<span id="L1648">                                ! The constant tidal amplitude used with INT_TIDE_DISSIPATION.</span>
<span id="L1649">KAPPA_H2_FACTOR = 0.75          !   [nondim] default = 1.0</span>
<span id="L1650">                                ! A scaling factor for the roughness amplitude with INT_TIDE_DISSIPATION.</span>
<span id="L1651">TKE_ITIDE_MAX = 0.1             !   [W m-2] default = 1000.0</span>
<span id="L1652">                                ! The maximum internal tide energy source available to mix above the bottom</span>
<span id="L1653">                                ! boundary layer with INT_TIDE_DISSIPATION.</span>
<span id="L1654">READ_TIDEAMP = True             !   [Boolean] default = False</span>
<span id="L1655">                                ! If true, read a file (given by TIDEAMP_FILE) containing the tidal amplitude</span>
<span id="L1656">                                ! with INT_TIDE_DISSIPATION.</span>
<span id="L1657">TIDEAMP_FILE = &quot;tideamp.nc&quot;     ! default = &quot;tideamp.nc&quot;</span>
<span id="L1658">                                ! The path to the file containing the spatially varying tidal amplitudes with</span>
<span id="L1659">                                ! INT_TIDE_DISSIPATION.</span>
<span id="L1660">TIDEAMP_VARNAME = &quot;tideamp&quot;     ! default = &quot;tideamp&quot;</span>
<span id="L1661">                                ! The name of the tidal amplitude variable in the input file.</span>
<span id="L1662">H2_FILE = &quot;sgs_h2.nc&quot;           !</span>
<span id="L1663">                                ! The path to the file containing the sub-grid-scale topographic roughness</span>
<span id="L1664">                                ! amplitude with INT_TIDE_DISSIPATION.</span>
<span id="L1665">ROUGHNESS_VARNAME = &quot;h2&quot;        ! default = &quot;h2&quot;</span>
<span id="L1666">                                ! The name in the input file of the squared sub-grid-scale topographic roughness</span>
<span id="L1667">                                ! amplitude variable.</span>
<span id="L1668">FRACTIONAL_ROUGHNESS_MAX = 0.1  !   [nondim] default = 0.1</span>
<span id="L1669">                                ! The maximum topographic roughness amplitude as a fraction of the mean depth,</span>
<span id="L1670">                                ! or a negative value for no limitations on roughness.</span>
<span id="L1671">ML_RADIATION = True             !   [Boolean] default = False</span>
<span id="L1672">                                ! If true, allow a fraction of TKE available from wind work to penetrate below</span>
<span id="L1673">                                ! the base of the mixed layer with a vertical decay scale determined by the</span>
<span id="L1674">                                ! minimum of: (1) The depth of the mixed layer, (2) an Ekman length scale.</span>
<span id="L1675">ML_RAD_EFOLD_COEFF = 0.2        !   [nondim] default = 0.2</span>
<span id="L1676">                                ! A coefficient that is used to scale the penetration depth for turbulence below</span>
<span id="L1677">                                ! the base of the mixed layer. This is only used if ML_RADIATION is true.</span>
<span id="L1678">ML_RAD_BUG = False              !   [Boolean] default = False</span>
<span id="L1679">                                ! If true use code with a bug that reduces the energy available in the</span>
<span id="L1680">                                ! transition layer by a factor of the inverse of the energy deposition</span>
<span id="L1681">                                ! lenthscale (in m).</span>
<span id="L1682">ML_RAD_KD_MAX = 0.001           !   [m2 s-1] default = 0.001</span>
<span id="L1683">                                ! The maximum diapycnal diffusivity due to turbulence radiated from the base of</span>
<span id="L1684">                                ! the mixed layer. This is only used if ML_RADIATION is true.</span>
<span id="L1685">ML_RAD_COEFF = 0.1              !   [nondim] default = 0.2</span>
<span id="L1686">                                ! The coefficient which scales MSTAR*USTAR^3 to obtain the energy available for</span>
<span id="L1687">                                ! mixing below the base of the mixed layer. This is only used if ML_RADIATION is</span>
<span id="L1688">                                ! true.</span>
<span id="L1689">ML_RAD_APPLY_TKE_DECAY = True   !   [Boolean] default = True</span>
<span id="L1690">                                ! If true, apply the same exponential decay to ML_rad as is applied to the other</span>
<span id="L1691">                                ! surface sources of TKE in the mixed layer code. This is only used if</span>
<span id="L1692">                                ! ML_RADIATION is true.</span>
<span id="L1693">MSTAR = 0.3                     !   [nondim] default = 1.2</span>
<span id="L1694">                                ! The ratio of the friction velocity cubed to the TKE input to the mixed layer.</span>
<span id="L1695">TKE_DECAY = 10.0                !   [nondim] default = 2.5</span>
<span id="L1696">                                ! The ratio of the natural Ekman depth to the TKE decay scale.</span>
<span id="L1697">BBL_EFFIC = 0.2                 !   [nondim] default = 0.2</span>
<span id="L1698">                                ! The efficiency with which the energy extracted by bottom drag drives BBL</span>
<span id="L1699">                                ! diffusion.  This is only used if BOTTOMDRAGLAW is true.</span>
<span id="L1700">BBL_MIXING_MAX_DECAY = 200.0    !   [m] default = 200.0</span>
<span id="L1701">                                ! The maximum decay scale for the BBL diffusion, or 0 to allow the mixing to</span>
<span id="L1702">                                ! penetrate as far as stratification and rotation permit.  The default for now</span>
<span id="L1703">                                ! is 200 m. This is only used if BOTTOMDRAGLAW is true.</span>
<span id="L1704">BBL_MIXING_AS_MAX = False       !   [Boolean] default = True</span>
<span id="L1705">                                ! If true, take the maximum of the diffusivity from the BBL mixing and the other</span>
<span id="L1706">                                ! diffusivities. Otherwise, diffusivity from the BBL_mixing is simply added.</span>
<span id="L1707">USE_LOTW_BBL_DIFFUSIVITY = False !   [Boolean] default = False</span>
<span id="L1708">                                ! If true, uses a simple, imprecise but non-coordinate dependent, model of BBL</span>
<span id="L1709">                                ! mixing diffusivity based on Law of the Wall. Otherwise, uses the original BBL</span>
<span id="L1710">                                ! scheme.</span>
<span id="L1711">DRAG_DIFFUSIVITY_ANSWER_DATE = 20250101 ! default = 99991231</span>
<span id="L1712">                                ! The vintage of the order of arithmetic in the drag diffusivity calculations.</span>
<span id="L1713">                                ! Values above 20250301 use less confusing expressions to set the bottom-drag</span>
<span id="L1714">                                ! generated diffusivity when USE_LOTW_BBL_DIFFUSIVITY is false.</span>
<span id="L1715">DZ_BBL_AVG_MIN = 0.0            !   [m] default = 0.0</span>
<span id="L1716">                                ! A minimal distance over which to average to determine the average bottom</span>
<span id="L1717">                                ! boundary layer density.</span>
<span id="L1718">SIMPLE_TKE_TO_KD = False        !   [Boolean] default = False</span>
<span id="L1719">                                ! If true, uses a simple estimate of Kd/TKE that will work for arbitrary</span>
<span id="L1720">                                ! vertical coordinates. If false, calculates Kd/TKE and bounds based on exact</span>
<span id="L1721">                                ! energetics for an isopycnal layer-formulation.</span>
<span id="L1722"></span>
<span id="L1723">! === module MOM_bkgnd_mixing ===</span>
<span id="L1724">! Adding static vertical background mixing coefficients</span>
<span id="L1725">KD = 2.0E-05                    !   [m2 s-1] default = 0.0</span>
<span id="L1726">                                ! The background diapycnal diffusivity of density in the interior. Zero or the</span>
<span id="L1727">                                ! molecular value, ~1e-7 m2 s-1, may be used.</span>
<span id="L1728">KD_MIN = 2.0E-06                !   [m2 s-1] default = 2.0E-07</span>
<span id="L1729">                                ! The minimum diapycnal diffusivity.</span>
<span id="L1730">BRYAN_LEWIS_DIFFUSIVITY = False !   [Boolean] default = False</span>
<span id="L1731">                                ! If true, use a Bryan &amp; Lewis (JGR 1979) like tanh profile of background</span>
<span id="L1732">                                ! diapycnal diffusivity with depth. This is done via CVMix.</span>
<span id="L1733">HORIZ_VARYING_BACKGROUND = False !   [Boolean] default = False</span>
<span id="L1734">                                ! If true, apply vertically uniform, latitude-dependent background diffusivity,</span>
<span id="L1735">                                ! as described in Danabasoglu et al., 2012</span>
<span id="L1736">PRANDTL_BKGND = 1.0             !   [nondim] default = 1.0</span>
<span id="L1737">                                ! Turbulent Prandtl number used to convert vertical background diffusivities</span>
<span id="L1738">                                ! into viscosities.</span>
<span id="L1739">HENYEY_IGW_BACKGROUND = True    !   [Boolean] default = False</span>
<span id="L1740">                                ! If true, use a latitude-dependent scaling for the near surface background</span>
<span id="L1741">                                ! diffusivity, as described in Harrison &amp; Hallberg, JPO 2008.</span>
<span id="L1742">HENYEY_N0_2OMEGA = 20.0         !   [nondim] default = 20.0</span>
<span id="L1743">                                ! The ratio of the typical Buoyancy frequency to twice the Earth&#x27;s rotation</span>
<span id="L1744">                                ! period, used with the Henyey scaling from the mixing.</span>
<span id="L1745">HENYEY_MAX_LAT = 95.0           !   [degN] default = 95.0</span>
<span id="L1746">                                ! A latitude poleward of which the Henyey profile is returned to the minimum</span>
<span id="L1747">                                ! diffusivity</span>
<span id="L1748">KD_TANH_LAT_FN = False          !   [Boolean] default = False</span>
<span id="L1749">                                ! If true, use a tanh dependence of Kd_sfc on latitude, like CM2.1/CM2M.  There</span>
<span id="L1750">                                ! is no physical justification for this form, and it can not be used with</span>
<span id="L1751">                                ! HENYEY_IGW_BACKGROUND.</span>
<span id="L1752">KD_MAX = -1.0                   !   [m2 s-1] default = -1.0</span>
<span id="L1753">                                ! The maximum permitted increment for the diapycnal diffusivity from TKE-based</span>
<span id="L1754">                                ! parameterizations, or a negative value for no limit.</span>
<span id="L1755">KD_ADD = 0.0                    !   [m2 s-1] default = 0.0</span>
<span id="L1756">                                ! A uniform diapycnal diffusivity that is added everywhere without any filtering</span>
<span id="L1757">                                ! or scaling.</span>
<span id="L1758">USER_CHANGE_DIFFUSIVITY = False !   [Boolean] default = False</span>
<span id="L1759">                                ! If true, call user-defined code to change the diffusivity.</span>
<span id="L1760">DISSIPATION_MIN = 0.0           !   [W m-3] default = 0.0</span>
<span id="L1761">                                ! The minimum dissipation by which to determine a lower bound of Kd (a floor).</span>
<span id="L1762">DISSIPATION_N0 = 1.0E-07        !   [W m-3] default = 0.0</span>
<span id="L1763">                                ! The intercept when N=0 of the N-dependent expression used to set a minimum</span>
<span id="L1764">                                ! dissipation by which to determine a lower bound of Kd (a floor): A in eps_min</span>
<span id="L1765">                                ! = A + B*N.</span>
<span id="L1766">DISSIPATION_N1 = 6.0E-04        !   [J m-3] default = 0.0</span>
<span id="L1767">                                ! The coefficient multiplying N, following Gargett, used to set a minimum</span>
<span id="L1768">                                ! dissipation by which to determine a lower bound of Kd (a floor): B in eps_min</span>
<span id="L1769">                                ! = A + B*N</span>
<span id="L1770">DISSIPATION_KD_MIN = 0.0        !   [m2 s-1] default = 0.0</span>
<span id="L1771">                                ! The minimum vertical diffusivity applied as a floor.</span>
<span id="L1772">DOUBLE_DIFFUSION = False        !   [Boolean] default = False</span>
<span id="L1773">                                ! If true, increase diffusivites for temperature or salinity based on the</span>
<span id="L1774">                                ! double-diffusive parameterization described in Large et al. (1994).</span>
<span id="L1775"></span>
<span id="L1776">! === module MOM_kappa_shear ===</span>
<span id="L1777">! Parameterization of shear-driven turbulence following Jackson, Hallberg and Legg, JPO 2008</span>
<span id="L1778">USE_JACKSON_PARAM = True        !   [Boolean] default = False</span>
<span id="L1779">                                ! If true, use the Jackson-Hallberg-Legg (JPO 2008) shear mixing</span>
<span id="L1780">                                ! parameterization.</span>
<span id="L1781">VERTEX_SHEAR = False            !   [Boolean] default = False</span>
<span id="L1782">                                ! If true, do the calculations of the shear-driven mixing at the cell vertices</span>
<span id="L1783">                                ! (i.e., the vorticity points).</span>
<span id="L1784">VERTEX_SHEAR_THICKNESS_MEAN = False !   [Boolean] default = False</span>
<span id="L1785">                                ! If true, apply thickness weighting to horizontal averagings of diffusivity to</span>
<span id="L1786">                                ! tracer points in the kappa shear solver.</span>
<span id="L1787">RINO_CRIT = 0.25                !   [nondim] default = 0.25</span>
<span id="L1788">                                ! The critical Richardson number for shear mixing.</span>
<span id="L1789">SHEARMIX_RATE = 0.089           !   [nondim] default = 0.089</span>
<span id="L1790">                                ! A nondimensional rate scale for shear-driven entrainment. Jackson et al find</span>
<span id="L1791">                                ! values in the range of 0.085-0.089.</span>
<span id="L1792">MAX_RINO_IT = 25                !   [nondim] default = 50</span>
<span id="L1793">                                ! The maximum number of iterations that may be used to estimate the Richardson</span>
<span id="L1794">                                ! number driven mixing.</span>
<span id="L1795">KD_KAPPA_SHEAR_0 = 2.0E-05      !   [m2 s-1] default = 2.0E-05</span>
<span id="L1796">                                ! The background diffusivity that is used to smooth the density and shear</span>
<span id="L1797">                                ! profiles before solving for the diffusivities.  The default is the greater of</span>
<span id="L1798">                                ! KD and 1e-7 m2 s-1.</span>
<span id="L1799">KD_SEED_KAPPA_SHEAR = 1.0       !   [m2 s-1] default = 1.0</span>
<span id="L1800">                                ! A moderately large seed value of diapycnal diffusivity that is used as a</span>
<span id="L1801">                                ! starting turbulent diffusivity in the iterations to find an energetically</span>
<span id="L1802">                                ! constrained solution for the shear-driven diffusivity.</span>
<span id="L1803">KD_TRUNC_KAPPA_SHEAR = 2.0E-07  !   [m2 s-1] default = 2.0E-07</span>
<span id="L1804">                                ! The value of shear-driven diffusivity that is considered negligible and is</span>
<span id="L1805">                                ! rounded down to 0. The default is 1% of KD_KAPPA_SHEAR_0.</span>
<span id="L1806">FRI_CURVATURE = -0.97           !   [nondim] default = -0.97</span>
<span id="L1807">                                ! The nondimensional curvature of the function of the Richardson number in the</span>
<span id="L1808">                                ! kappa source term in the Jackson et al. scheme.</span>
<span id="L1809">TKE_N_DECAY_CONST = 0.24        !   [nondim] default = 0.24</span>
<span id="L1810">                                ! The coefficient for the decay of TKE due to stratification (i.e. proportional</span>
<span id="L1811">                                ! to N*tke). The values found by Jackson et al. are 0.24-0.28.</span>
<span id="L1812">TKE_SHEAR_DECAY_CONST = 0.14    !   [nondim] default = 0.14</span>
<span id="L1813">                                ! The coefficient for the decay of TKE due to shear (i.e. proportional to</span>
<span id="L1814">                                ! |S|*tke). The values found by Jackson et al. are 0.14-0.12.</span>
<span id="L1815">KAPPA_BUOY_SCALE_COEF = 0.82    !   [nondim] default = 0.82</span>
<span id="L1816">                                ! The coefficient for the buoyancy length scale in the kappa equation.  The</span>
<span id="L1817">                                ! values found by Jackson et al. are in the range of 0.81-0.86.</span>
<span id="L1818">KAPPA_N_OVER_S_SCALE_COEF2 = 0.0 !   [nondim] default = 0.0</span>
<span id="L1819">                                ! The square of the ratio of the coefficients of the buoyancy and shear scales</span>
<span id="L1820">                                ! in the diffusivity equation, Set this to 0 (the default) to eliminate the</span>
<span id="L1821">                                ! shear scale. This is only used if USE_JACKSON_PARAM is true.</span>
<span id="L1822">LZ_RESCALE = 1.0                !   [nondim] default = 1.0</span>
<span id="L1823">                                ! A coefficient to rescale the distance to the nearest solid boundary. This</span>
<span id="L1824">                                ! adjustment is to account for regions where 3 dimensional turbulence prevents</span>
<span id="L1825">                                ! the growth of shear instabilies [nondim].</span>
<span id="L1826">KAPPA_SHEAR_TOL_ERR = 0.1       !   [nondim] default = 0.1</span>
<span id="L1827">                                ! The fractional error in kappa that is tolerated. Iteration stops when changes</span>
<span id="L1828">                                ! between subsequent iterations are smaller than this everywhere in a column.</span>
<span id="L1829">                                ! The peak diffusivities usually converge most rapidly, and have much smaller</span>
<span id="L1830">                                ! errors than this.</span>
<span id="L1831">TKE_BACKGROUND = 0.0            !   [m2 s-2] default = 0.0</span>
<span id="L1832">                                ! A background level of TKE used in the first iteration of the kappa equation.</span>
<span id="L1833">                                ! TKE_BACKGROUND could be 0.</span>
<span id="L1834">KAPPA_SHEAR_ELIM_MASSLESS = True !   [Boolean] default = True</span>
<span id="L1835">                                ! If true, massless layers are merged with neighboring massive layers in this</span>
<span id="L1836">                                ! calculation.  The default is true and I can think of no good reason why it</span>
<span id="L1837">                                ! should be false. This is only used if USE_JACKSON_PARAM is true.</span>
<span id="L1838">MAX_KAPPA_SHEAR_IT = 13         ! default = 13</span>
<span id="L1839">                                ! The maximum number of iterations that may be used to estimate the</span>
<span id="L1840">                                ! time-averaged diffusivity.</span>
<span id="L1841">PRANDTL_TURB = 0.0              !   [nondim] default = 1.0</span>
<span id="L1842">                                ! The turbulent Prandtl number applied to shear instability.</span>
<span id="L1843">KAPPA_SHEAR_MAX_KAP_SRC_CHG = 10.0 !   [nondim] default = 10.0</span>
<span id="L1844">                                ! The maximum permitted increase in the kappa source within an iteration</span>
<span id="L1845">                                ! relative to the local source; this must be greater than 1.  The lower limit</span>
<span id="L1846">                                ! for the permitted fractional decrease is (1 - 0.5/kappa_src_max_chg).  These</span>
<span id="L1847">                                ! limits could perhaps be made dynamic with an improved iterative solver.</span>
<span id="L1848">KAPPA_SHEAR_ITER_BUG = False    !   [Boolean] default = False</span>
<span id="L1849">                                ! If true, use an older, dimensionally inconsistent estimate of the derivative</span>
<span id="L1850">                                ! of diffusivity with energy in the Newton&#x27;s method iteration.  The bug causes</span>
<span id="L1851">                                ! undercorrections when dz &gt; 1 m.</span>
<span id="L1852">KAPPA_SHEAR_ALL_LAYER_TKE_BUG = False !   [Boolean] default = False</span>
<span id="L1853">                                ! If true, report back the latest estimate of TKE instead of the time average</span>
<span id="L1854">                                ! TKE when there is mass in all layers.  Otherwise always report the time</span>
<span id="L1855">                                ! averaged TKE, as is currently done when there are some massless layers.</span>
<span id="L1856">USE_RESTRICTIVE_TOLERANCE_CHECK = False !   [Boolean] default = False</span>
<span id="L1857">                                ! If true, uses the more restrictive tolerance check to determine if a timestep</span>
<span id="L1858">                                ! is acceptable for the KS_it outer iteration loop.  False uses the original</span>
<span id="L1859">                                ! less restrictive check.</span>
<span id="L1860">KAPPA_SHEAR_MERGE_ML = True     !   [Boolean] default = True</span>
<span id="L1861">                                ! If true, combine the mixed layers together before solving the kappa-shear</span>
<span id="L1862">                                ! equations.</span>
<span id="L1863"></span>
<span id="L1864">! === module MOM_CVMix_shear ===</span>
<span id="L1865">! Parameterization of shear-driven turbulence via CVMix (various options)</span>
<span id="L1866">USE_LMD94 = False               !   [Boolean] default = False</span>
<span id="L1867">                                ! If true, use the Large-McWilliams-Doney (JGR 1994) shear mixing</span>
<span id="L1868">                                ! parameterization.</span>
<span id="L1869">USE_PP81 = False                !   [Boolean] default = False</span>
<span id="L1870">                                ! If true, use the Pacanowski and Philander (JPO 1981) shear mixing</span>
<span id="L1871">                                ! parameterization.</span>
<span id="L1872"></span>
<span id="L1873">! === module MOM_CVMix_ddiff ===</span>
<span id="L1874">! Parameterization of mixing due to double diffusion processes via CVMix</span>
<span id="L1875">USE_CVMIX_DDIFF = False         !   [Boolean] default = False</span>
<span id="L1876">                                ! If true, turns on double diffusive processes via CVMix. Note that double</span>
<span id="L1877">                                ! diffusive processes on viscosity are ignored in CVMix, see</span>
<span id="L1878">                                ! http://cvmix.github.io/ for justification.</span>
<span id="L1879"></span>
<span id="L1880">! === module MOM_diabatic_aux ===</span>
<span id="L1881">! The following parameters are used for auxiliary diabatic processes.</span>
<span id="L1882">RECLAIM_FRAZIL = True           !   [Boolean] default = True</span>
<span id="L1883">                                ! If true, try to use any frazil heat deficit to cool any overlying layers down</span>
<span id="L1884">                                ! to the freezing point, thereby avoiding the creation of thin ice when the SST</span>
<span id="L1885">                                ! is above the freezing point.</span>
<span id="L1886">SALT_EXTRACTION_LIMIT = 0.9999  !   [nondim] default = 0.9999</span>
<span id="L1887">                                ! An upper limit on the fraction of the salt in a layer that can be lost to the</span>
<span id="L1888">                                ! net surface salt fluxes within a timestep.</span>
<span id="L1889">PRESSURE_DEPENDENT_FRAZIL = False !   [Boolean] default = False</span>
<span id="L1890">                                ! If true, use a pressure dependent freezing temperature when making frazil. The</span>
<span id="L1891">                                ! default is false, which will be faster but is inappropriate with ice-shelf</span>
<span id="L1892">                                ! cavities.</span>
<span id="L1893">DO_BRINE_PLUME = False          !   [Boolean] default = False</span>
<span id="L1894">                                ! If true, use a brine plume parameterization from Nguyen et al., 2009.</span>
<span id="L1895">VAR_PEN_SW = True               !   [Boolean] default = False</span>
<span id="L1896">                                ! If true, use one of the CHL_A schemes specified by OPACITY_SCHEME to determine</span>
<span id="L1897">                                ! the e-folding depth of incoming short wave radiation.</span>
<span id="L1898">CHL_FROM_FILE = True            !   [Boolean] default = True</span>
<span id="L1899">                                ! If true, chl_a is read from a file.</span>
<span id="L1900">CHL_FILE = &quot;seawifs_1998-2006_GOLD_smoothed_2X.nc&quot; !</span>
<span id="L1901">                                ! CHL_FILE is the file containing chl_a concentrations in the variable CHL_A. It</span>
<span id="L1902">                                ! is used when VAR_PEN_SW and CHL_FROM_FILE are true.</span>
<span id="L1903">CHL_VARNAME = &quot;CHL_A&quot;           ! default = &quot;CHL_A&quot;</span>
<span id="L1904">                                ! Name of CHL_A variable in CHL_FILE.</span>
<span id="L1905"></span>
<span id="L1906">! === module MOM_mixed_layer ===</span>
<span id="L1907">NSTAR = 0.15                    !   [nondim] default = 0.15</span>
<span id="L1908">                                ! The portion of the buoyant potential energy imparted by surface fluxes that is</span>
<span id="L1909">                                ! available to drive entrainment at the base of mixed layer when that energy is</span>
<span id="L1910">                                ! positive.</span>
<span id="L1911">BULK_RI_ML = 0.05               !   [nondim]</span>
<span id="L1912">                                ! The efficiency with which mean kinetic energy released by mechanically forced</span>
<span id="L1913">                                ! entrainment of the mixed layer is converted to turbulent kinetic energy.</span>
<span id="L1914">ABSORB_ALL_SW = True            !   [Boolean] default = False</span>
<span id="L1915">                                ! If true,  all shortwave radiation is absorbed by the ocean, instead of passing</span>
<span id="L1916">                                ! through to the bottom mud.</span>
<span id="L1917">NSTAR2 = 0.15                   !   [nondim] default = 0.15</span>
<span id="L1918">                                ! The portion of any potential energy released by convective adjustment that is</span>
<span id="L1919">                                ! available to drive entrainment at the base of mixed layer. By default</span>
<span id="L1920">                                ! NSTAR2=NSTAR.</span>
<span id="L1921">BULK_RI_CONVECTIVE = 0.05       !   [nondim] default = 0.05</span>
<span id="L1922">                                ! The efficiency with which convectively released mean kinetic energy is</span>
<span id="L1923">                                ! converted to turbulent kinetic energy.  By default</span>
<span id="L1924">                                ! BULK_RI_CONVECTIVE=BULK_RI_ML.</span>
<span id="L1925">HMIX_MIN = 2.0                  !   [m] default = 0.0</span>
<span id="L1926">                                ! The minimum mixed layer depth if the mixed layer depth is determined</span>
<span id="L1927">                                ! dynamically.</span>
<span id="L1928">MECH_TKE_FLOOR = 1.0E-150       !   [m3 s-2] default = 1.0E-150</span>
<span id="L1929">                                ! A tiny floor on the amount of turbulent kinetic energy that is used when the</span>
<span id="L1930">                                ! mixed layer does not yet contain HMIX_MIN fluid.  The default is so small that</span>
<span id="L1931">                                ! its actual value is irrelevant, so long as it is greater than 0.</span>
<span id="L1932">LIMIT_BUFFER_DETRAIN = True     !   [Boolean] default = False</span>
<span id="L1933">                                ! If true, limit the detrainment from the buffer layers to not be too different</span>
<span id="L1934">                                ! from the neighbors.</span>
<span id="L1935">ALLOWED_DETRAIN_TEMP_CHG = 0.5  !   [K] default = 0.5</span>
<span id="L1936">                                ! The amount by which temperature is allowed to exceed previous values during</span>
<span id="L1937">                                ! detrainment.</span>
<span id="L1938">ALLOWED_DETRAIN_SALT_CHG = 0.1  !   [ppt] default = 0.1</span>
<span id="L1939">                                ! The amount by which salinity is allowed to exceed previous values during</span>
<span id="L1940">                                ! detrainment.</span>
<span id="L1941">ML_DT_DS_WEIGHT = 6.0           !   [degC ppt-1] default = 6.0</span>
<span id="L1942">                                ! When forced to extrapolate T &amp; S to match the layer densities, this factor (in</span>
<span id="L1943">                                ! deg C / PSU) is combined with the derivatives of density with T &amp; S to</span>
<span id="L1944">                                ! determine what direction is orthogonal to density contours. It should be a</span>
<span id="L1945">                                ! typical value of (dR/dS) / (dR/dT) in oceanic profiles.</span>
<span id="L1946">BUFFER_LAYER_EXTRAP_LIMIT = -1.0 !   [nondim] default = -1.0</span>
<span id="L1947">                                ! A limit on the density range over which extrapolation can occur when</span>
<span id="L1948">                                ! detraining from the buffer layers, relative to the density range within the</span>
<span id="L1949">                                ! mixed and buffer layers, when the detrainment is going into the lightest</span>
<span id="L1950">                                ! interior layer, nondimensional, or a negative value not to apply this limit.</span>
<span id="L1951">BUFFER_LAYER_HMIN_THICK = 5.0   !   [m] default = 5.0</span>
<span id="L1952">                                ! The minimum buffer layer thickness when the mixed layer is very thick.</span>
<span id="L1953">BUFFER_LAYER_HMIN_REL = 0.05    !   [nondim] default = 0.05</span>
<span id="L1954">                                ! The minimum buffer layer thickness relative to the combined mixed land buffer</span>
<span id="L1955">                                ! ayer thicknesses when they are thin.</span>
<span id="L1956">BUFFER_LAY_DETRAIN_TIME = 1.44E+04 !   [s] default = 1.44E+04</span>
<span id="L1957">                                ! A timescale that characterizes buffer layer detrainment events.</span>
<span id="L1958">BUFFER_SPLIT_RHO_TOL = 0.1      !   [nondim] default = 0.1</span>
<span id="L1959">                                ! The fractional tolerance for matching layer target densities when splitting</span>
<span id="L1960">                                ! layers to deal with massive interior layers that are lighter than one of the</span>
<span id="L1961">                                ! mixed or buffer layers.</span>
<span id="L1962">DEPTH_LIMIT_FLUXES = 0.1        !   [m] default = 0.2</span>
<span id="L1963">                                ! The surface fluxes are scaled away when the total ocean depth is less than</span>
<span id="L1964">                                ! DEPTH_LIMIT_FLUXES.</span>
<span id="L1965">ML_RESORT = True                !   [Boolean] default = False</span>
<span id="L1966">                                ! If true, resort the topmost layers by potential density before the mixed layer</span>
<span id="L1967">                                ! calculations.</span>
<span id="L1968">ML_PRESORT_NK_CONV_ADJ = 4      !   [nondim] default = 0</span>
<span id="L1969">                                ! Convectively mix the first ML_PRESORT_NK_CONV_ADJ layers before sorting when</span>
<span id="L1970">                                ! ML_RESORT is true.</span>
<span id="L1971">BML_USTAR_MIN = 1.45842E-18     !   [m s-1] default = 1.45842E-18</span>
<span id="L1972">                                ! The minimum value of ustar that should be used by the bulk mixed layer model</span>
<span id="L1973">                                ! in setting vertical TKE decay scales. This must be greater than 0.</span>
<span id="L1974">BML_NONBOUSINESQ = False        !   [Boolean] default = False</span>
<span id="L1975">                                ! If true, use non-Boussinesq expressions for the energetic calculations used in</span>
<span id="L1976">                                ! the bulk mixed layer calculations.</span>
<span id="L1977">RESOLVE_EKMAN = False           !   [Boolean] default = False</span>
<span id="L1978">                                ! If true, the NKML&gt;1 layers in the mixed layer are chosen to optimally</span>
<span id="L1979">                                ! represent the impact of the Ekman transport on the mixed layer TKE budget.</span>
<span id="L1980">                                ! Otherwise, the sublayers are distributed uniformly through the mixed layer.</span>
<span id="L1981">CORRECT_ABSORPTION_DEPTH = True !   [Boolean] default = False</span>
<span id="L1982">                                ! If true, the average depth at which penetrating shortwave radiation is</span>
<span id="L1983">                                ! absorbed is adjusted to match the average heating depth of an exponential</span>
<span id="L1984">                                ! profile by moving some of the heating upward in the water column.</span>
<span id="L1985">DO_RIVERMIX = True              !   [Boolean] default = False</span>
<span id="L1986">                                ! If true, apply additional mixing wherever there is runoff, so that it is mixed</span>
<span id="L1987">                                ! down to RIVERMIX_DEPTH, if the ocean is that deep.</span>
<span id="L1988">RIVERMIX_DEPTH = 40.0           !   [m] default = 0.0</span>
<span id="L1989">                                ! The depth to which rivers are mixed if DO_RIVERMIX is defined.</span>
<span id="L1990">USE_RIVER_HEAT_CONTENT = False  !   [Boolean] default = False</span>
<span id="L1991">                                ! If true, use the fluxes%runoff_Hflx field to set the heat carried by runoff,</span>
<span id="L1992">                                ! instead of using SST*CP*liq_runoff.</span>
<span id="L1993">USE_CALVING_HEAT_CONTENT = False !   [Boolean] default = False</span>
<span id="L1994">                                ! If true, use the fluxes%calving_Hflx field to set the heat carried by runoff,</span>
<span id="L1995">                                ! instead of using SST*CP*froz_runoff.</span>
<span id="L1996">BULKML_CONV_MOMENTUM_BUG = False !   [Boolean] default = False</span>
<span id="L1997">                                ! If true, use code with a bug that causes a loss of momentum conservation</span>
<span id="L1998">                                ! during mixedlayer convection.</span>
<span id="L1999">LIMIT_BUFFER_DET_DH_SFC = 0.5   !   [nondim] default = 0.5</span>
<span id="L2000">                                ! The fractional limit in the change between grid points of the surface region</span>
<span id="L2001">                                ! (mixed &amp; buffer layer) thickness.</span>
<span id="L2002">LIMIT_BUFFER_DET_DH_BATHY = 0.2 !   [nondim] default = 0.2</span>
<span id="L2003">                                ! The fraction of the total depth by which the thickness of the surface region</span>
<span id="L2004">                                ! (mixed &amp; buffer layer) is allowed to change between grid points.</span>
<span id="L2005"></span>
<span id="L2006">! === module MOM_regularize_layers ===</span>
<span id="L2007">REGULARIZE_SURFACE_LAYERS = False !   [Boolean] default = False</span>
<span id="L2008">                                ! If defined, vertically restructure the near-surface layers when they have too</span>
<span id="L2009">                                ! much lateral variations to allow for sensible lateral barotropic transports.</span>
<span id="L2010"></span>
<span id="L2011">! === module MOM_opacity ===</span>
<span id="L2012">OPACITY_SCHEME = &quot;MANIZZA_05&quot;   ! default = &quot;MANIZZA_05&quot;</span>
<span id="L2013">                                ! This character string specifies how chlorophyll concentrations are translated</span>
<span id="L2014">                                ! into opacities. Currently valid options include:</span>
<span id="L2015">                                !        MANIZZA_05 - Use Manizza et al., GRL, 2005.</span>
<span id="L2016">                                !        MOREL_88 - Use Morel, JGR, 1988.</span>
<span id="L2017">                                !        OHLMANN_03 - Use Ohlmann, J Clim, 2003. (only use if dz(1)&gt;2.0m)</span>
<span id="L2018">BLUE_FRAC_SW = 0.5              !   [nondim] default = 0.5</span>
<span id="L2019">                                ! The fraction of the penetrating shortwave radiation that is in the blue band.</span>
<span id="L2020">PEN_SW_NBANDS = 3               ! default = 1</span>
<span id="L2021">                                ! The number of bands of penetrating shortwave radiation.</span>
<span id="L2022">PEN_SW_FLUX_ABSORB = 2.5E-11    !   [degC m s-1] default = 2.5E-11</span>
<span id="L2023">                                ! A minimum remaining shortwave heating rate that will be simply absorbed in the</span>
<span id="L2024">                                ! next sufficiently thick layers for computational efficiency, instead of</span>
<span id="L2025">                                ! continuing to penetrate.  The default, 2.5e-11 degC m s-1, is about 1e-4 W m-2</span>
<span id="L2026">                                ! or 0.08 degC m century-1, but 0 is also a valid value.</span>
<span id="L2027">PEN_SW_ABSORB_MINTHICK = 1.0    !   [m] default = 1.0</span>
<span id="L2028">                                ! A thickness that is used to absorb the remaining penetrating shortwave heat</span>
<span id="L2029">                                ! flux when it drops below PEN_SW_FLUX_ABSORB.</span>
<span id="L2030">OPACITY_VALUES_MANIZZA = 0.0232, 0.074, 0.225, 0.037, 2.86, 0.0 !   [m-1] default = 0.0232, 0.074, 0.225, 0.037, 2.86, 0.0</span>
<span id="L2031">                                ! Pairs of opacity coefficients for blue, red and near-infrared radiation with</span>
<span id="L2032">                                ! parameterizations following the functional form from Manizza et al., GRL 2005,</span>
<span id="L2033">                                ! namely in the form opacity = coef_1 + coef_2 * chl**pow for each band.</span>
<span id="L2034">                                ! Although coefficients are set for 3 bands, more or less bands may actually be</span>
<span id="L2035">                                ! used, with extra bands following the same properties as band 3.</span>
<span id="L2036">CHOROPHYLL_POWER_MANIZZA = 0.674, 0.629, 0.0 !   [nondim] default = 0.674, 0.629, 0.0</span>
<span id="L2037">                                ! Powers of chlorophyll for blue, red and near-infrared radiation bands in</span>
<span id="L2038">                                ! expressions for opacity of the form opacity = coef_1 + coef_2 * chl**pow.</span>
<span id="L2039">OPACITY_BAND_WAVELENGTHS = 0.0, 550.0, 700.0, 2800.0 !   [nm] default = 0.0, 550.0, 700.0, 2800.0</span>
<span id="L2040">                                ! The bounding wavelengths for the various bands of shortwave radiation, with</span>
<span id="L2041">                                ! defaults that depend on the setting for OPACITY_SCHEME.</span>
<span id="L2042">OPACITY_LAND_VALUE = 10.0       !   [m-1] default = 10.0</span>
<span id="L2043">                                ! The value to use for opacity over land. The default is 10 m-1 - a value for</span>
<span id="L2044">                                ! muddy water.</span>
<span id="L2045"></span>
<span id="L2046">! === module MOM_tracer_advect ===</span>
<span id="L2047">TRACER_ADVECTION_SCHEME = &quot;PLM&quot; ! default = &quot;PLM&quot;</span>
<span id="L2048">                                ! The horizontal transport scheme for tracers:</span>
<span id="L2049">                                !   PLM    - Piecewise Linear Method</span>
<span id="L2050">                                !   PPM:H3 - Piecewise Parabolic Method (Huyhn 3rd order)</span>
<span id="L2051">                                !   PPM    - Piecewise Parabolic Method (Colella-Woodward)</span>
<span id="L2052"></span>
<span id="L2053">! === module MOM_tracer_hor_diff ===</span>
<span id="L2054">KHTR = 10.0                     !   [m2 s-1] default = 0.0</span>
<span id="L2055">                                ! The background along-isopycnal tracer diffusivity.</span>
<span id="L2056">KHTR_MIN = 50.0                 !   [m2 s-1] default = 0.0</span>
<span id="L2057">                                ! The minimum along-isopycnal tracer diffusivity.</span>
<span id="L2058">FULL_DEPTH_KHTR_MIN = False     !   [Boolean] default = False</span>
<span id="L2059">                                ! If true, KHTR_MIN is enforced throughout the whole water column. Otherwise,</span>
<span id="L2060">                                ! KHTR_MIN is only enforced at the surface. This parameter is only available</span>
<span id="L2061">                                ! when KHTR_USE_EBT_STRUCT=True and KHTR_MIN&gt;0.</span>
<span id="L2062">KHTR_MAX = 900.0                !   [m2 s-1] default = 0.0</span>
<span id="L2063">                                ! The maximum along-isopycnal tracer diffusivity. Set to a positive value to</span>
<span id="L2064">                                ! activate.</span>
<span id="L2065">KHTR_PASSIVITY_COEFF = 3.0      !   [nondim] default = 0.0</span>
<span id="L2066">                                ! The coefficient that scales deformation radius over grid-spacing in passivity,</span>
<span id="L2067">                                ! where passivity is the ratio between along isopycnal mixing of tracers to</span>
<span id="L2068">                                ! thickness mixing. A non-zero value enables this parameterization.</span>
<span id="L2069">KHTR_PASSIVITY_MIN = 0.5        !   [nondim] default = 0.5</span>
<span id="L2070">                                ! The minimum passivity which is the ratio between along isopycnal mixing of</span>
<span id="L2071">                                ! tracers to thickness mixing.</span>
<span id="L2072">DIFFUSE_ML_TO_INTERIOR = True   !   [Boolean] default = False</span>
<span id="L2073">                                ! If true, enable epipycnal mixing between the surface boundary layer and the</span>
<span id="L2074">                                ! interior.</span>
<span id="L2075">CHECK_DIFFUSIVE_CFL = False     !   [Boolean] default = False</span>
<span id="L2076">                                ! If true, use enough iterations the diffusion to ensure that the diffusive</span>
<span id="L2077">                                ! equivalent of the CFL limit is not violated.  If false, always use the greater</span>
<span id="L2078">                                ! of 1 or MAX_TR_DIFFUSION_CFL iteration.</span>
<span id="L2079">MAX_TR_DIFFUSION_CFL = -1.0     !   [nondim] default = -1.0</span>
<span id="L2080">                                ! If positive, locally limit the along-isopycnal tracer diffusivity to keep the</span>
<span id="L2081">                                ! diffusive CFL locally at or below this value.  The number of diffusive</span>
<span id="L2082">                                ! iterations is often this value or the next greater integer.</span>
<span id="L2083">RECALC_NEUTRAL_SURF = False     !   [Boolean] default = False</span>
<span id="L2084">                                ! If true, then recalculate the neutral surfaces if the</span>
<span id="L2085">                                ! diffusive CFL is exceeded. If false, assume that the</span>
<span id="L2086">                                ! positions of the surfaces do not change</span>
<span id="L2087">HOR_DIFF_ANSWER_DATE = 20240101 ! default = 99991231</span>
<span id="L2088">                                ! The vintage of the order of arithmetic to use for the tracer diffusion.</span>
<span id="L2089">                                ! Values of 20240330 or below recover the answers from the original form of the</span>
<span id="L2090">                                ! along-isopycnal mixed layer to interior mixing code, while higher values use</span>
<span id="L2091">                                ! mathematically equivalent expressions that recover rotational symmetry when</span>
<span id="L2092">                                ! DIFFUSE_ML_TO_INTERIOR is true.</span>
<span id="L2093">HOR_DIFF_LIMIT_BUG = True       !   [Boolean] default = False</span>
<span id="L2094">                                ! If true and the answer date is 20240330 or below, use a rotational symmetry</span>
<span id="L2095">                                ! breaking bug when limiting the tracer properties in tracer_epipycnal_ML_diff.</span>
<span id="L2096">ML_KHTR_SCALE = 0.0             !   [nondim] default = 1.0</span>
<span id="L2097">                                ! With Diffuse_ML_interior, the ratio of the truly horizontal diffusivity in the</span>
<span id="L2098">                                ! mixed layer to the epipycnal diffusivity.  The valid range is 0 to 1.</span>
<span id="L2099"></span>
<span id="L2100">! === module MOM_neutral_diffusion ===</span>
<span id="L2101">! This module implements neutral diffusion of tracers</span>
<span id="L2102">USE_NEUTRAL_DIFFUSION = False   !   [Boolean] default = False</span>
<span id="L2103">                                ! If true, enables the neutral diffusion module.</span>
<span id="L2104"></span>
<span id="L2105">! === module MOM_hor_bnd_diffusion ===</span>
<span id="L2106">! This module implements horizontal diffusion of tracers near boundaries</span>
<span id="L2107">USE_HORIZONTAL_BOUNDARY_DIFFUSION = False !   [Boolean] default = False</span>
<span id="L2108">                                ! If true, enables the horizonal boundary tracer&#x27;s diffusion module.</span>
<span id="L2109">OBSOLETE_DIAGNOSTIC_IS_FATAL = True !   [Boolean] default = True</span>
<span id="L2110">                                ! If an obsolete diagnostic variable appears in the diag_table, cause a FATAL</span>
<span id="L2111">                                ! error rather than issue a WARNING.</span>
<span id="L2112"></span>
<span id="L2113">! === module MOM_sum_output ===</span>
<span id="L2114">CALCULATE_APE = True            !   [Boolean] default = True</span>
<span id="L2115">                                ! If true, calculate the available potential energy of the interfaces.  Setting</span>
<span id="L2116">                                ! this to false reduces the memory footprint of high-PE-count models</span>
<span id="L2117">                                ! dramatically.</span>
<span id="L2118">WRITE_STOCKS = True             !   [Boolean] default = True</span>
<span id="L2119">                                ! If true, write the integrated tracer amounts to stdout when the energy files</span>
<span id="L2120">                                ! are written.</span>
<span id="L2121">MAXTRUNC = 5000                 !   [truncations save_interval-1] default = 0</span>
<span id="L2122">                                ! The run will be stopped, and the day set to a very large value if the velocity</span>
<span id="L2123">                                ! is truncated more than MAXTRUNC times between energy saves.  Set MAXTRUNC to 0</span>
<span id="L2124">                                ! to stop if there is any truncation of velocities.</span>
<span id="L2125">MAX_ENERGY = 0.0                !   [m2 s-2] default = 0.0</span>
<span id="L2126">                                ! The maximum permitted average energy per unit mass; the model will be stopped</span>
<span id="L2127">                                ! if there is more energy than this.  If zero or negative, this is set to</span>
<span id="L2128">                                ! 10*MAXVEL^2.</span>
<span id="L2129">MAXVEL = 6.0                    !   [m s-1] default = 3.0E+08</span>
<span id="L2130">                                ! The maximum velocity allowed before the velocity components are truncated.</span>
<span id="L2131">ENERGYFILE = &quot;ocean.stats&quot;      ! default = &quot;ocean.stats&quot;</span>
<span id="L2132">                                ! The file to use to write the energies and globally summed diagnostics.</span>
<span id="L2133">DATE_STAMPED_STDOUT = True      !   [Boolean] default = True</span>
<span id="L2134">                                ! If true, use dates (not times) in messages to stdout</span>
<span id="L2135">ISO_DATE_STAMPED_STDOUT = False !   [Boolean] default = False</span>
<span id="L2136">                                ! If true, use ISO formatted dates in messages to stdout</span>
<span id="L2137">TIMEUNIT = 8.64E+04             !   [s] default = 8.64E+04</span>
<span id="L2138">                                ! The time unit in seconds a number of input fields</span>
<span id="L2139">READ_DEPTH_LIST = False         !   [Boolean] default = False</span>
<span id="L2140">                                ! Read the depth list from a file if it exists or create that file otherwise.</span>
<span id="L2141">DEPTH_LIST_MIN_INC = 1.0E-10    !   [m] default = 1.0E-10</span>
<span id="L2142">                                ! The minimum increment between the depths of the entries in the depth-list</span>
<span id="L2143">                                ! file.</span>
<span id="L2144">ENERGYSAVEDAYS = 0.25           !   [days] default = 1.0</span>
<span id="L2145">                                ! The interval in units of TIMEUNIT between saves of the energies of the run and</span>
<span id="L2146">                                ! other globally summed diagnostics.</span>
<span id="L2147">ENERGYSAVEDAYS_GEOMETRIC = 0.0  !   [days] default = 0.0</span>
<span id="L2148">                                ! The starting interval in units of TIMEUNIT for the first call to save the</span>
<span id="L2149">                                ! energies of the run and other globally summed diagnostics. The interval</span>
<span id="L2150">                                ! increases by a factor of 2. after each call to write_energy.</span>
<span id="L2151"></span>
<span id="L2152">! === module ocean_stochastics_init ===</span>
<span id="L2153">DO_SPPT = False                 !   [Boolean] default = False</span>
<span id="L2154">                                ! If true, then stochastically perturb the thermodynamic tendencies of T,S, amd</span>
<span id="L2155">                                ! h.  Amplitude and correlations are controlled by the nam_stoch namelist in the</span>
<span id="L2156">                                ! UFS model only.</span>
<span id="L2157">DO_SKEB = False                 !   [Boolean] default = False</span>
<span id="L2158">                                ! If true, then stochastically perturb the currents using the stochastic kinetic</span>
<span id="L2159">                                ! energy backscatter scheme.</span>
<span id="L2160">PERT_EPBL = False               !   [Boolean] default = False</span>
<span id="L2161">                                ! If true, then stochastically perturb the kinetic energy production and</span>
<span id="L2162">                                ! dissipation terms.  Amplitude and correlations are controlled by the nam_stoch</span>
<span id="L2163">                                ! namelist in the UFS model only.</span>
<span id="L2164"></span>
<span id="L2165">! === module MOM_surface_forcing ===</span>
<span id="L2166">VARIABLE_WINDS = True           !   [Boolean] default = True</span>
<span id="L2167">                                ! If true, the winds vary in time after the initialization.</span>
<span id="L2168">VARIABLE_BUOYFORCE = True       !   [Boolean] default = True</span>
<span id="L2169">                                ! If true, the buoyancy forcing varies in time after the initialization of the</span>
<span id="L2170">                                ! model.</span>
<span id="L2171">BUOY_CONFIG = &quot;file&quot;            ! default = &quot;zero&quot;</span>
<span id="L2172">                                ! The character string that indicates how buoyancy forcing is specified.  Valid</span>
<span id="L2173">                                ! options include (file), (data_override), (zero), (const), (linear), (MESO),</span>
<span id="L2174">                                ! (SCM_CVmix_tests), (BFB), (dumbbell), (USER) and (NONE).</span>
<span id="L2175">ARCHAIC_OMIP_FORCING_FILE = False !   [Boolean] default = True</span>
<span id="L2176">                                ! If true, use the forcing variable decomposition from the old German OMIP</span>
<span id="L2177">                                ! prescription that predated CORE. If false, use the variable groupings</span>
<span id="L2178">                                ! available from MOM output diagnostics of forcing variables.</span>
<span id="L2179">LONGWAVE_FILE = &quot;ocean_forcing_daily.nc&quot; !</span>
<span id="L2180">                                ! The file with the longwave heat flux, in the variable given by</span>
<span id="L2181">                                ! LONGWAVE_FORCING_VAR.</span>
<span id="L2182">LONGWAVE_FORCING_VAR = &quot;LW&quot;     ! default = &quot;LW&quot;</span>
<span id="L2183">                                ! The variable with the longwave forcing field.</span>
<span id="L2184">LONGWAVE_FILE_DAYS_PER_RECORD = 0 ! default = 0</span>
<span id="L2185">                                ! If positive the number of days of longwave fluxes per time level in</span>
<span id="L2186">                                ! LONGWAVE_FILE, or if negative the number of time levels per day.  If 31 change</span>
<span id="L2187">                                ! forcing monthly, or if 0 the model will guess the right value based on the</span>
<span id="L2188">                                ! file size.</span>
<span id="L2189">SHORTWAVE_FILE = &quot;ocean_forcing_daily.nc&quot; !</span>
<span id="L2190">                                ! The file with the shortwave heat flux, in the variable given by</span>
<span id="L2191">                                ! SHORTWAVE_FORCING_VAR.</span>
<span id="L2192">SHORTWAVE_FORCING_VAR = &quot;SW&quot;    ! default = &quot;SW&quot;</span>
<span id="L2193">                                ! The variable with the shortwave forcing field.</span>
<span id="L2194">SHORTWAVE_FILE_DAYS_PER_RECORD = 0 ! default = 0</span>
<span id="L2195">                                ! If positive the number of days of shortwave fluxes per time level in</span>
<span id="L2196">                                ! SHORTWAVE_FILE, or if negative the number of time levels per day.  If 31</span>
<span id="L2197">                                ! change forcing monthly, or if 0 the model will guess the right value based on</span>
<span id="L2198">                                ! the file size.</span>
<span id="L2199">EVAPORATION_FILE = &quot;ocean_forcing_daily.nc&quot; !</span>
<span id="L2200">                                ! The file with the evaporative moisture flux, in the variable given by</span>
<span id="L2201">                                ! EVAP_FORCING_VAR.</span>
<span id="L2202">EVAP_FORCING_VAR = &quot;evap&quot;       ! default = &quot;evap&quot;</span>
<span id="L2203">                                ! The variable with the evaporative moisture flux.</span>
<span id="L2204">EVAPORATION_FILE_DAYS_PER_RECORD = 0 ! default = 0</span>
<span id="L2205">                                ! If positive the number of days of evaporation per time level in</span>
<span id="L2206">                                ! EVAPORATION_FILE, or if negative the number of time levels per day.  If 31</span>
<span id="L2207">                                ! change forcing monthly, or if 0 the model will guess the right value based on</span>
<span id="L2208">                                ! the file size.</span>
<span id="L2209">LATENTHEAT_FILE = &quot;ocean_forcing_daily.nc&quot; !</span>
<span id="L2210">                                ! The file with the latent heat flux, in the variable given by</span>
<span id="L2211">                                ! LATENT_FORCING_VAR.</span>
<span id="L2212">LATENT_FORCING_VAR = &quot;latent&quot;   ! default = &quot;latent&quot;</span>
<span id="L2213">                                ! The variable with the latent heat flux.</span>
<span id="L2214">LATENTHEAT_FILE_DAYS_PER_RECORD = 0 ! default = 0</span>
<span id="L2215">                                ! If positive the number of days of latent heat fluxes per time level in</span>
<span id="L2216">                                ! LATENTHEAT_FILE, or if negative the number of time levels per day.  If 31</span>
<span id="L2217">                                ! change forcing monthly, or if 0 the model will guess the right value based on</span>
<span id="L2218">                                ! the file size.</span>
<span id="L2219">SENSIBLEHEAT_FILE = &quot;ocean_forcing_daily.nc&quot; !</span>
<span id="L2220">                                ! The file with the sensible heat flux, in the variable given by</span>
<span id="L2221">                                ! SENSIBLE_FORCING_VAR.</span>
<span id="L2222">SENSIBLE_FORCING_VAR = &quot;sensible&quot; ! default = &quot;sensible&quot;</span>
<span id="L2223">                                ! The variable with the sensible heat flux.</span>
<span id="L2224">SENSIBLEHEAT_FILE_DAYS_PER_RECORD = 0 ! default = 0</span>
<span id="L2225">                                ! If positive the number of days of sensible heat fluxes per time level in</span>
<span id="L2226">                                ! SENSIBLEHEAT_FILE, or if negative the number of time levels per day.  If 31</span>
<span id="L2227">                                ! change forcing monthly, or if 0 the model will guess the right value based on</span>
<span id="L2228">                                ! the file size.</span>
<span id="L2229">RAIN_FILE = &quot;ocean_precip_monthly.nc&quot; !</span>
<span id="L2230">                                ! The file with the liquid precipitation flux, in the variable given by</span>
<span id="L2231">                                ! RAIN_FORCING_VAR.</span>
<span id="L2232">RAIN_FORCING_VAR = &quot;liq_precip&quot; ! default = &quot;liq_precip&quot;</span>
<span id="L2233">                                ! The variable with the liquid precipitation flux.</span>
<span id="L2234">RAIN_FILE_DAYS_PER_RECORD = 0   ! default = 0</span>
<span id="L2235">                                ! If positive the number of days of rain fluxes per time level in RAIN_FILE, or</span>
<span id="L2236">                                ! if negative the number of time levels per day.  If 31 change forcing monthly,</span>
<span id="L2237">                                ! or if 0 the model will guess the right value based on the file size.</span>
<span id="L2238">SNOW_FILE = &quot;ocean_precip_monthly.nc&quot; !</span>
<span id="L2239">                                ! The file with the frozen precipitation flux, in the variable given by</span>
<span id="L2240">                                ! SNOW_FORCING_VAR.</span>
<span id="L2241">SNOW_FORCING_VAR = &quot;froz_precip&quot; ! default = &quot;froz_precip&quot;</span>
<span id="L2242">                                ! The variable with the frozen precipitation flux.</span>
<span id="L2243">RUNOFF_FILE = &quot;ocean_precip_monthly.nc&quot; !</span>
<span id="L2244">                                ! The file with the fresh and frozen runoff/calving fluxes, in variables given</span>
<span id="L2245">                                ! by LIQ_RUNOFF_FORCING_VAR and FROZ_RUNOFF_FORCING_VAR.</span>
<span id="L2246">LIQ_RUNOFF_FORCING_VAR = &quot;liq_runoff&quot; ! default = &quot;liq_runoff&quot;</span>
<span id="L2247">                                ! The variable with the liquid runoff flux.</span>
<span id="L2248">FROZ_RUNOFF_FORCING_VAR = &quot;froz_runoff&quot; ! default = &quot;froz_runoff&quot;</span>
<span id="L2249">                                ! The variable with the frozen runoff flux.</span>
<span id="L2250">RUNOFF_FILE_DAYS_PER_RECORD = 0 ! default = 0</span>
<span id="L2251">                                ! If positive the number of days of runoff per time level in RUNOFF_FILE, or if</span>
<span id="L2252">                                ! negative the number of time levels per day.  If 31 change forcing monthly, or</span>
<span id="L2253">                                ! if 0 the model will guess the right value based on the file size.</span>
<span id="L2254">SSTRESTORE_FILE = &quot;ocean_forcing_daily.nc&quot; !</span>
<span id="L2255">                                ! The file with the SST toward which to restore in the variable given by</span>
<span id="L2256">                                ! SST_RESTORE_VAR.</span>
<span id="L2257">SALINITYRESTORE_FILE = &quot;ocean_forcing_daily.nc&quot; !</span>
<span id="L2258">                                ! The file with the surface salinity toward which to restore in the variable</span>
<span id="L2259">                                ! given by SSS_RESTORE_VAR.</span>
<span id="L2260">SST_RESTORE_VAR = &quot;SST&quot;         ! default = &quot;SST&quot;</span>
<span id="L2261">                                ! The variable with the SST toward which to restore.</span>
<span id="L2262">SSTRESTORE_FILE_DAYS_PER_RECORD = 0 ! default = 0</span>
<span id="L2263">                                ! If positive the number of days of SST per time level in SSTRESTORE_FILE, or if</span>
<span id="L2264">                                ! negative the number of time levels per day.  If 31 change forcing monthly, or</span>
<span id="L2265">                                ! if 0 the model will guess the right value based on the file size.</span>
<span id="L2266">SSS_RESTORE_VAR = &quot;SSS&quot;         ! default = &quot;SSS&quot;</span>
<span id="L2267">                                ! The variable with the SSS toward which to restore.</span>
<span id="L2268">SALINITYRESTORE_FILE_DAYS_PER_RECORD = 0 ! default = 0</span>
<span id="L2269">                                ! If positive the number of days of salinity per time level in</span>
<span id="L2270">                                ! SALINITYRESTORE_FILE, or if negative the number of time levels per day.  If 31</span>
<span id="L2271">                                ! change forcing monthly, or if 0 the model will guess the right value based on</span>
<span id="L2272">                                ! the file size.</span>
<span id="L2273">WIND_CONFIG = &quot;file&quot;            ! default = &quot;zero&quot;</span>
<span id="L2274">                                ! The character string that indicates how wind forcing is specified.  Valid</span>
<span id="L2275">                                ! options include (file), (data_override), (2gyre), (1gyre), (gyres), (zero),</span>
<span id="L2276">                                ! (const), (Neverworld), (scurves), (ideal_hurr), (SCM_CVmix_tests) and (USER).</span>
<span id="L2277">WIND_FILE = &quot;ocean_forcing_daily.nc&quot; !</span>
<span id="L2278">                                ! The file in which the wind stresses are found in variables STRESS_X and</span>
<span id="L2279">                                ! STRESS_Y.</span>
<span id="L2280">WINDSTRESS_X_VAR = &quot;taux&quot;       ! default = &quot;STRESS_X&quot;</span>
<span id="L2281">                                ! The name of the x-wind stress variable in WIND_FILE.</span>
<span id="L2282">WINDSTRESS_Y_VAR = &quot;tauy&quot;       ! default = &quot;STRESS_Y&quot;</span>
<span id="L2283">                                ! The name of the y-wind stress variable in WIND_FILE.</span>
<span id="L2284">WIND_STAGGER = &quot;C&quot;              ! default = &quot;C&quot;</span>
<span id="L2285">                                ! A character indicating how the wind stress components are staggered in</span>
<span id="L2286">                                ! WIND_FILE.  This may be A or C for now.</span>
<span id="L2287">WINDSTRESS_SCALE = 1.0          !   [nondim] default = 1.0</span>
<span id="L2288">                                ! A value by which the wind stresses in WIND_FILE are rescaled.</span>
<span id="L2289">USTAR_FORCING_VAR = &quot;&quot;          ! default = &quot;&quot;</span>
<span id="L2290">                                ! The name of the friction velocity variable in WIND_FILE or blank to get ustar</span>
<span id="L2291">                                ! from the wind stresses plus the gustiness.</span>
<span id="L2292">WIND_FILE_DAYS_PER_RECORD = 0   ! default = 0</span>
<span id="L2293">                                ! If positive the number of days of wind stress per time level in WIND_FILE, or</span>
<span id="L2294">                                ! if negative the number of time levels per day.  If 31 change forcing monthly,</span>
<span id="L2295">                                ! or if 0 the model will guess the right value based on the file size.</span>
<span id="L2296">RESTOREBUOY = True              !   [Boolean] default = False</span>
<span id="L2297">                                ! If true, the buoyancy fluxes drive the model back toward some specified</span>
<span id="L2298">                                ! surface state with a rate given by FLUXCONST.</span>
<span id="L2299">LATENT_HEAT_FUSION = 3.34E+05   !   [J/kg] default = 3.34E+05</span>
<span id="L2300">                                ! The latent heat of fusion.</span>
<span id="L2301">LATENT_HEAT_VAPORIZATION = 2.5E+06 !   [J/kg] default = 2.5E+06</span>
<span id="L2302">                                ! The latent heat of fusion.</span>
<span id="L2303">FLUXCONST = 0.5                 !   [m day-1] default = 0.0</span>
<span id="L2304">                                ! The constant that relates the restoring surface fluxes to the relative surface</span>
<span id="L2305">                                ! anomalies (akin to a piston velocity).  Note the non-MKS units.</span>
<span id="L2306">FLUXCONST_T = 0.5               !   [m day-1] default = 0.5</span>
<span id="L2307">                                ! The constant that relates the restoring surface temperature flux to the</span>
<span id="L2308">                                ! relative surface anomaly (akin to a piston velocity).  Note the non-MKS units.</span>
<span id="L2309">FLUXCONST_S = 0.5               !   [m day-1] default = 0.5</span>
<span id="L2310">                                ! The constant that relates the restoring surface salinity flux to the relative</span>
<span id="L2311">                                ! surface anomaly (akin to a piston velocity).  Note the non-MKS units.</span>
<span id="L2312">RESTORE_FLUX_RHO = 1024.0       !   [kg m-3] default = 1024.0</span>
<span id="L2313">                                ! The density that is used to convert piston velocities into salt or heat fluxes</span>
<span id="L2314">                                ! with RESTORE_SALINITY or RESTORE_TEMPERATURE.</span>
<span id="L2315">GUST_CONST = 0.0                !   [Pa] default = 0.0</span>
<span id="L2316">                                ! The background gustiness in the winds.</span>
<span id="L2317">USTAR_GUSTLESS_BUG = False      !   [Boolean] default = False</span>
<span id="L2318">                                ! If true include a bug in the time-averaging of the gustless wind friction</span>
<span id="L2319">                                ! velocity</span>
<span id="L2320">READ_GUST_2D = True             !   [Boolean] default = False</span>
<span id="L2321">                                ! If true, use a 2-dimensional gustiness supplied from an input file</span>
<span id="L2322">GUST_2D_FILE = &quot;gustiness_qscat.nc&quot; !</span>
<span id="L2323">                                ! The file in which the wind gustiness is found in variable gustiness.</span>
<span id="L2324"></span>
<span id="L2325">! === module MOM_restart ===</span>
<span id="L2326">USE_WAVES = False               !   [Boolean] default = False</span>
<span id="L2327">                                ! If true, enables surface wave modules.</span>
<span id="L2328"></span>
<span id="L2329">! === module MOM_main (MOM_driver) ===</span>
<span id="L2330">DT_FORCING = 7200.0             !   [s] default = 3600.0</span>
<span id="L2331">                                ! The time step for changing forcing, coupling with other components, or</span>
<span id="L2332">                                ! potentially writing certain diagnostics. The default value is given by DT.</span>
<span id="L2333">DAYMAX = 1.0                    !   [days]</span>
<span id="L2334">                                ! The final time of the whole simulation, in units of TIMEUNIT seconds.  This</span>
<span id="L2335">                                ! also sets the potential end time of the present run segment if the end time is</span>
<span id="L2336">                                ! not set via ocean_solo_nml in input.nml.</span>
<span id="L2337">SINGLE_STEPPING_CALL = True     !   [Boolean] default = True</span>
<span id="L2338">                                ! If true, advance the state of MOM with a single step including both dynamics</span>
<span id="L2339">                                ! and thermodynamics.  If false the two phases are advanced with separate calls.</span>
<span id="L2340">RESTART_CONTROL = 3             ! default = 1</span>
<span id="L2341">                                ! An integer whose bits encode which restart files are written. Add 2 (bit 1)</span>
<span id="L2342">                                ! for a time-stamped file, and odd (bit 0) for a non-time-stamped file. A</span>
<span id="L2343">                                ! non-time-stamped restart file is saved at the end of the run segment for any</span>
<span id="L2344">                                ! non-negative value.</span>
<span id="L2345">RESTINT = 365.0                 !   [days] default = 0.0</span>
<span id="L2346">                                ! The interval between saves of the restart file in units of TIMEUNIT.  Use 0</span>
<span id="L2347">                                ! (the default) to not save incremental restart files at all.</span>
<span id="L2348">WRITE_CPU_STEPS = 1000          ! default = 1000</span>
<span id="L2349">                                ! The number of coupled timesteps between writing the cpu time. If this is not</span>
<span id="L2350">                                ! positive, do not check cpu time, and the segment run-length can not be set via</span>
<span id="L2351">                                ! an elapsed CPU time.</span>
<span id="L2352"></span>
<span id="L2353">! === module MOM_write_cputime ===</span>
<span id="L2354">MAXCPU = 2.88E+04               !   [wall-clock seconds] default = -1.0</span>
<span id="L2355">                                ! The maximum amount of cpu time per processor for which MOM should run before</span>
<span id="L2356">                                ! saving a restart file and quitting with a return value that indicates that a</span>
<span id="L2357">                                ! further run is required to complete the simulation. If automatic restarts are</span>
<span id="L2358">                                ! not desired, use a negative value for MAXCPU.  MAXCPU has units of wall-clock</span>
<span id="L2359">                                ! seconds, so the actual CPU time used is larger by a factor of the number of</span>
<span id="L2360">                                ! processors used.</span>
<span id="L2361">CPU_TIME_FILE = &quot;CPU_stats&quot;     ! default = &quot;CPU_stats&quot;</span>
<span id="L2362">                                ! The file into which CPU time is written.</span>
<span id="L2363"></span>
<span id="L2364">! === module MOM_file_parser ===</span>
<span id="L2365">SEND_LOG_TO_STDOUT = False      !   [Boolean] default = False</span>
<span id="L2366">                                ! If true, all log messages are also sent to stdout.</span>
<span id="L2367">DOCUMENT_FILE = &quot;MOM_parameter_doc&quot; ! default = &quot;MOM_parameter_doc&quot;</span>
<span id="L2368">                                ! The basename for files where run-time parameters, their settings, units and</span>
<span id="L2369">                                ! defaults are documented. Blank will disable all parameter documentation.</span>
<span id="L2370">COMPLETE_DOCUMENTATION = True   !   [Boolean] default = True</span>
<span id="L2371">                                ! If true, all run-time parameters are documented in MOM_parameter_doc.all .</span>
<span id="L2372">MINIMAL_DOCUMENTATION = True    !   [Boolean] default = True</span>
<span id="L2373">                                ! If true, non-default run-time parameters are documented in</span>
<span id="L2374">                                ! MOM_parameter_doc.short .</span>
</pre>
