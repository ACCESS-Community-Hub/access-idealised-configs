---
search:
  exclude: true
---

# benchmark: MOM_parameter_doc.all

Every MOM6 parameter of the tested run of [benchmark](../mom6examples/benchmark.md), as MOM6 wrote it to `MOM_parameter_doc.all` in the run's output folder. Line numbers match the file.

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
<span id="L62">DT = 900.0                      !   [s]</span>
<span id="L63">                                ! The (baroclinic) dynamics time step.  The time-step that is actually used will</span>
<span id="L64">                                ! be an integer fraction of the forcing time-step (DT_FORCING in ocean-only mode</span>
<span id="L65">                                ! or the coupling timestep in coupled mode.)</span>
<span id="L66">DT_THERM = 3600.0               !   [s] default = 900.0</span>
<span id="L67">                                ! The thermodynamic time step. Ideally DT_THERM should be an integer multiple of</span>
<span id="L68">                                ! DT and of DT_TRACER_ADVECT and less than the forcing or coupling time-step.</span>
<span id="L69">                                ! However, if THERMO_SPANS_COUPLING is true, DT_THERM can be an integer multiple</span>
<span id="L70">                                ! of the coupling timestep. By default DT_THERM is set to DT.</span>
<span id="L71">THERMO_SPANS_COUPLING = False   !   [Boolean] default = False</span>
<span id="L72">                                ! If true, the MOM will take thermodynamic timesteps that can be longer than the</span>
<span id="L73">                                ! coupling timestep. The actual thermodynamic timestep that is used in this case</span>
<span id="L74">                                ! is the largest integer multiple of the coupling timestep that is less than or</span>
<span id="L75">                                ! equal to DT_THERM.</span>
<span id="L76">DT_TRACER_ADVECT = 3600.0       !   [s] default = 3600.0</span>
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
<span id="L103">DTBT_RESET_PERIOD = 0.0         !   [s] default = 3600.0</span>
<span id="L104">                                ! The period between recalculations of DTBT (if DTBT &lt;= 0). If DTBT_RESET_PERIOD</span>
<span id="L105">                                ! is negative, DTBT is set based only on information available at</span>
<span id="L106">                                ! initialization.  If 0, DTBT will be set every dynamics time step. The default</span>
<span id="L107">                                ! is set by DT_THERM.  This is only used if SPLIT is true.</span>
<span id="L108">FRAZIL = True                   !   [Boolean] default = False</span>
<span id="L109">                                ! If true, water freezes if it gets too cold, and the accumulated heat deficit</span>
<span id="L110">                                ! is returned in the surface state.  FRAZIL is only used if</span>
<span id="L111">                                ! ENABLE_THERMODYNAMICS is true.</span>
<span id="L112">DO_GEOTHERMAL = False           !   [Boolean] default = False</span>
<span id="L113">                                ! If true, apply geothermal heating.</span>
<span id="L114">BOUND_SALINITY = False          !   [Boolean] default = False</span>
<span id="L115">                                ! If true, limit salinity to being positive. (The sea-ice model may ask for more</span>
<span id="L116">                                ! salt than is available and drive the salinity negative otherwise.)</span>
<span id="L117">SALINITY_UNDERFLOW = 0.0        !   [PPT] default = 0.0</span>
<span id="L118">                                ! A tiny value of salinity below which the it is set to 0.  For reference, one</span>
<span id="L119">                                ! molecule of salt per square meter of ocean is of order 1e-29 ppt.</span>
<span id="L120">TEMPERATURE_UNDERFLOW = 0.0     !   [degC] default = 0.0</span>
<span id="L121">                                ! A tiny magnitude of temperatures below which they are set to 0.</span>
<span id="L122">C_P = 3925.0                    !   [J kg-1 K-1] default = 3991.86795711963</span>
<span id="L123">                                ! The heat capacity of sea water, approximated as a constant. This is only used</span>
<span id="L124">                                ! if ENABLE_THERMODYNAMICS is true. The default value is from the TEOS-10</span>
<span id="L125">                                ! definition of conservative temperature.</span>
<span id="L126">USE_PSURF_IN_EOS = True         !   [Boolean] default = True</span>
<span id="L127">                                ! If true, always include the surface pressure contributions in equation of</span>
<span id="L128">                                ! state calculations.</span>
<span id="L129">P_REF = 2.0E+07                 !   [Pa] default = 2.0E+07</span>
<span id="L130">                                ! The pressure that is used for calculating the coordinate density.  (1 Pa = 1e4</span>
<span id="L131">                                ! dbar, so 2e7 is commonly used.) This is only used if USE_EOS and</span>
<span id="L132">                                ! ENABLE_THERMODYNAMICS are true.</span>
<span id="L133">NONBLOCKING_P_SURF_BUG = True   !   [Boolean] default = True</span>
<span id="L134">                                ! If true, recover a bug in which the non-blocking halo update of the surface</span>
<span id="L135">                                ! pressure is not completed before the halo points of forces%p_surf are copied</span>
<span id="L136">                                ! into tv%p_surf, so that those halo points hold the surface pressure from the</span>
<span id="L137">                                ! previous coupling step, or zeros on the first step after a restart.  This is</span>
<span id="L138">                                ! only used if NONBLOCKING_UPDATES and USE_PSURF_IN_EOS are true</span>
<span id="L139">NKML = 2                        !   [nondim] default = 2</span>
<span id="L140">                                ! The number of sublayers within the mixed layer if BULKMIXEDLAYER is true.</span>
<span id="L141">NKBL = 2                        !   [nondim] default = 2</span>
<span id="L142">                                ! The number of layers that are used as variable density buffer layers if</span>
<span id="L143">                                ! BULKMIXEDLAYER is true.</span>
<span id="L144">FIRST_DIRECTION = 0             ! default = 0</span>
<span id="L145">                                ! An integer that indicates which direction goes first in parts of the code that</span>
<span id="L146">                                ! use directionally split updates, with even numbers (or 0) used for x- first</span>
<span id="L147">                                ! and odd numbers used for y-first.</span>
<span id="L148">ALTERNATE_FIRST_DIRECTION = False !   [Boolean] default = False</span>
<span id="L149">                                ! If true, after every dynamic timestep alternate whether the x- or y- direction</span>
<span id="L150">                                ! updates occur first in directionally split parts of the calculation. If this</span>
<span id="L151">                                ! is true, FIRST_DIRECTION applies at the start of a new run or if the next</span>
<span id="L152">                                ! first direction can not be found in the restart file.</span>
<span id="L153">CHECK_BAD_SURFACE_VALS = False  !   [Boolean] default = False</span>
<span id="L154">                                ! If true, check the surface state for ridiculous values.</span>
<span id="L155">DEFAULT_ANSWER_DATE = 99991231  ! default = 99991231</span>
<span id="L156">                                ! This sets the default value for the various _ANSWER_DATE parameters.</span>
<span id="L157">SURFACE_ANSWER_DATE = 99991231  ! default = 99991231</span>
<span id="L158">                                ! The vintage of the expressions for the surface properties.  Values below</span>
<span id="L159">                                ! 20190101 recover the answers from the end of 2018, while higher values use</span>
<span id="L160">                                ! updated and more robust forms of the same expressions.</span>
<span id="L161">SAVE_INITIAL_CONDS = True       !   [Boolean] default = False</span>
<span id="L162">                                ! If true, write the initial conditions to a file given by IC_OUTPUT_FILE.</span>
<span id="L163">IC_OUTPUT_FILE = &quot;GOLD_IC&quot;      ! default = &quot;MOM_IC&quot;</span>
<span id="L164">                                ! The file into which to write the initial conditions.</span>
<span id="L165">WRITE_GEOM = 1                  ! default = 1</span>
<span id="L166">                                ! If =0, never write the geometry and vertical grid files. If =1, write the</span>
<span id="L167">                                ! geometry and vertical grid files only for a new simulation. If =2, always</span>
<span id="L168">                                ! write the geometry and vertical grid files. Other values are invalid.</span>
<span id="L169">GEOM_FILE = &quot;ocean_geometry&quot;    ! default = &quot;ocean_geometry&quot;</span>
<span id="L170">                                ! The file into which to write the ocean geometry.</span>
<span id="L171">USE_DBCLIENT = False            !   [Boolean] default = False</span>
<span id="L172">                                ! If true, initialize a client to a remote database that can be used for online</span>
<span id="L173">                                ! analysis and machine-learning inference.</span>
<span id="L174">ICE_SHELF = False               !   [Boolean] default = False</span>
<span id="L175">                                ! If true, enables the ice shelf model.</span>
<span id="L176">USE_PARTICLES = False           !   [Boolean] default = False</span>
<span id="L177">                                ! If true, use the particles package.</span>
<span id="L178">USE_UH_PARTICLES = False        !   [Boolean] default = False</span>
<span id="L179">                                ! If true, use the uh velocity in the particles package.</span>
<span id="L180">ENSEMBLE_OCEAN = False          !   [Boolean] default = False</span>
<span id="L181">                                ! If False, The model is being run in serial mode as a single realization. If</span>
<span id="L182">                                ! True, The current model realization is part of a larger ensemble and at the</span>
<span id="L183">                                ! end of step MOM, we will perform a gather of the ensemble members for</span>
<span id="L184">                                ! statistical evaluation and/or data assimilation.</span>
<span id="L185">HOMOGENIZE_FORCINGS = False     !   [Boolean] default = False</span>
<span id="L186">                                ! If True, homogenize the forces and fluxes.</span>
<span id="L187"></span>
<span id="L188">! === module MOM_domains ===</span>
<span id="L189">REENTRANT_X = True              !   [Boolean] default = True</span>
<span id="L190">                                ! If true, the domain is zonally reentrant.</span>
<span id="L191">REENTRANT_Y = False             !   [Boolean] default = False</span>
<span id="L192">                                ! If true, the domain is meridionally reentrant.</span>
<span id="L193">TRIPOLAR_N = False              !   [Boolean] default = False</span>
<span id="L194">                                ! Use tripolar connectivity at the northern edge of the domain.  With</span>
<span id="L195">                                ! TRIPOLAR_N, NIGLOBAL must be even.</span>
<span id="L196">NIGLOBAL = 360                  !</span>
<span id="L197">                                ! The total number of thickness grid points in the x-direction in the physical</span>
<span id="L198">                                ! domain. With STATIC_MEMORY_ this is set in MOM_memory.h at compile time.</span>
<span id="L199">NJGLOBAL = 180                  !</span>
<span id="L200">                                ! The total number of thickness grid points in the y-direction in the physical</span>
<span id="L201">                                ! domain. With STATIC_MEMORY_ this is set in MOM_memory.h at compile time.</span>
<span id="L202">NIHALO = 4                      ! default = 4</span>
<span id="L203">                                ! The number of halo points on each side in the x-direction.  How this is set</span>
<span id="L204">                                ! varies with the calling component and static or dynamic memory configuration.</span>
<span id="L205">NJHALO = 4                      ! default = 4</span>
<span id="L206">                                ! The number of halo points on each side in the y-direction.  How this is set</span>
<span id="L207">                                ! varies with the calling component and static or dynamic memory configuration.</span>
<span id="L208"></span>
<span id="L209">! === module MOM_hor_index ===</span>
<span id="L210">! Sets the horizontal array index types.</span>
<span id="L211"></span>
<span id="L212">! === module MOM_grid ===</span>
<span id="L213">! Parameters providing information about the lateral grid.</span>
<span id="L214">REFERENCE_HEIGHT = 0.0          !   [m] default = 0.0</span>
<span id="L215">                                ! A reference value for geometric height fields, such as bathyT.</span>
<span id="L216"></span>
<span id="L217">! === module MOM_fixed_initialization ===</span>
<span id="L218">INPUTDIR = &quot;INPUT&quot;              ! default = &quot;.&quot;</span>
<span id="L219">                                ! The directory in which input files are found.</span>
<span id="L220"></span>
<span id="L221">! === module MOM_grid_init ===</span>
<span id="L222">GRID_CONFIG = &quot;mercator&quot;        !</span>
<span id="L223">                                ! A character string that determines the method for defining the horizontal</span>
<span id="L224">                                ! grid.  Current options are:</span>
<span id="L225">                                !     mosaic - read the grid from a mosaic (supergrid)</span>
<span id="L226">                                !              file set by GRID_FILE.</span>
<span id="L227">                                !     cartesian - use a (flat) Cartesian grid.</span>
<span id="L228">                                !     spherical - use a simple spherical grid.</span>
<span id="L229">                                !     mercator - use a Mercator spherical grid.</span>
<span id="L230">SOUTHLAT = -41.0                !   [degrees_N]</span>
<span id="L231">                                ! The southern latitude of the domain.</span>
<span id="L232">LENLAT = 41.0                   !   [degrees_N]</span>
<span id="L233">                                ! The latitudinal length of the domain.</span>
<span id="L234">WESTLON = 0.0                   !   [degrees_E] default = 0.0</span>
<span id="L235">                                ! The western longitude of the domain.</span>
<span id="L236">LENLON = 90.0                   !   [degrees_E]</span>
<span id="L237">                                ! The longitudinal length of the domain.</span>
<span id="L238">RAD_EARTH = 6.378E+06           !   [m] default = 6.378E+06</span>
<span id="L239">                                ! The radius of the Earth.</span>
<span id="L240">ISOTROPIC = True                !   [Boolean] default = False</span>
<span id="L241">                                ! If true, an isotropic grid on a sphere (also known as a Mercator grid) is</span>
<span id="L242">                                ! used. With an isotropic grid, the meridional extent of the domain (LENLAT),</span>
<span id="L243">                                ! the zonal extent (LENLON), and the number of grid points in each direction are</span>
<span id="L244">                                ! _not_ independent. In MOM the meridional extent is determined to fit the zonal</span>
<span id="L245">                                ! extent and the number of grid points, while grid is perfectly isotropic.</span>
<span id="L246">EQUATOR_REFERENCE = True        !   [Boolean] default = True</span>
<span id="L247">                                ! If true, the grid is defined to have the equator at the nearest q- or h- grid</span>
<span id="L248">                                ! point to (-LOWLAT*NJGLOBAL/LENLAT).</span>
<span id="L249">LAT_ENHANCE_FACTOR = 1.0        !   [nondim] default = 1.0</span>
<span id="L250">                                ! The amount by which the meridional resolution is enhanced within</span>
<span id="L251">                                ! LAT_EQ_ENHANCE of the equator.</span>
<span id="L252">LAT_EQ_ENHANCE = 0.0            !   [degrees_N] default = 0.0</span>
<span id="L253">                                ! The latitude range to the north and south of the equator over which the</span>
<span id="L254">                                ! resolution is enhanced.</span>
<span id="L255">TOPO_CONFIG = &quot;benchmark&quot;       !</span>
<span id="L256">                                ! This specifies how bathymetry is specified:</span>
<span id="L257">                                !     file - read bathymetric information from the file</span>
<span id="L258">                                !       specified by (TOPO_FILE).</span>
<span id="L259">                                !     flat - flat bottom set to MAXIMUM_DEPTH.</span>
<span id="L260">                                !     bowl - an analytically specified bowl-shaped basin</span>
<span id="L261">                                !       ranging between MAXIMUM_DEPTH and MINIMUM_DEPTH.</span>
<span id="L262">                                !     spoon - a similar shape to &#x27;bowl&#x27;, but with an vertical</span>
<span id="L263">                                !       wall at the southern face.</span>
<span id="L264">                                !     halfpipe - a zonally uniform channel with a half-sine</span>
<span id="L265">                                !       profile in the meridional direction.</span>
<span id="L266">                                !     bbuilder - build topography from list of functions.</span>
<span id="L267">                                !     benchmark - use the benchmark test case topography.</span>
<span id="L268">                                !     Neverworld - use the Neverworld test case topography.</span>
<span id="L269">                                !     DOME - use a slope and channel configuration for the</span>
<span id="L270">                                !       DOME sill-overflow test case.</span>
<span id="L271">                                !     ISOMIP - use a slope and channel configuration for the</span>
<span id="L272">                                !       ISOMIP test case.</span>
<span id="L273">                                !     DOME2D - use a shelf and slope configuration for the</span>
<span id="L274">                                !       DOME2D gravity current/overflow test case.</span>
<span id="L275">                                !     Kelvin - flat but with rotated land mask.</span>
<span id="L276">                                !     seamount - Gaussian bump for spontaneous motion test case.</span>
<span id="L277">                                !     dumbbell - Sloshing channel with reservoirs on both ends.</span>
<span id="L278">                                !     shelfwave - exponential slope for shelfwave test case.</span>
<span id="L279">                                !     Phillips - ACC-like idealized topography used in the Phillips config.</span>
<span id="L280">                                !     dense - Denmark Strait-like dense water formation and overflow.</span>
<span id="L281">                                !     USER - call a user modified routine.</span>
<span id="L282"></span>
<span id="L283">! === module benchmark_initialize_topography ===</span>
<span id="L284">MINIMUM_DEPTH = 1.0             !   [m] default = 0.0</span>
<span id="L285">                                ! The minimum depth of the ocean.</span>
<span id="L286">MAXIMUM_DEPTH = 5500.0          !   [m]</span>
<span id="L287">                                ! The maximum depth of the ocean.</span>
<span id="L288"></span>
<span id="L289">! === module MOM_open_boundary ===</span>
<span id="L290">! Controls where open boundaries are located, what kind of boundary condition to impose, and what data to apply,</span>
<span id="L291">! if any.</span>
<span id="L292">OBC_NUMBER_OF_SEGMENTS = 0      ! default = 0</span>
<span id="L293">                                ! The number of open boundary segments.</span>
<span id="L294">MASKING_DEPTH = -9999.0         !   [m] default = -9999.0</span>
<span id="L295">                                ! The depth below which to mask points as land points, for which all fluxes are</span>
<span id="L296">                                ! zeroed out. MASKING_DEPTH is ignored if it has the special default value.</span>
<span id="L297">CHANNEL_CONFIG = &quot;none&quot;         ! default = &quot;none&quot;</span>
<span id="L298">                                ! A parameter that determines which set of channels are</span>
<span id="L299">                                ! restricted to specific  widths.  Options are:</span>
<span id="L300">                                !     none - All channels have the grid width.</span>
<span id="L301">                                !     global_1deg - Sets 16 specific channels appropriate</span>
<span id="L302">                                !       for a 1-degree model, as used in CM2G.</span>
<span id="L303">                                !     list - Read the channel locations and widths from a</span>
<span id="L304">                                !       text file, like MOM_channel_list in the MOM_SIS</span>
<span id="L305">                                !       test case.</span>
<span id="L306">                                !     file - Read open face widths everywhere from a</span>
<span id="L307">                                !       NetCDF file on the model grid.</span>
<span id="L308">SUBGRID_TOPO_AT_VEL = False     !   [Boolean] default = False</span>
<span id="L309">                                ! If true, use variables from TOPO_AT_VEL_FILE as parameters for porous barrier.</span>
<span id="L310">ROTATION = &quot;2omegasinlat&quot;       ! default = &quot;2omegasinlat&quot;</span>
<span id="L311">                                ! This specifies how the Coriolis parameter is specified:</span>
<span id="L312">                                !     2omegasinlat - Use twice the planetary rotation rate</span>
<span id="L313">                                !       times the sine of latitude.</span>
<span id="L314">                                !     betaplane - Use a beta-plane or f-plane.</span>
<span id="L315">                                !     USER - call a user modified routine.</span>
<span id="L316">OMEGA = 7.2921E-05              !   [s-1] default = 7.2921E-05</span>
<span id="L317">                                ! The rotation rate of the earth.</span>
<span id="L318">GRID_ROTATION_ANGLE_BUGS = False !   [Boolean] default = False</span>
<span id="L319">                                ! If true, use an older algorithm to calculate the sine and cosines needed</span>
<span id="L320">                                ! rotate between grid-oriented directions and true north and east.  Differences</span>
<span id="L321">                                ! arise at the tripolar fold.</span>
<span id="L322"></span>
<span id="L323">! === module MOM_verticalGrid ===</span>
<span id="L324">! Parameters providing information about the vertical grid.</span>
<span id="L325">G_EARTH = 9.8                   !   [m s-2] default = 9.8</span>
<span id="L326">                                ! The gravitational acceleration of the Earth.</span>
<span id="L327">RHO_0 = 1035.0                  !   [kg m-3] default = 1035.0</span>
<span id="L328">                                ! The mean ocean density used with BOUSSINESQ true to calculate accelerations</span>
<span id="L329">                                ! and the mass for conservation properties, or with BOUSSINSEQ false to convert</span>
<span id="L330">                                ! some parameters from vertical units of m to kg m-2.</span>
<span id="L331">BOUSSINESQ = True               !   [Boolean] default = True</span>
<span id="L332">                                ! If true, make the Boussinesq approximation.</span>
<span id="L333">ANGSTROM = 1.0E-10              !   [m] default = 1.0E-10</span>
<span id="L334">                                ! The minimum layer thickness, usually one-Angstrom.</span>
<span id="L335">H_TO_M = 1.0                    !   [m H-1] default = 1.0</span>
<span id="L336">                                ! A constant that translates the model&#x27;s internal units of thickness into m.</span>
<span id="L337">NK = 22                         !   [nondim]</span>
<span id="L338">                                ! The number of model layers.</span>
<span id="L339">ADVECTION_SCHEME_VARIANCE_UNDERFLOW = 1.0E-23 !   [Conc2 (tracer dependent)] default = 1.0E-23</span>
<span id="L340">                                ! A tiny magnitude for variance used to determine when advection scheme variance</span>
<span id="L341">                                ! production is set to 0.</span>
<span id="L342"></span>
<span id="L343">! === module MOM_tracer_registry ===</span>
<span id="L344"></span>
<span id="L345">! === module MOM_EOS ===</span>
<span id="L346">EQN_OF_STATE = &quot;WRIGHT&quot;         ! default = &quot;WRIGHT_FULL&quot;</span>
<span id="L347">                                ! EQN_OF_STATE determines which ocean equation of state should be used.</span>
<span id="L348">                                ! Currently, the valid choices are &quot;LINEAR&quot;, &quot;UNESCO&quot;, &quot;JACKETT_MCD&quot;, &quot;WRIGHT&quot;,</span>
<span id="L349">                                ! &quot;WRIGHT_REDUCED&quot;, &quot;WRIGHT_FULL&quot;, &quot;NEMO&quot;, &quot;ROQUET_RHO&quot;, &quot;ROQUET_SPV&quot; and</span>
<span id="L350">                                ! &quot;TEOS10&quot;.  This is only used if USE_EOS is true.</span>
<span id="L351">USE_WRIGHT_2ND_DERIV_BUG = False !   [Boolean] default = False</span>
<span id="L352">                                ! If true, use a bug in the calculation of the second derivatives of density</span>
<span id="L353">                                ! with temperature and with temperature and pressure that causes some terms to</span>
<span id="L354">                                ! be only 2/3 of what they should be.</span>
<span id="L355">EOS_QUADRATURE = False          !   [Boolean] default = False</span>
<span id="L356">                                ! If true, always use the generic (quadrature) code code for the integrals of</span>
<span id="L357">                                ! density.</span>
<span id="L358">TFREEZE_FORM = &quot;LINEAR&quot;         ! default = &quot;LINEAR&quot;</span>
<span id="L359">                                ! TFREEZE_FORM determines which expression should be used for the freezing</span>
<span id="L360">                                ! point.  Currently, the valid choices are &quot;LINEAR&quot;, &quot;MILLERO_78&quot;, &quot;TEOS_POLY&quot;,</span>
<span id="L361">                                ! &quot;TEOS10&quot;</span>
<span id="L362">TFREEZE_S0_P0 = 0.0             !   [degC] default = 0.0</span>
<span id="L363">                                ! When TFREEZE_FORM=LINEAR, this is the freezing potential temperature at S=0,</span>
<span id="L364">                                ! P=0.</span>
<span id="L365">DTFREEZE_DS = -0.054            !   [degC ppt-1] default = -0.054</span>
<span id="L366">                                ! When TFREEZE_FORM=LINEAR, this is the derivative of the freezing potential</span>
<span id="L367">                                ! temperature with salinity.</span>
<span id="L368">DTFREEZE_DP = 0.0               !   [degC Pa-1] default = 0.0</span>
<span id="L369">                                ! When TFREEZE_FORM=LINEAR, this is the derivative of the freezing potential</span>
<span id="L370">                                ! temperature with pressure.</span>
<span id="L371">TFREEZE_S_IS_PRACS = True       !   [Boolean] default = True</span>
<span id="L372">                                ! When True, the model will check if the model internal salinity is practical</span>
<span id="L373">                                ! salinity.  If the model uses absolute salinity, a conversion will be applied.</span>
<span id="L374">TFREEZE_T_IS_POTT = True        !   [Boolean] default = True</span>
<span id="L375">                                ! When True, the model will check if the model internal temperature is potential</span>
<span id="L376">                                ! temperature.  If the model uses conservative temperature, a conversion will be</span>
<span id="L377">                                ! applied.</span>
<span id="L378"></span>
<span id="L379">! === module MOM_restart ===</span>
<span id="L380">PARALLEL_RESTARTFILES = False   !   [Boolean] default = False</span>
<span id="L381">                                ! If true, the IO layout is used to group processors that write to the same</span>
<span id="L382">                                ! restart file or each processor writes its own (numbered) restart file. If</span>
<span id="L383">                                ! false, a single restart file is generated combining output from all PEs.</span>
<span id="L384">RESTARTFILE = &quot;MOM.res&quot;         ! default = &quot;MOM.res&quot;</span>
<span id="L385">                                ! The name-root of the restart file.</span>
<span id="L386">MAX_FIELDS = 100                ! default = 100</span>
<span id="L387">                                ! The maximum number of restart fields that can be used.</span>
<span id="L388">RESTART_CHECKSUMS_REQUIRED = True !   [Boolean] default = True</span>
<span id="L389">                                ! If true, require the restart checksums to match and error out otherwise. Users</span>
<span id="L390">                                ! may want to avoid this comparison if for example the restarts are made from a</span>
<span id="L391">                                ! run with a different mask_table than the current run, in which case the</span>
<span id="L392">                                ! checksums will not match and cause crash.</span>
<span id="L393">RESTART_SYMMETRIC_CHECKSUMS = False !   [Boolean] default = False</span>
<span id="L394">                                ! If true, do the restart checksums on all the edge points for a non-reentrant</span>
<span id="L395">                                ! grid.  This requires that SYMMETRIC_MEMORY_ is defined at compile time.</span>
<span id="L396">RESTART_UNSIGNED_ZEROS = False  !   [Boolean] default = False</span>
<span id="L397">                                ! If true, convert any negative zeros that would be written to the restart file</span>
<span id="L398">                                ! into ordinary unsigned zeros.  This does not change answers, but it can be</span>
<span id="L399">                                ! helpful in comparing restart files after grid rotation, for example.</span>
<span id="L400">USE_FILTER = False              !   [Boolean] default = False</span>
<span id="L401">                                ! If true, use streaming band-pass filters to detect the instantaneous tidal</span>
<span id="L402">                                ! signals in the simulation.</span>
<span id="L403"></span>
<span id="L404">! === module MOM_tracer_flow_control ===</span>
<span id="L405">USE_USER_TRACER_EXAMPLE = False !   [Boolean] default = False</span>
<span id="L406">                                ! If true, use the USER_tracer_example tracer package.</span>
<span id="L407">USE_DOME_TRACER = False         !   [Boolean] default = False</span>
<span id="L408">                                ! If true, use the DOME_tracer tracer package.</span>
<span id="L409">USE_ISOMIP_TRACER = False       !   [Boolean] default = False</span>
<span id="L410">                                ! If true, use the ISOMIP_tracer tracer package.</span>
<span id="L411">USE_RGC_TRACER = False          !   [Boolean] default = False</span>
<span id="L412">                                ! If true, use the RGC_tracer tracer package.</span>
<span id="L413">USE_IDEAL_AGE_TRACER = True     !   [Boolean] default = False</span>
<span id="L414">                                ! If true, use the ideal_age_example tracer package.</span>
<span id="L415">USE_MARBL_TRACERS = False       !   [Boolean] default = False</span>
<span id="L416">                                ! If true, use the MARBL tracer package.</span>
<span id="L417">USE_REGIONAL_DYES = False       !   [Boolean] default = False</span>
<span id="L418">                                ! If true, use the regional_dyes tracer package.</span>
<span id="L419">USE_FILE_DYES = False           !   [Boolean] default = False</span>
<span id="L420">                                ! If true, use the file dyes tracer package.</span>
<span id="L421">USE_OIL_TRACER = False          !   [Boolean] default = False</span>
<span id="L422">                                ! If true, use the oil_tracer tracer package.</span>
<span id="L423">USE_ADVECTION_TEST_TRACER = False !   [Boolean] default = False</span>
<span id="L424">                                ! If true, use the advection_test_tracer tracer package.</span>
<span id="L425">USE_OCMIP2_CFC = False          !   [Boolean] default = False</span>
<span id="L426">                                ! If true, use the MOM_OCMIP2_CFC tracer package.</span>
<span id="L427">USE_CFC_CAP = False             !   [Boolean] default = False</span>
<span id="L428">                                ! If true, use the MOM_CFC_cap tracer package.</span>
<span id="L429">USE_generic_tracer = False      !   [Boolean] default = False</span>
<span id="L430">                                ! If true and _USE_GENERIC_TRACER is defined as a preprocessor macro, use the</span>
<span id="L431">                                ! MOM_generic_tracer packages.</span>
<span id="L432">USE_PSEUDO_SALT_TRACER = False  !   [Boolean] default = False</span>
<span id="L433">                                ! If true, use the pseudo salt tracer, typically run as a diagnostic.</span>
<span id="L434">USE_BOUNDARY_IMPULSE_TRACER = False !   [Boolean] default = False</span>
<span id="L435">                                ! If true, use the boundary impulse tracer.</span>
<span id="L436">USE_DYED_OBC_TRACER = False     !   [Boolean] default = False</span>
<span id="L437">                                ! If true, use the dyed_obc_tracer tracer package.</span>
<span id="L438">USE_NW2_TRACERS = False         !   [Boolean] default = False</span>
<span id="L439">                                ! If true, use the NeverWorld2 tracers.</span>
<span id="L440"></span>
<span id="L441">! === module ideal_age_example ===</span>
<span id="L442">DO_IDEAL_AGE = True             !   [Boolean] default = True</span>
<span id="L443">                                ! If true, use an ideal age tracer that is set to 0 age in the boundary layer</span>
<span id="L444">                                ! and ages at unit rate in the interior.</span>
<span id="L445">DO_IDEAL_VINTAGE = False        !   [Boolean] default = False</span>
<span id="L446">                                ! If true, use an ideal vintage tracer that is set to an exponentially</span>
<span id="L447">                                ! increasing value in the boundary layer and is conserved thereafter.</span>
<span id="L448">DO_IDEAL_AGE_DATED = False      !   [Boolean] default = False</span>
<span id="L449">                                ! If true, use an ideal age tracer that is everywhere 0 before</span>
<span id="L450">                                ! IDEAL_AGE_DATED_START_YEAR, but the behaves like the standard ideal age tracer</span>
<span id="L451">                                ! - i.e. is set to 0 age in the boundary layer and ages at unit rate in the</span>
<span id="L452">                                ! interior.</span>
<span id="L453">DO_BL_RESIDENCE = False         !   [Boolean] default = False</span>
<span id="L454">                                ! If true, use a residence tracer that is set to 0 age in the interior and ages</span>
<span id="L455">                                ! at unit rate in the boundary layer.</span>
<span id="L456">USE_REAL_BL_DEPTH = False       !   [Boolean] default = False</span>
<span id="L457">                                ! If true, the ideal age tracers will use the boundary layer depth diagnosed</span>
<span id="L458">                                ! from the BL or bulkmixedlayer scheme.</span>
<span id="L459">AGE_IC_FILE = &quot;&quot;                ! default = &quot;&quot;</span>
<span id="L460">                                ! The file in which the age-tracer initial values can be found, or an empty</span>
<span id="L461">                                ! string for internal initialization.</span>
<span id="L462">AGE_IC_FILE_IS_Z = False        !   [Boolean] default = False</span>
<span id="L463">                                ! If true, AGE_IC_FILE is in depth space, not layer space</span>
<span id="L464">TRACERS_MAY_REINIT = False      !   [Boolean] default = False</span>
<span id="L465">                                ! If true, tracers may go through the initialization code if they are not found</span>
<span id="L466">                                ! in the restart files.  Otherwise it is a fatal error if the tracers are not</span>
<span id="L467">                                ! found in the restart files of a restarted run.</span>
<span id="L468"></span>
<span id="L469">! === module MOM_coord_initialization ===</span>
<span id="L470">COORD_CONFIG = &quot;ts_range&quot;       ! default = &quot;none&quot;</span>
<span id="L471">                                ! This specifies how layers are to be defined:</span>
<span id="L472">                                !     ALE or none - used to avoid defining layers in ALE mode</span>
<span id="L473">                                !     file - read coordinate information from the file</span>
<span id="L474">                                !       specified by (COORD_FILE).</span>
<span id="L475">                                !     BFB - Custom coords for buoyancy-forced basin case</span>
<span id="L476">                                !       based on SST_S, T_BOT and DRHO_DT.</span>
<span id="L477">                                !     linear - linear based on interfaces not layers</span>
<span id="L478">                                !     layer_ref - linear based on layer densities</span>
<span id="L479">                                !     ts_ref - use reference temperature and salinity</span>
<span id="L480">                                !     ts_range - use range of temperature and salinity</span>
<span id="L481">                                !       (T_REF and S_REF) to determine surface density</span>
<span id="L482">                                !       and GINT calculate internal densities.</span>
<span id="L483">                                !     gprime - use reference density (RHO_0) for surface</span>
<span id="L484">                                !       density and GINT calculate internal densities.</span>
<span id="L485">                                !     ts_profile - use temperature and salinity profiles</span>
<span id="L486">                                !       (read from COORD_FILE) to set layer densities.</span>
<span id="L487">                                !     USER - call a user modified routine.</span>
<span id="L488">T_REF = 10.0                    !   [degC] default = 10.0</span>
<span id="L489">                                ! The default initial temperatures.</span>
<span id="L490">TS_RANGE_T_LIGHT = 25.0         !   [degC] default = 10.0</span>
<span id="L491">                                ! The initial temperature of the lightest layer when COORD_CONFIG is set to</span>
<span id="L492">                                ! ts_range.</span>
<span id="L493">TS_RANGE_T_DENSE = 3.0          !   [degC] default = 10.0</span>
<span id="L494">                                ! The initial temperature of the densest layer when COORD_CONFIG is set to</span>
<span id="L495">                                ! ts_range.</span>
<span id="L496">S_REF = 35.0                    !   [ppt] default = 35.0</span>
<span id="L497">                                ! The default initial salinities.</span>
<span id="L498">TS_RANGE_S_LIGHT = 35.0         !   [ppt] default = 35.0</span>
<span id="L499">                                ! The initial lightest salinities when COORD_CONFIG is set to ts_range.</span>
<span id="L500">TS_RANGE_S_DENSE = 35.0         !   [ppt] default = 35.0</span>
<span id="L501">                                ! The initial densest salinities when COORD_CONFIG is set to ts_range.</span>
<span id="L502">TS_RANGE_RESOLN_RATIO = 5.0     !   [nondim] default = 1.0</span>
<span id="L503">                                ! The ratio of density space resolution in the densest part of the range to that</span>
<span id="L504">                                ! in the lightest part of the range when COORD_CONFIG is set to ts_range. Values</span>
<span id="L505">                                ! greater than 1 increase the resolution of the denser water.</span>
<span id="L506">GFS = 9.8                       !   [m s-2] default = 9.8</span>
<span id="L507">                                ! The reduced gravity at the free surface.</span>
<span id="L508"></span>
<span id="L509">! === module MOM_state_initialization ===</span>
<span id="L510">FATAL_INCONSISTENT_RESTART_TIME = False !   [Boolean] default = False</span>
<span id="L511">                                ! If true and a time_in value is provided to MOM_initialize_state, verify that</span>
<span id="L512">                                ! the time read from a restart file is the same as time_in, and issue a fatal</span>
<span id="L513">                                ! error if it is not.  Otherwise, simply set the time to time_in if present.</span>
<span id="L514">INIT_LAYERS_FROM_Z_FILE = False !   [Boolean] default = False</span>
<span id="L515">                                ! If true, initialize the layer thicknesses, temperatures, and salinities from a</span>
<span id="L516">                                ! Z-space file on a latitude-longitude grid.</span>
<span id="L517">THICKNESS_CONFIG = &quot;benchmark&quot;  ! default = &quot;uniform&quot;</span>
<span id="L518">                                ! A string that determines how the initial layer thicknesses are specified for a</span>
<span id="L519">                                ! new run:</span>
<span id="L520">                                !     file - read interface heights from the file specified</span>
<span id="L521">                                !       by (THICKNESS_FILE).</span>
<span id="L522">                                !     thickness_file - read thicknesses from the file specified</span>
<span id="L523">                                !       by (THICKNESS_FILE).</span>
<span id="L524">                                !     mass_file - read thicknesses in units of mass per unit area from the file</span>
<span id="L525">                                !       specified by (THICKNESS_FILE).</span>
<span id="L526">                                !     coord - determined by ALE coordinate.</span>
<span id="L527">                                !     uniform - uniform thickness layers evenly distributed</span>
<span id="L528">                                !       between the surface and MAXIMUM_DEPTH.</span>
<span id="L529">                                !     list - read a list of positive interface depths.</span>
<span id="L530">                                !     param - use thicknesses from parameter THICKNESS_INIT_VALUES.</span>
<span id="L531">                                !     DOME - use a slope and channel configuration for the</span>
<span id="L532">                                !       DOME sill-overflow test case.</span>
<span id="L533">                                !     ISOMIP - use a configuration for the</span>
<span id="L534">                                !       ISOMIP test case.</span>
<span id="L535">                                !     benchmark - use the benchmark test case thicknesses.</span>
<span id="L536">                                !     Neverworld - use the Neverworld test case thicknesses.</span>
<span id="L537">                                !     search - search a density profile for the interface</span>
<span id="L538">                                !       densities. This is not yet implemented.</span>
<span id="L539">                                !     circle_obcs - the circle_obcs test case is used.</span>
<span id="L540">                                !     DOME2D - 2D version of DOME initialization.</span>
<span id="L541">                                !     adjustment2d - 2D lock exchange thickness ICs.</span>
<span id="L542">                                !     sloshing - sloshing gravity thickness ICs.</span>
<span id="L543">                                !     seamount - no motion test with seamount ICs.</span>
<span id="L544">                                !     dumbbell - sloshing channel ICs.</span>
<span id="L545">                                !     soliton - Equatorial Rossby soliton.</span>
<span id="L546">                                !     rossby_front - a mixed layer front in thermal wind balance.</span>
<span id="L547">                                !     USER - call a user modified routine.</span>
<span id="L548"></span>
<span id="L549">! === module benchmark_initialize_thickness ===</span>
<span id="L550">BENCHMARK_ML_DEPTH_IC = 50.0    !   [m] default = 50.0</span>
<span id="L551">                                ! Initial mixed layer depth in the benchmark test case.</span>
<span id="L552">BENCHMARK_THERMOCLINE_SCALE = 500.0 !   [m] default = 500.0</span>
<span id="L553">                                ! Initial thermocline depth scale in the benchmark test case.</span>
<span id="L554">BENCHMARK_T_LIGHT = 29.0        !   [degC] default = 29.0</span>
<span id="L555">                                ! A first guess at the temperature of the lightest layer in the benchmark test</span>
<span id="L556">                                ! case.</span>
<span id="L557">TS_CONFIG = &quot;benchmark&quot;         !</span>
<span id="L558">                                ! A string that determines how the initial temperatures and salinities are</span>
<span id="L559">                                ! specified for a new run:</span>
<span id="L560">                                !     file - read velocities from the file specified</span>
<span id="L561">                                !       by (TS_FILE).</span>
<span id="L562">                                !     fit - find the temperatures that are consistent with</span>
<span id="L563">                                !       the layer densities and salinity S_REF.</span>
<span id="L564">                                !     TS_profile - use temperature and salinity profiles</span>
<span id="L565">                                !       (read from TS_FILE) to set layer densities.</span>
<span id="L566">                                !     benchmark - use the benchmark test case T &amp; S.</span>
<span id="L567">                                !     linear - linear in logical layer space.</span>
<span id="L568">                                !     DOME2D - 2D DOME initialization.</span>
<span id="L569">                                !     ISOMIP - ISOMIP initialization.</span>
<span id="L570">                                !     adjustment2d - 2d lock exchange T/S ICs.</span>
<span id="L571">                                !     sloshing - sloshing mode T/S ICs.</span>
<span id="L572">                                !     seamount - no motion test with seamount ICs.</span>
<span id="L573">                                !     dumbbell - sloshing channel ICs.</span>
<span id="L574">                                !     rossby_front - a mixed layer front in thermal wind balance.</span>
<span id="L575">                                !     SCM_CVMix_tests - used in the SCM CVMix tests.</span>
<span id="L576">                                !     USER - call a user modified routine.</span>
<span id="L577">DEPRESS_INITIAL_SURFACE = False !   [Boolean] default = False</span>
<span id="L578">                                ! If true,  depress the initial surface to avoid huge tsunamis when a large</span>
<span id="L579">                                ! surface pressure is applied.</span>
<span id="L580">TRIM_IC_FOR_P_SURF = False      !   [Boolean] default = False</span>
<span id="L581">                                ! If true, cuts way the top of the column for initial conditions at the depth</span>
<span id="L582">                                ! where the hydrostatic pressure matches the imposed surface pressure which is</span>
<span id="L583">                                ! read from file.</span>
<span id="L584">VELOCITY_CONFIG = &quot;zero&quot;        ! default = &quot;zero&quot;</span>
<span id="L585">                                ! A string that determines how the initial velocities are specified for a new</span>
<span id="L586">                                ! run:</span>
<span id="L587">                                !     file - read velocities from the file specified</span>
<span id="L588">                                !       by (VELOCITY_FILE).</span>
<span id="L589">                                !     zero - the fluid is initially at rest.</span>
<span id="L590">                                !     uniform - the flow is uniform (determined by</span>
<span id="L591">                                !       parameters INITIAL_U_CONST and INITIAL_V_CONST).</span>
<span id="L592">                                !     rossby_front - a mixed layer front in thermal wind balance.</span>
<span id="L593">                                !     soliton - Equatorial Rossby soliton.</span>
<span id="L594">                                !     USER - call a user modified routine.</span>
<span id="L595">ODA_INCUPD = False              !   [Boolean] default = False</span>
<span id="L596">                                ! If true, oda incremental updates will be applied everywhere in the domain.</span>
<span id="L597">SPONGE = False                  !   [Boolean] default = False</span>
<span id="L598">                                ! If true, sponges may be applied anywhere in the domain. The exact location and</span>
<span id="L599">                                ! properties of those sponges are specified via SPONGE_CONFIG.</span>
<span id="L600"></span>
<span id="L601">! === module MOM_diag_mediator ===</span>
<span id="L602">NUM_DIAG_COORDS = 1             ! default = 1</span>
<span id="L603">                                ! The number of diagnostic vertical coordinates to use. For each coordinate, an</span>
<span id="L604">                                ! entry in DIAG_COORDS must be provided.</span>
<span id="L605">DIAG_REMAPPING_USE_OM4_SUBCELLS = True !   [Boolean] default = True</span>
<span id="L606">                                ! If true, use the OM4 remapping-via-subcells algorithm for diagnostics. See</span>
<span id="L607">                                ! REMAPPING_USE_OM4_SUBCELLS for details. We recommend setting this option to</span>
<span id="L608">                                ! false.</span>
<span id="L609">REMAPPING_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L610">                                ! The vintage of the expressions and order of arithmetic to use for remapping.</span>
<span id="L611">                                ! Values below 20190101 result in the use of older, less accurate expressions</span>
<span id="L612">                                ! that were in use at the end of 2018.  Higher values result in the use of more</span>
<span id="L613">                                ! robust and accurate forms of mathematically equivalent expressions.</span>
<span id="L614">USE_INDEX_DIAGNOSTIC_AXES = False !   [Boolean] default = False</span>
<span id="L615">                                ! If true, use a grid index coordinate convention for diagnostic axes.</span>
<span id="L616">DIAG_COORDS = &quot;z Z ZSTAR&quot;       ! default = &quot;z Z ZSTAR&quot;</span>
<span id="L617">                                ! A list of string tuples associating diag_table modules to a coordinate</span>
<span id="L618">                                ! definition used for diagnostics. Each string is of the form &quot;MODULE_SUFFIX</span>
<span id="L619">                                ! PARAMETER_SUFFIX COORDINATE_NAME&quot;.</span>
<span id="L620">DIAG_MISVAL = 1.0E+20           !   [various] default = 1.0E+20</span>
<span id="L621">                                ! Set the default missing value to use for diagnostics.</span>
<span id="L622">DIAG_AS_CHKSUM = False          !   [Boolean] default = False</span>
<span id="L623">                                ! Instead of writing diagnostics to the diag manager, write a text file</span>
<span id="L624">                                ! containing the checksum (bitcount) of the array.</span>
<span id="L625">AVAILABLE_DIAGS_FILE = &quot;available_diags.000000&quot; ! default = &quot;available_diags.000000&quot;</span>
<span id="L626">                                ! A file into which to write a list of all available ocean diagnostics that can</span>
<span id="L627">                                ! be included in a diag_table.</span>
<span id="L628">DIAG_COORD_DEF_Z = &quot;WOA09&quot;      ! default = &quot;WOA09&quot;</span>
<span id="L629">                                ! Determines how to specify the coordinate resolution. Valid options are:</span>
<span id="L630">                                !  PARAM       - use the vector-parameter DIAG_COORD_RES_Z</span>
<span id="L631">                                !  UNIFORM[:N] - uniformly distributed</span>
<span id="L632">                                !  FILE:string - read from a file. The string specifies</span>
<span id="L633">                                !                the filename and variable name, separated</span>
<span id="L634">                                !                by a comma or space, e.g. FILE:lev.nc,dz</span>
<span id="L635">                                !                or FILE:lev.nc,interfaces=zw</span>
<span id="L636">                                !  WOA09[:N]   - the WOA09 vertical grid (approximately)</span>
<span id="L637">                                !  WOA09INT[:N] - layers spanned by the WOA09 depths</span>
<span id="L638">                                !  WOA23INT[:N] - layers spanned by the WOA23 depths</span>
<span id="L639">                                !  FNC1:string - FNC1:dz_min,H_total,power,precision</span>
<span id="L640">                                !  HYBRID:string - read from a file. The string specifies</span>
<span id="L641">                                !                the filename and two variable names, separated</span>
<span id="L642">                                !                by a comma or space, for sigma-2 and dz.</span>
<span id="L643">                                !                e.g. HYBRID:vgrid.nc,sigma2,dz</span>
<span id="L644">                                !  HYBRID_3D:string - read from a file. The string specifies</span>
<span id="L645">                                !                the filename and two 3D variable names, separated</span>
<span id="L646">                                !                by a comma or space, for sigma-2 and dz. The</span>
<span id="L647">                                !                latter can be FNC1:string which is used everywhere.</span>
<span id="L648">                                !                e.g. HYBRID_3D:vgrid.nc,sigma2,dz</span>
<span id="L649">                                !  HYBRID_MAP:string - read from a file. The string specifies</span>
<span id="L650">                                !                the filename and three variable names, separated</span>
<span id="L651">                                !                by a comma or space, for map, sigma-2 and dz.</span>
<span id="L652">                                !                Map is a spatial index array with, maxval(map)=N,</span>
<span id="L653">                                !                and the others are 2D arrays containing N profiles.</span>
<span id="L654">                                !                Map typically contains integer values, but it can</span>
<span id="L655">                                !                contain real values, I+w, which imply using</span>
<span id="L656">                                !                the weighted sum of profiles I and I+1.</span>
<span id="L657">                                !                Dz can be FNC1:string which is used everywhere.</span>
<span id="L658">                                !                e.g. HYBRID_MAP:vgrid.nc,map,sigma2,dz</span>
<span id="L659"></span>
<span id="L660">! === module MOM_MEKE ===</span>
<span id="L661">USE_MEKE = False                !   [Boolean] default = False</span>
<span id="L662">                                ! If true, turns on the MEKE scheme which calculates a sub-grid mesoscale eddy</span>
<span id="L663">                                ! kinetic energy budget.</span>
<span id="L664"></span>
<span id="L665">! === module MOM_lateral_mixing_coeffs ===</span>
<span id="L666">USE_VARIABLE_MIXING = True      !   [Boolean] default = False</span>
<span id="L667">                                ! If true, the variable mixing code will be called.  This allows diagnostics to</span>
<span id="L668">                                ! be created even if the scheme is not used.  If KHTR_SLOPE_CFF&gt;0 or</span>
<span id="L669">                                ! KhTh_Slope_Cff&gt;0, this is set to true regardless of what is in the parameter</span>
<span id="L670">                                ! file.</span>
<span id="L671">USE_VISBECK = True              !   [Boolean] default = False</span>
<span id="L672">                                ! If true, use the Visbeck et al. (1997) formulation for</span>
<span id="L673">                                ! thickness diffusivity.</span>
<span id="L674">RESOLN_SCALED_KH = True         !   [Boolean] default = False</span>
<span id="L675">                                ! If true, the Laplacian lateral viscosity is scaled away when the first</span>
<span id="L676">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L677">DEPTH_SCALED_KHTH = False       !   [Boolean] default = False</span>
<span id="L678">                                ! If true, KHTH is scaled away when the depth is shallowerthan a reference</span>
<span id="L679">                                ! depth: KHTH = MIN(1,H/H0)**N * KHTH, where H0 is a reference depth, controlled</span>
<span id="L680">                                ! via DEPTH_SCALED_KHTH_H0, and the exponent (N) is controlled via</span>
<span id="L681">                                ! DEPTH_SCALED_KHTH_EXP.</span>
<span id="L682">RESOLN_SCALED_KHTH = True       !   [Boolean] default = False</span>
<span id="L683">                                ! If true, the interface depth diffusivity is scaled away when the first</span>
<span id="L684">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L685">RESOLN_SCALED_KHTR = True       !   [Boolean] default = False</span>
<span id="L686">                                ! If true, the epipycnal tracer diffusivity is scaled away when the first</span>
<span id="L687">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L688">RESOLN_USE_EBT = False          !   [Boolean] default = False</span>
<span id="L689">                                ! If true, uses the equivalent barotropic wave speed instead of first baroclinic</span>
<span id="L690">                                ! wave for calculating the resolution fn.</span>
<span id="L691">BACKSCAT_EBT_POWER = 0.0        !   [nondim] default = 0.0</span>
<span id="L692">                                ! Power to raise EBT vertical structure to when backscatter has vertical</span>
<span id="L693">                                ! structure.</span>
<span id="L694">BS_USE_SQG_STRUCT = False       !   [Boolean] default = False</span>
<span id="L695">                                ! If true, the SQG vertical structure is used for backscatter on the condition</span>
<span id="L696">                                ! that BS_EBT_power=0</span>
<span id="L697">KHTH_USE_EBT_STRUCT = False     !   [Boolean] default = False</span>
<span id="L698">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L699">                                ! thickness diffusivity.</span>
<span id="L700">KHTH_USE_SQG_STRUCT = False     !   [Boolean] default = False</span>
<span id="L701">                                ! If true, uses the surface quasigeostrophic structure as the vertical structure</span>
<span id="L702">                                ! of thickness diffusivity.</span>
<span id="L703">KHTR_USE_EBT_STRUCT = False     !   [Boolean] default = False</span>
<span id="L704">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L705">                                ! tracer diffusivity.</span>
<span id="L706">KHTR_USE_SQG_STRUCT = False     !   [Boolean] default = False</span>
<span id="L707">                                ! If true, uses the surface quasigeostrophic structure as the vertical structure</span>
<span id="L708">                                ! of tracer diffusivity.</span>
<span id="L709">KD_GL90_USE_EBT_STRUCT = False  !   [Boolean] default = False</span>
<span id="L710">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L711">                                ! diffusivity in the GL90 scheme.</span>
<span id="L712">KD_GL90_USE_SQG_STRUCT = False  !   [Boolean] default = False</span>
<span id="L713">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L714">                                ! diffusivity in the GL90 scheme.</span>
<span id="L715">KHTH_SLOPE_CFF = 0.1            !   [nondim] default = 0.0</span>
<span id="L716">                                ! The nondimensional coefficient in the Visbeck formula for the interface depth</span>
<span id="L717">                                ! diffusivity</span>
<span id="L718">KHTR_SLOPE_CFF = 0.1            !   [nondim] default = 0.0</span>
<span id="L719">                                ! The nondimensional coefficient in the Visbeck formula for the epipycnal tracer</span>
<span id="L720">                                ! diffusivity</span>
<span id="L721">USE_STORED_SLOPES = False       !   [Boolean] default = False</span>
<span id="L722">                                ! If true, the isopycnal slopes are calculated once and stored for re-use. This</span>
<span id="L723">                                ! uses more memory but avoids calling the equation of state more times than</span>
<span id="L724">                                ! should be necessary.</span>
<span id="L725">VERY_SMALL_FREQUENCY = 1.0E-17  !   [s-1] default = 1.0E-17</span>
<span id="L726">                                ! A miniscule frequency that is used to avoid division by 0.  The default value</span>
<span id="L727">                                ! is roughly (pi / (the age of the universe)).</span>
<span id="L728">USE_STANLEY_ISO = False         !   [Boolean] default = False</span>
<span id="L729">                                ! If true, turn on Stanley SGS T variance parameterization in isopycnal slope</span>
<span id="L730">                                ! code.</span>
<span id="L731">KD_SMOOTH = 1.0E-06             !   [m2 s-1] default = 1.0E-06</span>
<span id="L732">                                ! A diapycnal diffusivity that is used to interpolate more sensible values of T</span>
<span id="L733">                                ! &amp; S into thin layers.</span>
<span id="L734">USE_SIMPLER_EADY_GROWTH_RATE = False !   [Boolean] default = False</span>
<span id="L735">                                ! If true, use a simpler method to calculate the Eady growth rate that avoids</span>
<span id="L736">                                ! division by layer thickness. Recommended.</span>
<span id="L737">VARMIX_KTOP = 6                 !   [nondim] default = 2</span>
<span id="L738">                                ! The layer number at which to start vertical integration of S*N for purposes of</span>
<span id="L739">                                ! finding the Eady growth rate.</span>
<span id="L740">MIN_DZ_FOR_SLOPE_N2 = 1.0       !   [m] default = 1.0</span>
<span id="L741">                                ! The minimum vertical distance to use in the denominator of the bouyancy</span>
<span id="L742">                                ! frequency used in the slope calculation.</span>
<span id="L743">FULL_DEPTH_EADY_GROWTH_RATE = False !   [Boolean] default = False</span>
<span id="L744">                                ! If true, calculate the Eady growth rate based on average slope times</span>
<span id="L745">                                ! stratification that includes contributions from sea-level changes in its</span>
<span id="L746">                                ! denominator, rather than just the nominal depth of the bathymetry.  This only</span>
<span id="L747">                                ! applies when using the model interface heights as a proxy for isopycnal</span>
<span id="L748">                                ! slopes.</span>
<span id="L749">VISBECK_L_SCALE = 3.0E+04       !   [m or nondim] default = 0.0</span>
<span id="L750">                                ! The fixed length scale in the Visbeck formula, or if negative a nondimensional</span>
<span id="L751">                                ! scaling factor relating this length scale squared to the cell areas.</span>
<span id="L752">KH_RES_SCALE_COEF = 1.0         !   [nondim] default = 1.0</span>
<span id="L753">                                ! A coefficient that determines how KhTh is scaled away if RESOLN_SCALED_... is</span>
<span id="L754">                                ! true, as F = 1 / (1 + (KH_RES_SCALE_COEF*Rd/dx)^KH_RES_FN_POWER).</span>
<span id="L755">KH_RES_FN_POWER = 2             ! default = 2</span>
<span id="L756">                                ! The power of dx/Ld in the Kh resolution function.  Any positive integer may be</span>
<span id="L757">                                ! used, although even integers are more efficient to calculate.  Setting this</span>
<span id="L758">                                ! greater than 100 results in a step-function being used.</span>
<span id="L759">VISC_RES_SCALE_COEF = 1.0       !   [nondim] default = 1.0</span>
<span id="L760">                                ! A coefficient that determines how Kh is scaled away if RESOLN_SCALED_... is</span>
<span id="L761">                                ! true, as F = 1 / (1 + (KH_RES_SCALE_COEF*Rd/dx)^KH_RES_FN_POWER). This</span>
<span id="L762">                                ! function affects lateral viscosity, Kh, and not KhTh.</span>
<span id="L763">VISC_RES_FN_POWER = 2           ! default = 2</span>
<span id="L764">                                ! The power of dx/Ld in the Kh resolution function.  Any positive integer may be</span>
<span id="L765">                                ! used, although even integers are more efficient to calculate.  Setting this</span>
<span id="L766">                                ! greater than 100 results in a step-function being used. This function affects</span>
<span id="L767">                                ! lateral viscosity, Kh, and not KhTh.</span>
<span id="L768">INTERPOLATE_RES_FN = False      !   [Boolean] default = False</span>
<span id="L769">                                ! If true, interpolate the resolution function to the velocity points from the</span>
<span id="L770">                                ! thickness points; otherwise interpolate the wave speed and calculate the</span>
<span id="L771">                                ! resolution function independently at each point.</span>
<span id="L772">GILL_EQUATORIAL_LD = True       !   [Boolean] default = True</span>
<span id="L773">                                ! If true, uses Gill&#x27;s definition of the baroclinic equatorial deformation</span>
<span id="L774">                                ! radius, otherwise, if false, use Pedlosky&#x27;s definition. These definitions</span>
<span id="L775">                                ! differ by a factor of 2 in front of the beta term in the denominator. Gill&#x27;s</span>
<span id="L776">                                ! is the more appropriate definition.</span>
<span id="L777">INTERNAL_WAVE_SPEED_TOL = 0.001 !   [nondim] default = 0.001</span>
<span id="L778">                                ! The fractional tolerance for finding the wave speeds.</span>
<span id="L779">INTERNAL_WAVE_SPEED_MIN = 0.0   !   [m s-1] default = 0.0</span>
<span id="L780">                                ! A floor in the first mode speed below which 0 used instead.</span>
<span id="L781">INTERNAL_WAVE_SPEED_BETTER_EST = False !   [Boolean] default = True</span>
<span id="L782">                                ! If true, use a more robust estimate of the first mode wave speed as the</span>
<span id="L783">                                ! starting point for iterations.</span>
<span id="L784">EBT_REMAPPING_USE_OM4_SUBCELLS = True !   [Boolean] default = True</span>
<span id="L785">                                ! If true, use the OM4 remapping-via-subcells algorithm for calculating EBT</span>
<span id="L786">                                ! structure. See REMAPPING_USE_OM4_SUBCELLS for details. We recommend setting</span>
<span id="L787">                                ! this option to false.</span>
<span id="L788">USE_QG_LEITH_GM = False         !   [Boolean] default = False</span>
<span id="L789">                                ! If true, use the QG Leith viscosity as the GM coefficient.</span>
<span id="L790"></span>
<span id="L791">! === module MOM_set_visc ===</span>
<span id="L792">SET_VISC_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L793">                                ! The vintage of the order of arithmetic and expressions in the set viscosity</span>
<span id="L794">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L795">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L796">BOTTOMDRAGLAW = True            !   [Boolean] default = True</span>
<span id="L797">                                ! If true, the bottom stress is calculated with a drag law of the form</span>
<span id="L798">                                ! c_drag*|u|*u. The velocity magnitude may be an assumed value or it may be</span>
<span id="L799">                                ! based on the actual velocity in the bottommost HBBL, depending on LINEAR_DRAG.</span>
<span id="L800">DRAG_AS_BODY_FORCE = False      !   [Boolean] default = False</span>
<span id="L801">                                ! If true, the bottom stress is imposed as an explicit body force applied over a</span>
<span id="L802">                                ! fixed distance from the bottom, rather than as an implicit calculation based</span>
<span id="L803">                                ! on an enhanced near-bottom viscosity. The thickness of the bottom boundary</span>
<span id="L804">                                ! layer is HBBL.</span>
<span id="L805">CHANNEL_DRAG = False            !   [Boolean] default = False</span>
<span id="L806">                                ! If true, the bottom drag is exerted directly on each layer proportional to the</span>
<span id="L807">                                ! fraction of the bottom it overlies.</span>
<span id="L808">LINEAR_DRAG = False             !   [Boolean] default = False</span>
<span id="L809">                                ! If LINEAR_DRAG and BOTTOMDRAGLAW are defined the drag law is</span>
<span id="L810">                                ! cdrag*DRAG_BG_VEL*u.</span>
<span id="L811">DYNAMIC_VISCOUS_ML = True       !   [Boolean] default = False</span>
<span id="L812">                                ! If true, use a bulk Richardson number criterion to determine the mixed layer</span>
<span id="L813">                                ! thickness for viscosity.</span>
<span id="L814">BULK_RI_ML_VISC = 0.05          !   [nondim] default = 0.05</span>
<span id="L815">                                ! The efficiency with which mean kinetic energy released by mechanically forced</span>
<span id="L816">                                ! entrainment of the mixed layer is converted to turbulent kinetic energy.  By</span>
<span id="L817">                                ! default, BULK_RI_ML_VISC = BULK_RI_ML or 0.</span>
<span id="L818">TKE_DECAY_VISC = 10.0           !   [nondim] default = 10.0</span>
<span id="L819">                                ! TKE_DECAY_VISC relates the vertical rate of decay of the TKE available for</span>
<span id="L820">                                ! mechanical entrainment to the natural Ekman depth for use in calculating the</span>
<span id="L821">                                ! dynamic mixed layer viscosity.  By default, TKE_DECAY_VISC = TKE_DECAY or 0.</span>
<span id="L822">ML_OMEGA_FRAC = 1.0             !   [nondim] default = 0.0</span>
<span id="L823">                                ! When setting the decay scale for turbulence, use this fraction of the absolute</span>
<span id="L824">                                ! rotation rate blended with the local value of f, as sqrt((1-of)*f^2 +</span>
<span id="L825">                                ! of*4*omega^2).</span>
<span id="L826">HBBL = 10.0                     !   [m]</span>
<span id="L827">                                ! The thickness of a bottom boundary layer with a viscosity increased by</span>
<span id="L828">                                ! KV_EXTRA_BBL if BOTTOMDRAGLAW is not defined, or the thickness over which</span>
<span id="L829">                                ! near-bottom velocities are averaged for the drag law if BOTTOMDRAGLAW is</span>
<span id="L830">                                ! defined but LINEAR_DRAG is not.</span>
<span id="L831">CDRAG = 0.003                   !   [nondim] default = 0.003</span>
<span id="L832">                                ! CDRAG is the drag coefficient relating the magnitude of the velocity field to</span>
<span id="L833">                                ! the bottom stress. CDRAG is only used if BOTTOMDRAGLAW is defined.</span>
<span id="L834">BBL_USE_TIDAL_BG = False        !   [Boolean] default = False</span>
<span id="L835">                                ! Flag to use the tidal RMS amplitude in place of constant background velocity</span>
<span id="L836">                                ! for computing u* in the BBL. This flag is only used when BOTTOMDRAGLAW is true</span>
<span id="L837">                                ! and LINEAR_DRAG is false.</span>
<span id="L838">DRAG_BG_VEL = 0.1               !   [m s-1] default = 0.0</span>
<span id="L839">                                ! DRAG_BG_VEL is either the assumed bottom velocity (with LINEAR_DRAG) or an</span>
<span id="L840">                                ! unresolved  velocity that is combined with the resolved velocity to estimate</span>
<span id="L841">                                ! the velocity magnitude.  DRAG_BG_VEL is only used when BOTTOMDRAGLAW is</span>
<span id="L842">                                ! defined.</span>
<span id="L843">BBL_USE_EOS = False             !   [Boolean] default = True</span>
<span id="L844">                                ! If true, use the equation of state in determining the properties of the bottom</span>
<span id="L845">                                ! boundary layer.  Otherwise use the layer target potential densities.  The</span>
<span id="L846">                                ! default of this parameter is the value of USE_EOS.</span>
<span id="L847">BBL_THICK_MIN = 0.1             !   [m] default = 0.0</span>
<span id="L848">                                ! The minimum bottom boundary layer thickness that can be used with</span>
<span id="L849">                                ! BOTTOMDRAGLAW. This might be Kv/(cdrag*drag_bg_vel) to give Kv as the minimum</span>
<span id="L850">                                ! near-bottom viscosity.</span>
<span id="L851">HTBL_SHELF_MIN = 0.1            !   [m] default = 0.1</span>
<span id="L852">                                ! The minimum top boundary layer thickness that can be used with BOTTOMDRAGLAW.</span>
<span id="L853">                                ! This might be Kv/(cdrag*drag_bg_vel) to give Kv as the minimum near-top</span>
<span id="L854">                                ! viscosity.</span>
<span id="L855">HTBL_SHELF = 10.0               !   [m] default = 10.0</span>
<span id="L856">                                ! The thickness over which near-surface velocities are averaged for the drag law</span>
<span id="L857">                                ! under an ice shelf.  By default this is the same as HBBL</span>
<span id="L858">KV = 1.0E-04                    !   [m2 s-1]</span>
<span id="L859">                                ! The background kinematic viscosity in the interior. The molecular value, ~1e-6</span>
<span id="L860">                                ! m2 s-1, may be used.</span>
<span id="L861">KV_BBL_MIN = 1.0E-04            !   [m2 s-1] default = 1.0E-04</span>
<span id="L862">                                ! The minimum viscosities in the bottom boundary layer.</span>
<span id="L863">KV_TBL_MIN = 1.0E-04            !   [m2 s-1] default = 1.0E-04</span>
<span id="L864">                                ! The minimum viscosities in the top boundary layer.</span>
<span id="L865">CORRECT_BBL_BOUNDS = False      !   [Boolean] default = False</span>
<span id="L866">                                ! If true, uses the correct bounds on the BBL thickness and viscosity so that</span>
<span id="L867">                                ! the bottom layer feels the intended drag.</span>
<span id="L868"></span>
<span id="L869">! === module MOM_thickness_diffuse ===</span>
<span id="L870">KHTH = 1.0                      !   [m2 s-1] default = 0.0</span>
<span id="L871">                                ! The background horizontal thickness diffusivity.</span>
<span id="L872">READ_KHTH = False               !   [Boolean] default = False</span>
<span id="L873">                                ! If true, read a file (given by KHTH_FILE) containing the spatially varying</span>
<span id="L874">                                ! horizontal isopycnal height diffusivity.</span>
<span id="L875">KHTH_MIN = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L876">                                ! The minimum horizontal thickness diffusivity.</span>
<span id="L877">KHTH_MAX = 900.0                !   [m2 s-1] default = 0.0</span>
<span id="L878">                                ! The maximum horizontal thickness diffusivity.</span>
<span id="L879">KHTH_MAX_CFL = 0.8              !   [nondimensional] default = 0.8</span>
<span id="L880">                                ! The maximum value of the local diffusive CFL ratio that is permitted for the</span>
<span id="L881">                                ! thickness diffusivity. 1.0 is the marginally unstable value in a pure layered</span>
<span id="L882">                                ! model, but much smaller numbers (e.g. 0.1) seem to work better for ALE-based</span>
<span id="L883">                                ! models.</span>
<span id="L884">KH_ETA_CONST = 0.0              !   [m2 s-1] default = 0.0</span>
<span id="L885">                                ! The background horizontal diffusivity of the interface heights (without</span>
<span id="L886">                                ! considering the layer density structure).  If diffusive CFL limits are</span>
<span id="L887">                                ! encountered, the diffusivities of the isopycnals and the interfaces heights</span>
<span id="L888">                                ! are scaled back proportionately.</span>
<span id="L889">KH_ETA_VEL_SCALE = 0.0          !   [m s-1] default = 0.0</span>
<span id="L890">                                ! A velocity scale that is multiplied by the grid spacing to give a contribution</span>
<span id="L891">                                ! to the horizontal diffusivity of the interface heights (without considering</span>
<span id="L892">                                ! the layer density structure).</span>
<span id="L893">DETANGLE_INTERFACES = False     !   [Boolean] default = False</span>
<span id="L894">                                ! If defined add 3-d structured enhanced interface height diffusivities to</span>
<span id="L895">                                ! horizontally smooth jagged layers.</span>
<span id="L896">KHTH_SLOPE_MAX = 0.01           !   [nondim] default = 0.01</span>
<span id="L897">                                ! A slope beyond which the calculated isopycnal slope is not reliable and is</span>
<span id="L898">                                ! scaled away.</span>
<span id="L899">KHTH_USE_FGNV_STREAMFUNCTION = False !   [Boolean] default = False</span>
<span id="L900">                                ! If true, use the streamfunction formulation of Ferrari et al., 2010, which</span>
<span id="L901">                                ! effectively emphasizes graver vertical modes by smoothing in the vertical.</span>
<span id="L902">USE_STANLEY_GM = False          !   [Boolean] default = False</span>
<span id="L903">                                ! If true, turn on Stanley SGS T variance parameterization in GM code.</span>
<span id="L904">MEKE_GM_SRC_ALT = False         !   [Boolean] default = False</span>
<span id="L905">                                ! If true, use the GM energy conversion form S^2*N^2*kappa rather than the</span>
<span id="L906">                                ! streamfunction for the GM source term.</span>
<span id="L907">MEKE_GEOMETRIC = False          !   [Boolean] default = False</span>
<span id="L908">                                ! If true, uses the GM coefficient formulation from the GEOMETRIC framework</span>
<span id="L909">                                ! (Marshall et al., 2012).</span>
<span id="L910">USE_GME = False                 !   [Boolean] default = False</span>
<span id="L911">                                ! If true, use the GM+E backscatter scheme in association with the Gent and</span>
<span id="L912">                                ! McWilliams parameterization.</span>
<span id="L913">USE_GM_WORK_BUG = False         !   [Boolean] default = False</span>
<span id="L914">                                ! If true, compute the top-layer work tendency on the u-grid with the incorrect</span>
<span id="L915">                                ! sign, for legacy reproducibility.</span>
<span id="L916">STOCH_EOS = False               !   [Boolean] default = False</span>
<span id="L917">                                ! If true, stochastic perturbations are applied to the EOS in the PGF.</span>
<span id="L918">STANLEY_COEFF = -1.0            !   [nondim] default = -1.0</span>
<span id="L919">                                ! Coefficient correlating the temperature gradient and SGS T variance.</span>
<span id="L920"></span>
<span id="L921">! === module MOM_dynamics_split_RK2 ===</span>
<span id="L922">TIDES = False                   !   [Boolean] default = False</span>
<span id="L923">                                ! If true, apply tidal momentum forcing.</span>
<span id="L924">CALCULATE_SAL = False           !   [Boolean] default = False</span>
<span id="L925">                                ! If true, calculate self-attraction and loading.</span>
<span id="L926">USE_HA = False                  !   [Boolean] default = False</span>
<span id="L927">                                ! If true, perform inline harmonic analysis.</span>
<span id="L928">BE = 0.6                        !   [nondim] default = 0.6</span>
<span id="L929">                                ! If SPLIT is true, BE determines the relative weighting of a  2nd-order</span>
<span id="L930">                                ! Runga-Kutta baroclinic time stepping scheme (0.5) and a backward Euler scheme</span>
<span id="L931">                                ! (1) that is used for the Coriolis and inertial terms.  BE may be from 0.5 to</span>
<span id="L932">                                ! 1, but instability may occur near 0.5. BE is also applicable if SPLIT is false</span>
<span id="L933">                                ! and USE_RK2 is true.</span>
<span id="L934">BEGW = 0.0                      !   [nondim] default = 0.0</span>
<span id="L935">                                ! If SPLIT is true, BEGW is a number from 0 to 1 that controls the extent to</span>
<span id="L936">                                ! which the treatment of gravity waves is forward-backward (0) or simulated</span>
<span id="L937">                                ! backward Euler (1).  0 is almost always used. If SPLIT is false and USE_RK2 is</span>
<span id="L938">                                ! true, BEGW can be between 0 and 0.5 to damp gravity waves.</span>
<span id="L939">SET_DTBT_USE_BT_CONT = False    !   [Boolean] default = False</span>
<span id="L940">                                ! If true, use BT_CONT to calculate DTBT if possible.</span>
<span id="L941">SPLIT_BOTTOM_STRESS = False     !   [Boolean] default = False</span>
<span id="L942">                                ! If true, provide the bottom stress calculated by the vertical viscosity to the</span>
<span id="L943">                                ! barotropic solver.</span>
<span id="L944">BT_USE_LAYER_FLUXES = True      !   [Boolean] default = True</span>
<span id="L945">                                ! If true, use the summed layered fluxes plus an adjustment due to the change in</span>
<span id="L946">                                ! the barotropic velocity in the barotropic continuity equation.</span>
<span id="L947">BT_ADJ_CORR_MASS_SRC = True     !   [Boolean] default = True</span>
<span id="L948">                                ! If true, recalculates the barotropic mass source after predictor step. This</span>
<span id="L949">                                ! should make little difference in the deep ocean but appears to help for</span>
<span id="L950">                                ! vanished layers. If false, uses the same mass source as from the predictor</span>
<span id="L951">                                ! step.</span>
<span id="L952">STORE_CORIOLIS_ACCEL = True     !   [Boolean] default = True</span>
<span id="L953">                                ! If true, calculate the Coriolis accelerations at the end of each timestep for</span>
<span id="L954">                                ! use in the predictor step of the next split RK2 timestep.</span>
<span id="L955">FPMIX = False                   !   [Boolean] default = False</span>
<span id="L956">                                ! If true, add non-local momentum flux increments and diffuse down the Eulerian</span>
<span id="L957">                                ! gradient.</span>
<span id="L958">VISC_REM_BUG = True             !   [Boolean] default = False</span>
<span id="L959">                                ! If true, visc_rem_[uv] in split mode is incorrectly calculated or accounted</span>
<span id="L960">                                ! for in two places. This parameter controls the defaults of two individual</span>
<span id="L961">                                ! flags, VISC_REM_TIMESTEP_BUG in MOM_dynamics_split_RK2(b) and</span>
<span id="L962">                                ! VISC_REM_BT_WEIGHT_BUG in MOM_barotropic.</span>
<span id="L963">VISC_REM_TIMESTEP_BUG = True    !   [Boolean] default = True</span>
<span id="L964">                                ! If true, recover a bug that uses dt_pred rather than dt in vertvisc_remnant()</span>
<span id="L965">                                ! at the end of predictor stage for the following continuity() and btstep()</span>
<span id="L966">                                ! calls in the corrector step. Default of this flag is set by VISC_REM_BUG</span>
<span id="L967"></span>
<span id="L968">! === module MOM_continuity_PPM ===</span>
<span id="L969">MONOTONIC_CONTINUITY = False    !   [Boolean] default = False</span>
<span id="L970">                                ! If true, CONTINUITY_PPM uses the Colella and Woodward monotonic limiter.  The</span>
<span id="L971">                                ! default (false) is to use a simple positive definite limiter.</span>
<span id="L972">SIMPLE_2ND_PPM_CONTINUITY = False !   [Boolean] default = False</span>
<span id="L973">                                ! If true, CONTINUITY_PPM uses a simple 2nd order (arithmetic mean)</span>
<span id="L974">                                ! interpolation of the edge values. This may give better PV conservation</span>
<span id="L975">                                ! properties. While it formally reduces the accuracy of the continuity solver</span>
<span id="L976">                                ! itself in the strongly advective limit, it does not reduce the overall order</span>
<span id="L977">                                ! of accuracy of the dynamic core.</span>
<span id="L978">UPWIND_1ST_CONTINUITY = False   !   [Boolean] default = False</span>
<span id="L979">                                ! If true, CONTINUITY_PPM becomes a 1st-order upwind continuity solver.  This</span>
<span id="L980">                                ! scheme is highly diffusive but may be useful for debugging or in single-column</span>
<span id="L981">                                ! mode where its minimal stencil is useful.</span>
<span id="L982">ETA_TOLERANCE = 1.0E-06         !   [m] default = 1.1E-09</span>
<span id="L983">                                ! The tolerance for the differences between the barotropic and baroclinic</span>
<span id="L984">                                ! estimates of the sea surface height due to the fluxes through each face.  The</span>
<span id="L985">                                ! total tolerance for SSH is 4 times this value.  The default is</span>
<span id="L986">                                ! 0.5*NK*ANGSTROM, and this should not be set less than about</span>
<span id="L987">                                ! 10^-15*MAXIMUM_DEPTH.</span>
<span id="L988">VELOCITY_TOLERANCE = 0.001      !   [m s-1] default = 3.0E+08</span>
<span id="L989">                                ! The tolerance for barotropic velocity discrepancies between the barotropic</span>
<span id="L990">                                ! solution and  the sum of the layer thicknesses.</span>
<span id="L991">CONT_PPM_AGGRESS_ADJUST = False !   [Boolean] default = False</span>
<span id="L992">                                ! If true, allow the adjusted velocities to have a relative CFL change up to</span>
<span id="L993">                                ! 0.5.</span>
<span id="L994">CONT_PPM_VOLUME_BASED_CFL = False !   [Boolean] default = False</span>
<span id="L995">                                ! If true, use the ratio of the open face lengths to the tracer cell areas when</span>
<span id="L996">                                ! estimating CFL numbers.  The default is set by CONT_PPM_AGGRESS_ADJUST.</span>
<span id="L997">CONTINUITY_CFL_LIMIT = 0.5      !   [nondim] default = 0.5</span>
<span id="L998">                                ! The maximum CFL of the adjusted velocities.</span>
<span id="L999">CONT_PPM_BETTER_ITER = True     !   [Boolean] default = True</span>
<span id="L1000">                                ! If true, stop corrective iterations using a velocity based criterion and only</span>
<span id="L1001">                                ! stop if the iteration is better than all predecessors.</span>
<span id="L1002">CONT_PPM_USE_VISC_REM_MAX = True !   [Boolean] default = True</span>
<span id="L1003">                                ! If true, use more appropriate limiting bounds for corrections in strongly</span>
<span id="L1004">                                ! viscous columns.</span>
<span id="L1005">CONT_PPM_MARGINAL_FACE_AREAS = True !   [Boolean] default = True</span>
<span id="L1006">                                ! If true, use the marginal face areas from the continuity solver for use as the</span>
<span id="L1007">                                ! weights in the barotropic solver. Otherwise use the transport averaged areas.</span>
<span id="L1008"></span>
<span id="L1009">! === module MOM_CoriolisAdv ===</span>
<span id="L1010">NOSLIP = False                  !   [Boolean] default = False</span>
<span id="L1011">                                ! If true, no slip boundary conditions are used; otherwise free slip boundary</span>
<span id="L1012">                                ! conditions are assumed. The implementation of the free slip BCs on a C-grid is</span>
<span id="L1013">                                ! much cleaner than the no slip BCs. The use of free slip BCs is strongly</span>
<span id="L1014">                                ! encouraged, and no slip BCs are not used with the biharmonic viscosity.</span>
<span id="L1015">CORIOLIS_EN_DIS = False         !   [Boolean] default = False</span>
<span id="L1016">                                ! If true, two estimates of the thickness fluxes are used to estimate the</span>
<span id="L1017">                                ! Coriolis term, and the one that dissipates energy relative to the other one is</span>
<span id="L1018">                                ! used.</span>
<span id="L1019">CORIOLIS_SCHEME = &quot;SADOURNY75_ENERGY&quot; ! default = &quot;SADOURNY75_ENERGY&quot;</span>
<span id="L1020">                                ! CORIOLIS_SCHEME selects the discretization for the Coriolis terms. Valid</span>
<span id="L1021">                                ! values are:</span>
<span id="L1022">                                !    SADOURNY75_ENERGY - Sadourny, 1975; energy cons.</span>
<span id="L1023">                                !    ARAKAWA_HSU90     - Arakawa &amp; Hsu, 1990</span>
<span id="L1024">                                !    SADOURNY75_ENSTRO - Sadourny, 1975; enstrophy cons.</span>
<span id="L1025">                                !    ARAKAWA_LAMB81    - Arakawa &amp; Lamb, 1981; En. + Enst.</span>
<span id="L1026">                                !    ARAKAWA_LAMB_BLEND - A blend of Arakawa &amp; Lamb with</span>
<span id="L1027">                                !                         Arakawa &amp; Hsu and Sadourny energy</span>
<span id="L1028">                                !    WENOVI5TH_PV_ENSTRO   - 5th-order WENO PV enstrophy</span>
<span id="L1029">                                !    WENOVI3RD_PV_ENSTRO   - 3rd-order WENO PV enstrophy</span>
<span id="L1030">                                !    WENOVI7TH_PV_ENSTRO  - 7th-order WENO PV enstrophy</span>
<span id="L1031">BOUND_CORIOLIS = True           !   [Boolean] default = False</span>
<span id="L1032">                                ! If true, the Coriolis terms at u-points are bounded by the four estimates of</span>
<span id="L1033">                                ! (f+rv)v from the four neighboring v-points, and similarly at v-points.  This</span>
<span id="L1034">                                ! option would have no effect on the SADOURNY Coriolis scheme if it were</span>
<span id="L1035">                                ! possible to use centered difference thickness fluxes.</span>
<span id="L1036">KE_SCHEME = &quot;KE_ARAKAWA&quot;        ! default = &quot;KE_ARAKAWA&quot;</span>
<span id="L1037">                                ! KE_SCHEME selects the discretization for acceleration due to the kinetic</span>
<span id="L1038">                                ! energy gradient. Valid values are:</span>
<span id="L1039">                                !    KE_ARAKAWA, KE_SIMPLE_GUDONOV, KE_GUDONOV, KE_UP3</span>
<span id="L1040">PV_ADV_SCHEME = &quot;PV_ADV_CENTERED&quot; ! default = &quot;PV_ADV_CENTERED&quot;</span>
<span id="L1041">                                ! PV_ADV_SCHEME selects the discretization for PV advection. Valid values are:</span>
<span id="L1042">                                !    PV_ADV_CENTERED - centered (aka Sadourny, 75)</span>
<span id="L1043">                                !    PV_ADV_UPWIND1  - upwind, first order</span>
<span id="L1044"></span>
<span id="L1045">! === module MOM_PressureForce ===</span>
<span id="L1046">ANALYTIC_FV_PGF = True          !   [Boolean] default = True</span>
<span id="L1047">                                ! If true the pressure gradient forces are calculated with a finite volume form</span>
<span id="L1048">                                ! that analytically integrates the equations of state in pressure to avoid any</span>
<span id="L1049">                                ! possibility of numerical thermobaric instability, as described in Adcroft et</span>
<span id="L1050">                                ! al., O. Mod. (2008).</span>
<span id="L1051"></span>
<span id="L1052">! === module MOM_PressureForce_FV ===</span>
<span id="L1053">RHO_PGF_REF = 1035.0            !   [kg m-3] default = 1035.0</span>
<span id="L1054">                                ! The reference density that is subtracted off when calculating pressure</span>
<span id="L1055">                                ! gradient forces.  Its inverse is subtracted off of specific volumes when in</span>
<span id="L1056">                                ! non-Boussinesq mode.  The default is RHO_0.</span>
<span id="L1057">RHO_PGF_REF_BUG = True          !   [Boolean] default = True</span>
<span id="L1058">                                ! If true, recover a bug that RHO_0 (the mean seawater density in Boussinesq</span>
<span id="L1059">                                ! mode) and RHO_PGF_REF (the subtracted reference density in finite volume</span>
<span id="L1060">                                ! pressure gradient forces) are incorrectly interchanged in several instances in</span>
<span id="L1061">                                ! Boussinesq mode.</span>
<span id="L1062">SSH_IN_EOS_PRESSURE_FOR_PGF = False !   [Boolean] default = False</span>
<span id="L1063">                                ! If true, include contributions from the sea surface height in the height-based</span>
<span id="L1064">                                ! pressure used in the equation of state calculations for the Boussinesq</span>
<span id="L1065">                                ! pressure gradient forces, including adjustments for atmospheric or sea-ice</span>
<span id="L1066">                                ! pressure.</span>
<span id="L1067">MASS_WEIGHT_IN_PRESSURE_GRADIENT = False !   [Boolean] default = False</span>
<span id="L1068">                                ! If true, use mass weighting when interpolating T/S for integrals near the</span>
<span id="L1069">                                ! bathymetry in FV pressure gradient calculations.</span>
<span id="L1070">MASS_WEIGHT_IN_PRESSURE_GRADIENT_TOP = False !   [Boolean] default = False</span>
<span id="L1071">                                ! If true and MASS_WEIGHT_IN_PRESSURE_GRADIENT is true, use mass weighting when</span>
<span id="L1072">                                ! interpolating T/S for integrals near the top of the water column in FV</span>
<span id="L1073">                                ! pressure gradient calculations.</span>
<span id="L1074">MASS_WEIGHT_IN_PGF_VANISHED_ONLY = False !   [Boolean] default = False</span>
<span id="L1075">                                ! If true, use mass weighting when interpolating T/S for integrals only if one</span>
<span id="L1076">                                ! side is vanished according to RESET_INTXPA_H_NONVANISHED.</span>
<span id="L1077">CORRECTION_INTXPA = False       !   [Boolean] default = False</span>
<span id="L1078">                                ! If true, use a correction for surface pressure curvature in intx_pa.</span>
<span id="L1079">RESET_INTXPA_INTEGRAL = False   !   [Boolean] default = False</span>
<span id="L1080">                                ! If true, reset INTXPA to match pressures at first nonvanished cell. Includes</span>
<span id="L1081">                                ! pressure correction.</span>
<span id="L1082">RESET_INTXPA_INTEGRAL_FLATTEST = False !   [Boolean] default = False</span>
<span id="L1083">                                ! If true, use flattest interface as reference interface where there is no</span>
<span id="L1084">                                ! better choice for RESET_INTXPA_INTEGRAL. Otherwise, use surface interface.</span>
<span id="L1085">USE_INACCURATE_PGF_RHO_ANOM = False !   [Boolean] default = False</span>
<span id="L1086">                                ! If true, use a form of the PGF that uses the reference density in an</span>
<span id="L1087">                                ! inaccurate way. This is not recommended.</span>
<span id="L1088">RECONSTRUCT_FOR_PRESSURE = False !   [Boolean] default = False</span>
<span id="L1089">                                ! If True, use vertical reconstruction of T &amp; S within the integrals of the FV</span>
<span id="L1090">                                ! pressure gradient calculation. If False, use the constant-by-layer algorithm.</span>
<span id="L1091">                                ! The default is set by USE_REGRIDDING.</span>
<span id="L1092">PRESSURE_RECONSTRUCTION_SCHEME = 1 ! default = 1</span>
<span id="L1093">                                ! Order of vertical reconstruction of T/S to use in the integrals within the FV</span>
<span id="L1094">                                ! pressure gradient calculation.</span>
<span id="L1095">                                !  0: PCM or no reconstruction.</span>
<span id="L1096">                                !  1: PLM reconstruction.</span>
<span id="L1097">                                !  2: PPM reconstruction.</span>
<span id="L1098">BOUNDARY_EXTRAPOLATION_PRESSURE = True !   [Boolean] default = True</span>
<span id="L1099">                                ! If true, the reconstruction of T &amp; S for pressure in boundary cells is</span>
<span id="L1100">                                ! extrapolated, rather than using PCM in these cells. If true, the same order</span>
<span id="L1101">                                ! polynomial is used as is used for the interior cells.</span>
<span id="L1102">USE_STANLEY_PGF = False         !   [Boolean] default = False</span>
<span id="L1103">                                ! If true, turn on Stanley SGS T variance parameterization in PGF code.</span>
<span id="L1104"></span>
<span id="L1105">! === module MOM_Zanna_Bolton ===</span>
<span id="L1106">USE_ZB2020 = False              !   [Boolean] default = False</span>
<span id="L1107">                                ! If true, turns on Zanna-Bolton-2020 (ZB) subgrid momentum parameterization of</span>
<span id="L1108">                                ! mesoscale eddies.</span>
<span id="L1109"></span>
<span id="L1110">! === module MOM_hor_visc ===</span>
<span id="L1111">USE_CIRCULATION_IN_HORVISC = False !   [Boolean] default = False</span>
<span id="L1112">                                ! Use circulation theorem to compute vorticity in horvisc module (for ZB20 or</span>
<span id="L1113">                                ! Leith)</span>
<span id="L1114">USE_CONT_THICKNESS = False      !   [Boolean] default = False</span>
<span id="L1115">                                ! If true, use thickness at velocity points from continuity solver. This option</span>
<span id="L1116">                                ! currently only works with split mode.</span>
<span id="L1117">LAPLACIAN = False               !   [Boolean] default = False</span>
<span id="L1118">                                ! If true, use a Laplacian horizontal viscosity.</span>
<span id="L1119">BIHARMONIC = True               !   [Boolean] default = True</span>
<span id="L1120">                                ! If true, use a biharmonic horizontal viscosity. BIHARMONIC may be used with</span>
<span id="L1121">                                ! LAPLACIAN.</span>
<span id="L1122">AH = 0.0                        !   [m4 s-1] default = 0.0</span>
<span id="L1123">                                ! The background biharmonic horizontal viscosity.</span>
<span id="L1124">AH_VEL_SCALE = 0.05             !   [m s-1] default = 0.0</span>
<span id="L1125">                                ! The velocity scale which is multiplied by the cube of the grid spacing to</span>
<span id="L1126">                                ! calculate the biharmonic viscosity. The final viscosity is the largest of this</span>
<span id="L1127">                                ! scaled viscosity, the Smagorinsky and Leith viscosities, and AH.</span>
<span id="L1128">AH_TIME_SCALE = 0.0             !   [s] default = 0.0</span>
<span id="L1129">                                ! A time scale whose inverse is multiplied by the fourth power of the grid</span>
<span id="L1130">                                ! spacing to calculate biharmonic viscosity. The final viscosity is the largest</span>
<span id="L1131">                                ! of all viscosity formulations in use. 0.0 means that it&#x27;s not used.</span>
<span id="L1132">SMAGORINSKY_AH = True           !   [Boolean] default = False</span>
<span id="L1133">                                ! If true, use a biharmonic Smagorinsky nonlinear eddy viscosity.</span>
<span id="L1134">LEITH_AH = False                !   [Boolean] default = False</span>
<span id="L1135">                                ! If true, use a biharmonic Leith nonlinear eddy viscosity.</span>
<span id="L1136">USE_LEITHY = False              !   [Boolean] default = False</span>
<span id="L1137">                                ! If true, use a biharmonic Leith nonlinear eddy viscosity together with a</span>
<span id="L1138">                                ! harmonic backscatter.</span>
<span id="L1139">BOUND_AH = True                 !   [Boolean] default = True</span>
<span id="L1140">                                ! If true, the biharmonic coefficient is locally limited to be stable.</span>
<span id="L1141">RE_AH = 0.0                     !   [nondim] default = 0.0</span>
<span id="L1142">                                ! If nonzero, the biharmonic coefficient is scaled so that the biharmonic</span>
<span id="L1143">                                ! Reynolds number is equal to this.</span>
<span id="L1144">SMAG_BI_CONST = 0.06            !   [nondim] default = 0.0</span>
<span id="L1145">                                ! The nondimensional biharmonic Smagorinsky constant, typically 0.015 - 0.06.</span>
<span id="L1146">BOUND_CORIOLIS_BIHARM = True    !   [Boolean] default = True</span>
<span id="L1147">                                ! If true use a viscosity that increases with the square of the velocity shears,</span>
<span id="L1148">                                ! so that the resulting viscous drag is of comparable magnitude to the Coriolis</span>
<span id="L1149">                                ! terms when the velocity differences between adjacent grid points is</span>
<span id="L1150">                                ! 0.5*BOUND_CORIOLIS_VEL.  The default is the value of BOUND_CORIOLIS (or</span>
<span id="L1151">                                ! false).</span>
<span id="L1152">BOUND_CORIOLIS_VEL = 10.0       !   [m s-1] default = 10.0</span>
<span id="L1153">                                ! The velocity scale at which BOUND_CORIOLIS_BIHARM causes the biharmonic drag</span>
<span id="L1154">                                ! to have comparable magnitude to the Coriolis acceleration.  The default is set</span>
<span id="L1155">                                ! by MAXVEL.</span>
<span id="L1156">USE_LAND_MASK_FOR_HVISC = True  !   [Boolean] default = True</span>
<span id="L1157">                                ! If true, use the land mask for the computation of thicknesses at velocity</span>
<span id="L1158">                                ! locations. This eliminates the dependence on arbitrary values over land or</span>
<span id="L1159">                                ! outside of the domain.</span>
<span id="L1160">HORVISC_BOUND_COEF = 0.8        !   [nondim] default = 0.8</span>
<span id="L1161">                                ! The nondimensional coefficient of the ratio of the viscosity bounds to the</span>
<span id="L1162">                                ! theoretical maximum for stability without considering other terms.</span>
<span id="L1163">FRICTWORK_BUG = False           !   [Boolean] default = False</span>
<span id="L1164">                                ! If true, retain an answer-changing bug in calculating the FrictWork, which</span>
<span id="L1165">                                ! cancels the h in thickness flux and the h at velocity point. This isnot</span>
<span id="L1166">                                ! recommended.</span>
<span id="L1167"></span>
<span id="L1168">! === module MOM_vert_friction ===</span>
<span id="L1169">VERT_FRICTION_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1170">                                ! The vintage of the order of arithmetic and expressions in the viscous</span>
<span id="L1171">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L1172">                                ! while higher values use expressions that do not use an arbitrary hard-coded</span>
<span id="L1173">                                ! maximum viscous coupling coefficient between layers.  Values below 20230601</span>
<span id="L1174">                                ! recover a form of the viscosity within the mixed layer that breaks up the</span>
<span id="L1175">                                ! magnitude of the wind stress in some non-Boussinesq cases.</span>
<span id="L1176">DIRECT_STRESS = False           !   [Boolean] default = False</span>
<span id="L1177">                                ! If true, the wind stress is distributed over the topmost HMIX_STRESS of fluid</span>
<span id="L1178">                                ! (like in HYCOM), and an added mixed layer viscosity or a physically based</span>
<span id="L1179">                                ! boundary layer turbulence parameterization is not needed for stability.</span>
<span id="L1180">FIXED_DEPTH_LOTW_ML = False     !   [Boolean] default = False</span>
<span id="L1181">                                ! If true, use a Law-of-the-wall prescription for the mixed layer viscosity</span>
<span id="L1182">                                ! within a boundary layer that is the lesser of HMIX_FIXED and the total depth</span>
<span id="L1183">                                ! of the ocean in a column.</span>
<span id="L1184">LOTW_VISCOUS_ML_FLOOR = False   !   [Boolean] default = False</span>
<span id="L1185">                                ! If true, use a Law-of-the-wall prescription to set a lower bound on the</span>
<span id="L1186">                                ! viscous coupling between layers within the surface boundary layer, based the</span>
<span id="L1187">                                ! distance of interfaces from the surface.  This only acts when there are large</span>
<span id="L1188">                                ! changes in the thicknesses of successive layers or when the viscosity is set</span>
<span id="L1189">                                ! externally and the wind stress has subsequently increased.</span>
<span id="L1190">VON_KARMAN_CONST = 0.41         !   [nondim] default = 0.41</span>
<span id="L1191">                                ! The value the von Karman constant as used for mixed layer viscosity.</span>
<span id="L1192">HARMONIC_VISC = False           !   [Boolean] default = False</span>
<span id="L1193">                                ! If true, use the harmonic mean thicknesses for calculating the vertical</span>
<span id="L1194">                                ! viscosity.</span>
<span id="L1195">HARMONIC_BL_SCALE = 0.0         !   [nondim] default = 0.0</span>
<span id="L1196">                                ! A scale to determine when water is in the boundary layers based solely on</span>
<span id="L1197">                                ! harmonic mean thicknesses for the purpose of determining the extent to which</span>
<span id="L1198">                                ! the thicknesses used in the viscosities are upwinded.</span>
<span id="L1199">USE_GL90_IN_SSW = False         !   [Boolean] default = False</span>
<span id="L1200">                                ! If true, use simpler method to calculate 1/N^2 in GL90 vertical viscosity</span>
<span id="L1201">                                ! coefficient. This method is valid in stacked shallow water mode.</span>
<span id="L1202">CFL_TRUNCATE = 0.5              !   [nondim] default = 0.5</span>
<span id="L1203">                                ! The value of the CFL number that will cause velocity components to be</span>
<span id="L1204">                                ! truncated; instability can occur past 0.5.</span>
<span id="L1205">CFL_REPORT = 0.5                !   [nondim] default = 0.5</span>
<span id="L1206">                                ! The value of the CFL number that causes accelerations to be reported; the</span>
<span id="L1207">                                ! default is CFL_TRUNCATE.</span>
<span id="L1208">CFL_TRUNCATE_RAMP_TIME = 0.0    !   [s] default = 0.0</span>
<span id="L1209">                                ! The time over which the CFL truncation value is ramped up at the beginning of</span>
<span id="L1210">                                ! the run.</span>
<span id="L1211">CFL_TRUNCATE_START = 0.0        !   [nondim] default = 0.0</span>
<span id="L1212">                                ! The start value of the truncation CFL number used when ramping up CFL_TRUNC.</span>
<span id="L1213">STOKES_MIXING_COMBINED = False  !   [Boolean] default = False</span>
<span id="L1214">                                ! Flag to use Stokes drift Mixing via the Lagrangian  current (Eulerian plus</span>
<span id="L1215">                                ! Stokes drift).  Still needs work and testing, so not recommended for use.</span>
<span id="L1216">VEL_UNDERFLOW = 0.0             !   [m s-1] default = 0.0</span>
<span id="L1217">                                ! A negligibly small velocity magnitude below which velocity components are set</span>
<span id="L1218">                                ! to 0.  A reasonable value might be 1e-30 m/s, which is less than an Angstrom</span>
<span id="L1219">                                ! divided by the age of the universe.</span>
<span id="L1220"></span>
<span id="L1221">! === module MOM_barotropic ===</span>
<span id="L1222">USE_BT_CONT_TYPE = True         !   [Boolean] default = True</span>
<span id="L1223">                                ! If true, use a structure with elements that describe effective face areas from</span>
<span id="L1224">                                ! the summed continuity solver as a function the barotropic flow in coupling</span>
<span id="L1225">                                ! between the barotropic and baroclinic flow.  This is only used if SPLIT is</span>
<span id="L1226">                                ! true.</span>
<span id="L1227">INTEGRAL_BT_CONTINUITY = False  !   [Boolean] default = False</span>
<span id="L1228">                                ! If true, use the time-integrated velocity over the barotropic steps to</span>
<span id="L1229">                                ! determine the integrated transports used to update the continuity equation.</span>
<span id="L1230">                                ! Otherwise the transports are the sum of the transports based on a series of</span>
<span id="L1231">                                ! instantaneous velocities and the BT_CONT_TYPE for transports.  This is only</span>
<span id="L1232">                                ! valid if USE_BT_CONT_TYPE = True.</span>
<span id="L1233">BOUND_BT_CORRECTION = True      !   [Boolean] default = False</span>
<span id="L1234">                                ! If true, the corrective pseudo mass-fluxes into the barotropic solver are</span>
<span id="L1235">                                ! limited to values that require less than maxCFL_BT_cont to be accommodated.</span>
<span id="L1236">BT_CONT_CORR_BOUNDS = True      !   [Boolean] default = True</span>
<span id="L1237">                                ! If true, and BOUND_BT_CORRECTION is true, use the BT_cont_type variables to</span>
<span id="L1238">                                ! set limits determined by MAXCFL_BT_CONT on the CFL number of the velocities</span>
<span id="L1239">                                ! that are likely to be driven by the corrective mass fluxes.</span>
<span id="L1240">ADJUST_BT_CONT = False          !   [Boolean] default = False</span>
<span id="L1241">                                ! If true, adjust the curve fit to the BT_cont type that is used by the</span>
<span id="L1242">                                ! barotropic solver to match the transport about which the flow is being</span>
<span id="L1243">                                ! linearized.</span>
<span id="L1244">GRADUAL_BT_ICS = False          !   [Boolean] default = False</span>
<span id="L1245">                                ! If true, adjust the initial conditions for the barotropic solver to the values</span>
<span id="L1246">                                ! from the layered solution over a whole timestep instead of instantly. This is</span>
<span id="L1247">                                ! a decent approximation to the inclusion of sum(u dh_dt) while also correcting</span>
<span id="L1248">                                ! for truncation errors.</span>
<span id="L1249">BT_USE_VISC_REM_U_UH0 = False   !   [Boolean] default = False</span>
<span id="L1250">                                ! If true, use the viscous remnants when estimating the barotropic velocities</span>
<span id="L1251">                                ! that were used to calculate uh0 and vh0.  False is probably the better choice.</span>
<span id="L1252">NONLIN_BT_CONT_UPDATE_PERIOD = 1 ! default = 1</span>
<span id="L1253">                                ! If NONLINEAR_BT_CONTINUITY is true, this is the number of barotropic time</span>
<span id="L1254">                                ! steps between updates to the face areas, or 0 to update only before the</span>
<span id="L1255">                                ! barotropic stepping.</span>
<span id="L1256">BT_PROJECT_VELOCITY = True      !   [Boolean] default = False</span>
<span id="L1257">                                ! If true, step the barotropic velocity first and project out the velocity</span>
<span id="L1258">                                ! tendency by 1+BEBT when calculating the transport.  The default (false) is to</span>
<span id="L1259">                                ! use a predictor continuity step to find the pressure field, and then to do a</span>
<span id="L1260">                                ! corrector continuity step using a weighted average of the old and new</span>
<span id="L1261">                                ! velocities, with weights of (1-BEBT) and BEBT.</span>
<span id="L1262">BT_NONLIN_STRESS = False        !   [Boolean] default = False</span>
<span id="L1263">                                ! If true, use the full depth of the ocean at the start of the barotropic step</span>
<span id="L1264">                                ! when calculating the surface stress contribution to the barotropic</span>
<span id="L1265">                                ! acclerations.  Otherwise use the depth based on bathyT.</span>
<span id="L1266">DYNAMIC_SURFACE_PRESSURE = False !   [Boolean] default = False</span>
<span id="L1267">                                ! If true, add a dynamic pressure due to a viscous ice shelf, for instance.</span>
<span id="L1268">BT_CORIOLIS_SCALE = 1.0         !   [nondim] default = 1.0</span>
<span id="L1269">                                ! A factor by which the barotropic Coriolis anomaly terms are scaled.</span>
<span id="L1270">BAROTROPIC_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1271">                                ! The vintage of the expressions in the barotropic solver. Values below 20190101</span>
<span id="L1272">                                ! recover the answers from the end of 2018, while higher values use more</span>
<span id="L1273">                                ! efficient or general expressions.</span>
<span id="L1274">VISC_REM_BT_WEIGHT_BUG = True   !   [Boolean] default = True</span>
<span id="L1275">                                ! If true, recover a bug in barotropic solver that uses an unnormalized weight</span>
<span id="L1276">                                ! function for vertical averages of baroclinic velocity and forcing. Default of</span>
<span id="L1277">                                ! this flag is set by VISC_REM_BUG.</span>
<span id="L1278">TIDAL_SAL_FLATHER = False       !   [Boolean] default = False</span>
<span id="L1279">                                ! If true, then apply adjustments to the external gravity wave speed used with</span>
<span id="L1280">                                ! the Flather OBC routine consistent with the barotropic solver. This applies to</span>
<span id="L1281">                                ! cases with  tidal forcing using the scalar self-attraction approximation. The</span>
<span id="L1282">                                ! default is currently False in order to retain previous answers but should be</span>
<span id="L1283">                                ! set to True for new experiments</span>
<span id="L1284">SADOURNY = True                 !   [Boolean] default = True</span>
<span id="L1285">                                ! If true, the Coriolis terms are discretized with the Sadourny (1975) energy</span>
<span id="L1286">                                ! conserving scheme, otherwise the Arakawa &amp; Hsu scheme is used.  If the</span>
<span id="L1287">                                ! internal deformation radius is not resolved, the Sadourny scheme should</span>
<span id="L1288">                                ! probably be used.</span>
<span id="L1289">BT_THICK_SCHEME = &quot;FROM_BT_CONT&quot; ! default = &quot;FROM_BT_CONT&quot;</span>
<span id="L1290">                                ! A string describing the scheme that is used to set the open face areas used</span>
<span id="L1291">                                ! for barotropic transport and the relative weights of the accelerations. Valid</span>
<span id="L1292">                                ! values are:</span>
<span id="L1293">                                !    ARITHMETIC - arithmetic mean layer thicknesses</span>
<span id="L1294">                                !    HARMONIC - harmonic mean layer thicknesses</span>
<span id="L1295">                                !    HYBRID (the default) - use arithmetic means for</span>
<span id="L1296">                                !       layers above the shallowest bottom, the harmonic</span>
<span id="L1297">                                !       mean for layers below, and a weighted average for</span>
<span id="L1298">                                !       layers that straddle that depth</span>
<span id="L1299">                                !    FROM_BT_CONT - use the average thicknesses kept</span>
<span id="L1300">                                !       in the h_u and h_v fields of the BT_cont_type</span>
<span id="L1301">BT_STRONG_DRAG = False          !   [Boolean] default = False</span>
<span id="L1302">                                ! If true, use a stronger estimate of the retarding effects of strong bottom</span>
<span id="L1303">                                ! drag, by making it implicit with the barotropic time-step instead of implicit</span>
<span id="L1304">                                ! with the baroclinic time-step and dividing by the number of barotropic steps.</span>
<span id="L1305">BT_LINEAR_WAVE_DRAG = False     !   [Boolean] default = False</span>
<span id="L1306">                                ! If true, apply a linear drag to the barotropic velocities, using rates set by</span>
<span id="L1307">                                ! lin_drag_u &amp; _v divided by the depth of the ocean.  This was introduced to</span>
<span id="L1308">                                ! facilitate tide modeling.</span>
<span id="L1309">BT_LINEAR_FREQ_DRAG = False     !   [Boolean] default = False</span>
<span id="L1310">                                ! If true, apply frequency-dependent drag to the tidal velocities. The streaming</span>
<span id="L1311">                                ! band-pass filter must be turned on.</span>
<span id="L1312">CLIP_BT_VELOCITY = False        !   [Boolean] default = False</span>
<span id="L1313">                                ! If true, limit any velocity components that exceed CFL_TRUNCATE.  This should</span>
<span id="L1314">                                ! only be used as a desperate debugging measure.</span>
<span id="L1315">MAXCFL_BT_CONT = 0.25           !   [nondim] default = 0.25</span>
<span id="L1316">                                ! The maximum permitted CFL number associated with the barotropic accelerations</span>
<span id="L1317">                                ! from the summed velocities times the time-derivatives of thicknesses.</span>
<span id="L1318">DT_BT_FILTER = -0.25            !   [sec or nondim] default = -0.25</span>
<span id="L1319">                                ! A time-scale over which the barotropic mode solutions are filtered, in seconds</span>
<span id="L1320">                                ! if positive, or as a fraction of DT if negative. When used this can never be</span>
<span id="L1321">                                ! taken to be longer than 2*dt.  Set this to 0 to apply no filtering.</span>
<span id="L1322">G_BT_EXTRA = 0.0                !   [nondim] default = 0.0</span>
<span id="L1323">                                ! A nondimensional factor by which gtot is enhanced.</span>
<span id="L1324">SSH_EXTRA = 10.0                !   [m] default = 10.0</span>
<span id="L1325">                                ! An estimate of how much higher SSH might get, for use in calculating the safe</span>
<span id="L1326">                                ! external wave speed. The default is the minimum of 10 m or 5% of</span>
<span id="L1327">                                ! MAXIMUM_DEPTH.</span>
<span id="L1328">LINEARIZED_BT_CORIOLIS = True   !   [Boolean] default = True</span>
<span id="L1329">                                ! If true use the bottom depth instead of the total water column thickness in</span>
<span id="L1330">                                ! the barotropic Coriolis term calculations.</span>
<span id="L1331">BEBT = 0.2                      !   [nondim] default = 0.1</span>
<span id="L1332">                                ! BEBT determines whether the barotropic time stepping uses the forward-backward</span>
<span id="L1333">                                ! time-stepping scheme or a backward Euler scheme. BEBT is valid in the range</span>
<span id="L1334">                                ! from 0 (for a forward-backward treatment of nonrotating gravity waves) to 1</span>
<span id="L1335">                                ! (for a backward Euler treatment). In practice, BEBT must be greater than about</span>
<span id="L1336">                                ! 0.05.</span>
<span id="L1337">DTBT = -0.95                    !   [s or nondim] default = -0.98</span>
<span id="L1338">                                ! The barotropic time step, in s. DTBT is only used with the split explicit time</span>
<span id="L1339">                                ! stepping. To set the time step automatically based the maximum stable value</span>
<span id="L1340">                                ! use 0, or a negative value gives the fraction of the stable value. Setting</span>
<span id="L1341">                                ! DTBT to 0 is the same as setting it to -0.98. The value of DTBT that will</span>
<span id="L1342">                                ! actually be used is an integer fraction of DT, rounding down.</span>
<span id="L1343">BT_USE_OLD_CORIOLIS_BRACKET_BUG = False !   [Boolean] default = False</span>
<span id="L1344">                                ! If True, use an order of operations that is not bitwise rotationally symmetric</span>
<span id="L1345">                                ! in the meridional Coriolis term of the barotropic solver.</span>
<span id="L1346">MASK_COASTAL_PRESSURE_FORCE = False !   [Boolean] default = False</span>
<span id="L1347">                                ! If true, use the land masks to zero out the diagnosed barotropic pressure</span>
<span id="L1348">                                ! gradient accelerations at coastal or land points.  This changes diagnostics</span>
<span id="L1349">                                ! and improves the reproducibility of certain debugging checksums, but it does</span>
<span id="L1350">                                ! not alter the solutions themselves.</span>
<span id="L1351"></span>
<span id="L1352">! === module MOM_mixed_layer_restrat ===</span>
<span id="L1353">MIXEDLAYER_RESTRAT = True       !   [Boolean] default = False</span>
<span id="L1354">                                ! If true, a density-gradient dependent re-stratifying flow is imposed in the</span>
<span id="L1355">                                ! mixed layer. Can be used in ALE mode without restriction but in layer mode can</span>
<span id="L1356">                                ! only be used if BULKMIXEDLAYER is true.</span>
<span id="L1357">MLE%</span>
<span id="L1358">%MLE</span>
<span id="L1359">FOX_KEMPER_ML_RESTRAT_COEF = 5.0 !   [nondim] default = 0.0</span>
<span id="L1360">                                ! A nondimensional coefficient that is proportional to the ratio of the</span>
<span id="L1361">                                ! deformation radius to the dominant lengthscale of the submesoscale mixed layer</span>
<span id="L1362">                                ! instabilities, times the minimum of the ratio of the mesoscale eddy kinetic</span>
<span id="L1363">                                ! energy to the large-scale geostrophic kinetic energy or 1 plus the square of</span>
<span id="L1364">                                ! the grid spacing over the deformation radius, as detailed by Fox-Kemper et al.</span>
<span id="L1365">                                ! (2011)</span>
<span id="L1366">USE_STANLEY_ML = False          !   [Boolean] default = False</span>
<span id="L1367">                                ! If true, turn on Stanley SGS T variance parameterization in ML restrat code.</span>
<span id="L1368">KV_RESTRAT = 0.0                !   [m2 s-1] default = 0.0</span>
<span id="L1369">                                ! A small viscosity that sets a floor on the momentum mixing rate during</span>
<span id="L1370">                                ! restratification.  If this is positive, it will prevent some possible</span>
<span id="L1371">                                ! divisions by zero even if ustar, RESTRAT_USTAR_MIN, and f are all 0.</span>
<span id="L1372">RESTRAT_USTAR_MIN = 1.45842E-18 !   [m s-1] default = 1.45842E-18</span>
<span id="L1373">                                ! The minimum value of ustar that will be used by the mixed layer</span>
<span id="L1374">                                ! restratification module.  This can be tiny, but if this is greater than 0, it</span>
<span id="L1375">                                ! will prevent divisions by zero when f and KV_RESTRAT are zero.</span>
<span id="L1376"></span>
<span id="L1377">! === module MOM_diagnostics ===</span>
<span id="L1378">DIAG_EBT_MONO_N2_COLUMN_FRACTION = 0.0 !   [nondim] default = 0.0</span>
<span id="L1379">                                ! The lower fraction of water column over which N2 is limited as monotonic for</span>
<span id="L1380">                                ! the purposes of calculating the equivalent barotropic wave speed.</span>
<span id="L1381">DIAG_EBT_MONO_N2_DEPTH = -1.0   !   [m] default = -1.0</span>
<span id="L1382">                                ! The depth below which N2 is limited as monotonic for the purposes of</span>
<span id="L1383">                                ! calculating the equivalent barotropic wave speed.</span>
<span id="L1384">INTWAVE_REMAPPING_USE_OM4_SUBCELLS = True !   [Boolean] default = True</span>
<span id="L1385">                                ! If true, use the OM4 remapping-via-subcells algorithm for calculating EBT</span>
<span id="L1386">                                ! structure. See REMAPPING_USE_OM4_SUBCELLS for details. We recommend setting</span>
<span id="L1387">                                ! this option to false.</span>
<span id="L1388"></span>
<span id="L1389">! === module MOM_diabatic_driver ===</span>
<span id="L1390">! The following parameters are used for diabatic processes.</span>
<span id="L1391">USE_LEGACY_DIABATIC_DRIVER = True !   [Boolean] default = True</span>
<span id="L1392">                                ! If true, use a legacy version of the diabatic subroutine. This is temporary</span>
<span id="L1393">                                ! and is needed to avoid change in answers.</span>
<span id="L1394">ENERGETICS_SFC_PBL = False      !   [Boolean] default = False</span>
<span id="L1395">                                ! If true, use an implied energetics planetary boundary layer scheme to</span>
<span id="L1396">                                ! determine the diffusivity and viscosity in the surface boundary layer.</span>
<span id="L1397">EPBL_IS_ADDITIVE = True         !   [Boolean] default = True</span>
<span id="L1398">                                ! If true, the diffusivity from ePBL is added to all other diffusivities.</span>
<span id="L1399">                                ! Otherwise, the larger of kappa-shear and ePBL diffusivities are used.</span>
<span id="L1400">ML_MIX_FIRST = 0.0              !   [nondim] default = 0.0</span>
<span id="L1401">                                ! The fraction of the mixed layer mixing that is applied before interior</span>
<span id="L1402">                                ! diapycnal mixing.  0 by default.</span>
<span id="L1403">INTERNAL_TIDES = False          !   [Boolean] default = False</span>
<span id="L1404">                                ! If true, use the code that advances a separate set of equations for the</span>
<span id="L1405">                                ! internal tide energy density.</span>
<span id="L1406">MASSLESS_MATCH_TARGETS = True   !   [Boolean] default = True</span>
<span id="L1407">                                ! If true, the temperature and salinity of massless layers are kept consistent</span>
<span id="L1408">                                ! with their target densities. Otherwise the properties of massless layers</span>
<span id="L1409">                                ! evolve diffusively to match massive neighboring layers.</span>
<span id="L1410">AGGREGATE_FW_FORCING = True     !   [Boolean] default = True</span>
<span id="L1411">                                ! If true, the net incoming and outgoing fresh water fluxes are combined and</span>
<span id="L1412">                                ! applied as either incoming or outgoing depending on the sign of the net. If</span>
<span id="L1413">                                ! false, the net incoming fresh water flux is added to the model and thereafter</span>
<span id="L1414">                                ! the net outgoing is removed from the topmost non-vanished layers of the</span>
<span id="L1415">                                ! updated state.</span>
<span id="L1416">MIX_BOUNDARY_TRACERS = True     !   [Boolean] default = True</span>
<span id="L1417">                                ! If true, mix the passive tracers in massless layers at the bottom into the</span>
<span id="L1418">                                ! interior as though a diffusivity of KD_MIN_TR were operating.</span>
<span id="L1419">KD_MIN_TR = 2.0E-06             !   [m2 s-1] default = 2.0E-06</span>
<span id="L1420">                                ! A minimal diffusivity that should always be applied to tracers, especially in</span>
<span id="L1421">                                ! massless layers near the bottom. The default is 0.1*KD.</span>
<span id="L1422">KD_BBL_TR = 0.0                 !   [m2 s-1] default = 0.0</span>
<span id="L1423">                                ! A bottom boundary layer tracer diffusivity that will allow for explicitly</span>
<span id="L1424">                                ! specified bottom fluxes. The entrainment at the bottom is at least</span>
<span id="L1425">                                ! sqrt(Kd_BBL_tr*dt) over the same distance.</span>
<span id="L1426">TRACER_TRIDIAG = False          !   [Boolean] default = False</span>
<span id="L1427">                                ! If true, use the passive tracer tridiagonal solver for T and S</span>
<span id="L1428">MINIMUM_FORCING_DEPTH = 0.001   !   [m] default = 0.001</span>
<span id="L1429">                                ! The smallest depth over which forcing can be applied. This only takes effect</span>
<span id="L1430">                                ! when near-surface layers become thin relative to this scale, in which case the</span>
<span id="L1431">                                ! forcing tendencies scaled down by distributing the forcing over this depth</span>
<span id="L1432">                                ! scale.</span>
<span id="L1433">EVAP_CFL_LIMIT = 0.8            !   [nondim] default = 0.8</span>
<span id="L1434">                                ! The largest fraction of a layer than can be lost to forcing (e.g. evaporation,</span>
<span id="L1435">                                ! sea-ice formation) in one time-step. The unused mass loss is passed down</span>
<span id="L1436">                                ! through the column.</span>
<span id="L1437">MLD_EN_VALS = 25.0, 2500.0, 2.5E+05 !   [J/m2] default = 25.0, 2500.0, 2.5E+05</span>
<span id="L1438">                                ! The energy values used to compute MLDs.  If not set (or all set to 0.), the</span>
<span id="L1439">                                ! default will overwrite to 25., 2500., 250000.</span>
<span id="L1440">BMLD_EN_VALS = 25.0, 2500.0, 2.5E+05 !   [J/m2] default = 25.0, 2500.0, 2.5E+05</span>
<span id="L1441">                                ! The energy values used to compute Bottom MLDs.  If not set (or all set to 0.),</span>
<span id="L1442">                                ! the default will overwrite to 25., 2500., 250000.</span>
<span id="L1443">DIAG_MLD_DENSITY_DIFF = 0.1     !   [kg/m3] default = 0.1</span>
<span id="L1444">                                ! The density difference used to determine a diagnostic mixed layer depth,</span>
<span id="L1445">                                ! MLD_user, following the definition of Levitus 1982. The MLD is the depth at</span>
<span id="L1446">                                ! which the density is larger than the surface density by the specified amount.</span>
<span id="L1447">DIAG_DEPTH_SUBML_N2 = 50.0      !   [m] default = 50.0</span>
<span id="L1448">                                ! The distance over which to calculate a diagnostic of the stratification at the</span>
<span id="L1449">                                ! base of the mixed layer.</span>
<span id="L1450"></span>
<span id="L1451">! === module MOM_CVMix_KPP ===</span>
<span id="L1452">! This is the MOM wrapper to CVMix:KPP</span>
<span id="L1453">! See http://cvmix.github.io/</span>
<span id="L1454">USE_KPP = False                 !   [Boolean] default = False</span>
<span id="L1455">                                ! If true, turns on the [CVMix] KPP scheme of Large et al., 1994, to calculate</span>
<span id="L1456">                                ! diffusivities and non-local transport in the OBL.</span>
<span id="L1457"></span>
<span id="L1458">! === module MOM_CVMix_conv ===</span>
<span id="L1459">! Parameterization of enhanced mixing due to convection via CVMix</span>
<span id="L1460">USE_CVMix_CONVECTION = False    !   [Boolean] default = False</span>
<span id="L1461">                                ! If true, turns on the enhanced mixing due to convection via CVMix. This scheme</span>
<span id="L1462">                                ! increases diapycnal diffs./viscs. at statically unstable interfaces. Relevant</span>
<span id="L1463">                                ! parameters are contained in the CVMix_CONVECTION% parameter block.</span>
<span id="L1464"></span>
<span id="L1465">! === module MOM_entrain_diffusive ===</span>
<span id="L1466">MAX_ENT_IT = 20                 ! default = 5</span>
<span id="L1467">                                ! The maximum number of iterations that may be used to calculate the interior</span>
<span id="L1468">                                ! diapycnal entrainment.</span>
<span id="L1469">TOLERANCE_ENT = 1.0E-05         !   [m] default = 1.341640786499874E-05</span>
<span id="L1470">                                ! The tolerance with which to solve for entrainment values.</span>
<span id="L1471">ENTRAIN_DIFFUSIVE_MAX_ENT = 1.0E+04 !   [m] default = 1.0E+04</span>
<span id="L1472">                                ! A large ceiling on the maximum permitted amount of entrainment across each</span>
<span id="L1473">                                ! interface between the mixed and buffer layers within a timestep.</span>
<span id="L1474"></span>
<span id="L1475">! === module MOM_set_diffusivity ===</span>
<span id="L1476">FLUX_RI_MAX = 0.2               !   [nondim] default = 0.2</span>
<span id="L1477">                                ! The flux Richardson number where the stratification is large enough that N2 &gt;</span>
<span id="L1478">                                ! omega2.  The full expression for the Flux Richardson number is usually</span>
<span id="L1479">                                ! FLUX_RI_MAX*N2/(N2+OMEGA2).</span>
<span id="L1480">SET_DIFF_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1481">                                ! The vintage of the order of arithmetic and expressions in the set diffusivity</span>
<span id="L1482">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L1483">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L1484">                                ! Values above 20250301 also use less confusing expressions to set the</span>
<span id="L1485">                                ! bottom-drag generated diffusivity when USE_LOTW_BBL_DIFFUSIVITY is false.</span>
<span id="L1486"></span>
<span id="L1487">! === module MOM_tidal_mixing ===</span>
<span id="L1488">! Vertical Tidal Mixing Parameterization</span>
<span id="L1489">USE_CVMix_TIDAL = False         !   [Boolean] default = False</span>
<span id="L1490">                                ! If true, turns on tidal mixing via CVMix</span>
<span id="L1491">INT_TIDE_DISSIPATION = False    !   [Boolean] default = False</span>
<span id="L1492">                                ! If true, use an internal tidal dissipation scheme to drive diapycnal mixing,</span>
<span id="L1493">                                ! along the lines of St. Laurent et al. (2002) and Simmons et al. (2004).</span>
<span id="L1494">ML_RADIATION = False            !   [Boolean] default = False</span>
<span id="L1495">                                ! If true, allow a fraction of TKE available from wind work to penetrate below</span>
<span id="L1496">                                ! the base of the mixed layer with a vertical decay scale determined by the</span>
<span id="L1497">                                ! minimum of: (1) The depth of the mixed layer, (2) an Ekman length scale.</span>
<span id="L1498">BBL_EFFIC = 0.2                 !   [nondim] default = 0.2</span>
<span id="L1499">                                ! The efficiency with which the energy extracted by bottom drag drives BBL</span>
<span id="L1500">                                ! diffusion.  This is only used if BOTTOMDRAGLAW is true.</span>
<span id="L1501">BBL_MIXING_MAX_DECAY = 200.0    !   [m] default = 200.0</span>
<span id="L1502">                                ! The maximum decay scale for the BBL diffusion, or 0 to allow the mixing to</span>
<span id="L1503">                                ! penetrate as far as stratification and rotation permit.  The default for now</span>
<span id="L1504">                                ! is 200 m. This is only used if BOTTOMDRAGLAW is true.</span>
<span id="L1505">BBL_MIXING_AS_MAX = True        !   [Boolean] default = True</span>
<span id="L1506">                                ! If true, take the maximum of the diffusivity from the BBL mixing and the other</span>
<span id="L1507">                                ! diffusivities. Otherwise, diffusivity from the BBL_mixing is simply added.</span>
<span id="L1508">USE_LOTW_BBL_DIFFUSIVITY = False !   [Boolean] default = False</span>
<span id="L1509">                                ! If true, uses a simple, imprecise but non-coordinate dependent, model of BBL</span>
<span id="L1510">                                ! mixing diffusivity based on Law of the Wall. Otherwise, uses the original BBL</span>
<span id="L1511">                                ! scheme.</span>
<span id="L1512">DRAG_DIFFUSIVITY_ANSWER_DATE = 20250101 ! default = 99991231</span>
<span id="L1513">                                ! The vintage of the order of arithmetic in the drag diffusivity calculations.</span>
<span id="L1514">                                ! Values above 20250301 use less confusing expressions to set the bottom-drag</span>
<span id="L1515">                                ! generated diffusivity when USE_LOTW_BBL_DIFFUSIVITY is false.</span>
<span id="L1516">DZ_BBL_AVG_MIN = 0.0            !   [m] default = 0.0</span>
<span id="L1517">                                ! A minimal distance over which to average to determine the average bottom</span>
<span id="L1518">                                ! boundary layer density.</span>
<span id="L1519">SIMPLE_TKE_TO_KD = False        !   [Boolean] default = False</span>
<span id="L1520">                                ! If true, uses a simple estimate of Kd/TKE that will work for arbitrary</span>
<span id="L1521">                                ! vertical coordinates. If false, calculates Kd/TKE and bounds based on exact</span>
<span id="L1522">                                ! energetics for an isopycnal layer-formulation.</span>
<span id="L1523"></span>
<span id="L1524">! === module MOM_bkgnd_mixing ===</span>
<span id="L1525">! Adding static vertical background mixing coefficients</span>
<span id="L1526">KD = 2.0E-05                    !   [m2 s-1] default = 0.0</span>
<span id="L1527">                                ! The background diapycnal diffusivity of density in the interior. Zero or the</span>
<span id="L1528">                                ! molecular value, ~1e-7 m2 s-1, may be used.</span>
<span id="L1529">KD_MIN = 2.0E-07                !   [m2 s-1] default = 2.0E-07</span>
<span id="L1530">                                ! The minimum diapycnal diffusivity.</span>
<span id="L1531">BRYAN_LEWIS_DIFFUSIVITY = False !   [Boolean] default = False</span>
<span id="L1532">                                ! If true, use a Bryan &amp; Lewis (JGR 1979) like tanh profile of background</span>
<span id="L1533">                                ! diapycnal diffusivity with depth. This is done via CVMix.</span>
<span id="L1534">HORIZ_VARYING_BACKGROUND = False !   [Boolean] default = False</span>
<span id="L1535">                                ! If true, apply vertically uniform, latitude-dependent background diffusivity,</span>
<span id="L1536">                                ! as described in Danabasoglu et al., 2012</span>
<span id="L1537">PRANDTL_BKGND = 1.0             !   [nondim] default = 1.0</span>
<span id="L1538">                                ! Turbulent Prandtl number used to convert vertical background diffusivities</span>
<span id="L1539">                                ! into viscosities.</span>
<span id="L1540">HENYEY_IGW_BACKGROUND = False   !   [Boolean] default = False</span>
<span id="L1541">                                ! If true, use a latitude-dependent scaling for the near surface background</span>
<span id="L1542">                                ! diffusivity, as described in Harrison &amp; Hallberg, JPO 2008.</span>
<span id="L1543">KD_TANH_LAT_FN = False          !   [Boolean] default = False</span>
<span id="L1544">                                ! If true, use a tanh dependence of Kd_sfc on latitude, like CM2.1/CM2M.  There</span>
<span id="L1545">                                ! is no physical justification for this form, and it can not be used with</span>
<span id="L1546">                                ! HENYEY_IGW_BACKGROUND.</span>
<span id="L1547">KD_MAX = -1.0                   !   [m2 s-1] default = -1.0</span>
<span id="L1548">                                ! The maximum permitted increment for the diapycnal diffusivity from TKE-based</span>
<span id="L1549">                                ! parameterizations, or a negative value for no limit.</span>
<span id="L1550">KD_ADD = 0.0                    !   [m2 s-1] default = 0.0</span>
<span id="L1551">                                ! A uniform diapycnal diffusivity that is added everywhere without any filtering</span>
<span id="L1552">                                ! or scaling.</span>
<span id="L1553">USER_CHANGE_DIFFUSIVITY = False !   [Boolean] default = False</span>
<span id="L1554">                                ! If true, call user-defined code to change the diffusivity.</span>
<span id="L1555">DISSIPATION_MIN = 0.0           !   [W m-3] default = 0.0</span>
<span id="L1556">                                ! The minimum dissipation by which to determine a lower bound of Kd (a floor).</span>
<span id="L1557">DISSIPATION_N0 = 0.0            !   [W m-3] default = 0.0</span>
<span id="L1558">                                ! The intercept when N=0 of the N-dependent expression used to set a minimum</span>
<span id="L1559">                                ! dissipation by which to determine a lower bound of Kd (a floor): A in eps_min</span>
<span id="L1560">                                ! = A + B*N.</span>
<span id="L1561">DISSIPATION_N1 = 0.0            !   [J m-3] default = 0.0</span>
<span id="L1562">                                ! The coefficient multiplying N, following Gargett, used to set a minimum</span>
<span id="L1563">                                ! dissipation by which to determine a lower bound of Kd (a floor): B in eps_min</span>
<span id="L1564">                                ! = A + B*N</span>
<span id="L1565">DISSIPATION_KD_MIN = 0.0        !   [m2 s-1] default = 0.0</span>
<span id="L1566">                                ! The minimum vertical diffusivity applied as a floor.</span>
<span id="L1567">DOUBLE_DIFFUSION = False        !   [Boolean] default = False</span>
<span id="L1568">                                ! If true, increase diffusivites for temperature or salinity based on the</span>
<span id="L1569">                                ! double-diffusive parameterization described in Large et al. (1994).</span>
<span id="L1570"></span>
<span id="L1571">! === module MOM_kappa_shear ===</span>
<span id="L1572">! Parameterization of shear-driven turbulence following Jackson, Hallberg and Legg, JPO 2008</span>
<span id="L1573">USE_JACKSON_PARAM = True        !   [Boolean] default = False</span>
<span id="L1574">                                ! If true, use the Jackson-Hallberg-Legg (JPO 2008) shear mixing</span>
<span id="L1575">                                ! parameterization.</span>
<span id="L1576">VERTEX_SHEAR = False            !   [Boolean] default = False</span>
<span id="L1577">                                ! If true, do the calculations of the shear-driven mixing at the cell vertices</span>
<span id="L1578">                                ! (i.e., the vorticity points).</span>
<span id="L1579">VERTEX_SHEAR_THICKNESS_MEAN = False !   [Boolean] default = False</span>
<span id="L1580">                                ! If true, apply thickness weighting to horizontal averagings of diffusivity to</span>
<span id="L1581">                                ! tracer points in the kappa shear solver.</span>
<span id="L1582">RINO_CRIT = 0.25                !   [nondim] default = 0.25</span>
<span id="L1583">                                ! The critical Richardson number for shear mixing.</span>
<span id="L1584">SHEARMIX_RATE = 0.089           !   [nondim] default = 0.089</span>
<span id="L1585">                                ! A nondimensional rate scale for shear-driven entrainment. Jackson et al find</span>
<span id="L1586">                                ! values in the range of 0.085-0.089.</span>
<span id="L1587">MAX_RINO_IT = 25                !   [nondim] default = 50</span>
<span id="L1588">                                ! The maximum number of iterations that may be used to estimate the Richardson</span>
<span id="L1589">                                ! number driven mixing.</span>
<span id="L1590">KD_KAPPA_SHEAR_0 = 2.0E-05      !   [m2 s-1] default = 2.0E-05</span>
<span id="L1591">                                ! The background diffusivity that is used to smooth the density and shear</span>
<span id="L1592">                                ! profiles before solving for the diffusivities.  The default is the greater of</span>
<span id="L1593">                                ! KD and 1e-7 m2 s-1.</span>
<span id="L1594">KD_SEED_KAPPA_SHEAR = 1.0       !   [m2 s-1] default = 1.0</span>
<span id="L1595">                                ! A moderately large seed value of diapycnal diffusivity that is used as a</span>
<span id="L1596">                                ! starting turbulent diffusivity in the iterations to find an energetically</span>
<span id="L1597">                                ! constrained solution for the shear-driven diffusivity.</span>
<span id="L1598">KD_TRUNC_KAPPA_SHEAR = 2.0E-07  !   [m2 s-1] default = 2.0E-07</span>
<span id="L1599">                                ! The value of shear-driven diffusivity that is considered negligible and is</span>
<span id="L1600">                                ! rounded down to 0. The default is 1% of KD_KAPPA_SHEAR_0.</span>
<span id="L1601">FRI_CURVATURE = -0.97           !   [nondim] default = -0.97</span>
<span id="L1602">                                ! The nondimensional curvature of the function of the Richardson number in the</span>
<span id="L1603">                                ! kappa source term in the Jackson et al. scheme.</span>
<span id="L1604">TKE_N_DECAY_CONST = 0.24        !   [nondim] default = 0.24</span>
<span id="L1605">                                ! The coefficient for the decay of TKE due to stratification (i.e. proportional</span>
<span id="L1606">                                ! to N*tke). The values found by Jackson et al. are 0.24-0.28.</span>
<span id="L1607">TKE_SHEAR_DECAY_CONST = 0.14    !   [nondim] default = 0.14</span>
<span id="L1608">                                ! The coefficient for the decay of TKE due to shear (i.e. proportional to</span>
<span id="L1609">                                ! |S|*tke). The values found by Jackson et al. are 0.14-0.12.</span>
<span id="L1610">KAPPA_BUOY_SCALE_COEF = 0.82    !   [nondim] default = 0.82</span>
<span id="L1611">                                ! The coefficient for the buoyancy length scale in the kappa equation.  The</span>
<span id="L1612">                                ! values found by Jackson et al. are in the range of 0.81-0.86.</span>
<span id="L1613">KAPPA_N_OVER_S_SCALE_COEF2 = 0.0 !   [nondim] default = 0.0</span>
<span id="L1614">                                ! The square of the ratio of the coefficients of the buoyancy and shear scales</span>
<span id="L1615">                                ! in the diffusivity equation, Set this to 0 (the default) to eliminate the</span>
<span id="L1616">                                ! shear scale. This is only used if USE_JACKSON_PARAM is true.</span>
<span id="L1617">LZ_RESCALE = 1.0                !   [nondim] default = 1.0</span>
<span id="L1618">                                ! A coefficient to rescale the distance to the nearest solid boundary. This</span>
<span id="L1619">                                ! adjustment is to account for regions where 3 dimensional turbulence prevents</span>
<span id="L1620">                                ! the growth of shear instabilies [nondim].</span>
<span id="L1621">KAPPA_SHEAR_TOL_ERR = 0.1       !   [nondim] default = 0.1</span>
<span id="L1622">                                ! The fractional error in kappa that is tolerated. Iteration stops when changes</span>
<span id="L1623">                                ! between subsequent iterations are smaller than this everywhere in a column.</span>
<span id="L1624">                                ! The peak diffusivities usually converge most rapidly, and have much smaller</span>
<span id="L1625">                                ! errors than this.</span>
<span id="L1626">TKE_BACKGROUND = 0.0            !   [m2 s-2] default = 0.0</span>
<span id="L1627">                                ! A background level of TKE used in the first iteration of the kappa equation.</span>
<span id="L1628">                                ! TKE_BACKGROUND could be 0.</span>
<span id="L1629">KAPPA_SHEAR_ELIM_MASSLESS = True !   [Boolean] default = True</span>
<span id="L1630">                                ! If true, massless layers are merged with neighboring massive layers in this</span>
<span id="L1631">                                ! calculation.  The default is true and I can think of no good reason why it</span>
<span id="L1632">                                ! should be false. This is only used if USE_JACKSON_PARAM is true.</span>
<span id="L1633">MAX_KAPPA_SHEAR_IT = 13         ! default = 13</span>
<span id="L1634">                                ! The maximum number of iterations that may be used to estimate the</span>
<span id="L1635">                                ! time-averaged diffusivity.</span>
<span id="L1636">PRANDTL_TURB = 0.0              !   [nondim] default = 1.0</span>
<span id="L1637">                                ! The turbulent Prandtl number applied to shear instability.</span>
<span id="L1638">KAPPA_SHEAR_MAX_KAP_SRC_CHG = 10.0 !   [nondim] default = 10.0</span>
<span id="L1639">                                ! The maximum permitted increase in the kappa source within an iteration</span>
<span id="L1640">                                ! relative to the local source; this must be greater than 1.  The lower limit</span>
<span id="L1641">                                ! for the permitted fractional decrease is (1 - 0.5/kappa_src_max_chg).  These</span>
<span id="L1642">                                ! limits could perhaps be made dynamic with an improved iterative solver.</span>
<span id="L1643">KAPPA_SHEAR_ITER_BUG = False    !   [Boolean] default = False</span>
<span id="L1644">                                ! If true, use an older, dimensionally inconsistent estimate of the derivative</span>
<span id="L1645">                                ! of diffusivity with energy in the Newton&#x27;s method iteration.  The bug causes</span>
<span id="L1646">                                ! undercorrections when dz &gt; 1 m.</span>
<span id="L1647">KAPPA_SHEAR_ALL_LAYER_TKE_BUG = False !   [Boolean] default = False</span>
<span id="L1648">                                ! If true, report back the latest estimate of TKE instead of the time average</span>
<span id="L1649">                                ! TKE when there is mass in all layers.  Otherwise always report the time</span>
<span id="L1650">                                ! averaged TKE, as is currently done when there are some massless layers.</span>
<span id="L1651">USE_RESTRICTIVE_TOLERANCE_CHECK = False !   [Boolean] default = False</span>
<span id="L1652">                                ! If true, uses the more restrictive tolerance check to determine if a timestep</span>
<span id="L1653">                                ! is acceptable for the KS_it outer iteration loop.  False uses the original</span>
<span id="L1654">                                ! less restrictive check.</span>
<span id="L1655">KAPPA_SHEAR_MERGE_ML = True     !   [Boolean] default = True</span>
<span id="L1656">                                ! If true, combine the mixed layers together before solving the kappa-shear</span>
<span id="L1657">                                ! equations.</span>
<span id="L1658"></span>
<span id="L1659">! === module MOM_CVMix_shear ===</span>
<span id="L1660">! Parameterization of shear-driven turbulence via CVMix (various options)</span>
<span id="L1661">USE_LMD94 = False               !   [Boolean] default = False</span>
<span id="L1662">                                ! If true, use the Large-McWilliams-Doney (JGR 1994) shear mixing</span>
<span id="L1663">                                ! parameterization.</span>
<span id="L1664">USE_PP81 = False                !   [Boolean] default = False</span>
<span id="L1665">                                ! If true, use the Pacanowski and Philander (JPO 1981) shear mixing</span>
<span id="L1666">                                ! parameterization.</span>
<span id="L1667"></span>
<span id="L1668">! === module MOM_CVMix_ddiff ===</span>
<span id="L1669">! Parameterization of mixing due to double diffusion processes via CVMix</span>
<span id="L1670">USE_CVMIX_DDIFF = False         !   [Boolean] default = False</span>
<span id="L1671">                                ! If true, turns on double diffusive processes via CVMix. Note that double</span>
<span id="L1672">                                ! diffusive processes on viscosity are ignored in CVMix, see</span>
<span id="L1673">                                ! http://cvmix.github.io/ for justification.</span>
<span id="L1674"></span>
<span id="L1675">! === module MOM_diabatic_aux ===</span>
<span id="L1676">! The following parameters are used for auxiliary diabatic processes.</span>
<span id="L1677">RECLAIM_FRAZIL = False          !   [Boolean] default = True</span>
<span id="L1678">                                ! If true, try to use any frazil heat deficit to cool any overlying layers down</span>
<span id="L1679">                                ! to the freezing point, thereby avoiding the creation of thin ice when the SST</span>
<span id="L1680">                                ! is above the freezing point.</span>
<span id="L1681">SALT_EXTRACTION_LIMIT = 0.9999  !   [nondim] default = 0.9999</span>
<span id="L1682">                                ! An upper limit on the fraction of the salt in a layer that can be lost to the</span>
<span id="L1683">                                ! net surface salt fluxes within a timestep.</span>
<span id="L1684">PRESSURE_DEPENDENT_FRAZIL = False !   [Boolean] default = False</span>
<span id="L1685">                                ! If true, use a pressure dependent freezing temperature when making frazil. The</span>
<span id="L1686">                                ! default is false, which will be faster but is inappropriate with ice-shelf</span>
<span id="L1687">                                ! cavities.</span>
<span id="L1688">DO_BRINE_PLUME = False          !   [Boolean] default = False</span>
<span id="L1689">                                ! If true, use a brine plume parameterization from Nguyen et al., 2009.</span>
<span id="L1690">VAR_PEN_SW = False              !   [Boolean] default = False</span>
<span id="L1691">                                ! If true, use one of the CHL_A schemes specified by OPACITY_SCHEME to determine</span>
<span id="L1692">                                ! the e-folding depth of incoming short wave radiation.</span>
<span id="L1693"></span>
<span id="L1694">! === module MOM_mixed_layer ===</span>
<span id="L1695">MSTAR = 0.3                     !   [nondim] default = 1.2</span>
<span id="L1696">                                ! The ratio of the friction velocity cubed to the TKE input to the mixed layer.</span>
<span id="L1697">NSTAR = 0.15                    !   [nondim] default = 0.15</span>
<span id="L1698">                                ! The portion of the buoyant potential energy imparted by surface fluxes that is</span>
<span id="L1699">                                ! available to drive entrainment at the base of mixed layer when that energy is</span>
<span id="L1700">                                ! positive.</span>
<span id="L1701">BULK_RI_ML = 0.05               !   [nondim]</span>
<span id="L1702">                                ! The efficiency with which mean kinetic energy released by mechanically forced</span>
<span id="L1703">                                ! entrainment of the mixed layer is converted to turbulent kinetic energy.</span>
<span id="L1704">ABSORB_ALL_SW = True            !   [Boolean] default = False</span>
<span id="L1705">                                ! If true,  all shortwave radiation is absorbed by the ocean, instead of passing</span>
<span id="L1706">                                ! through to the bottom mud.</span>
<span id="L1707">TKE_DECAY = 10.0                !   [nondim] default = 2.5</span>
<span id="L1708">                                ! TKE_DECAY relates the vertical rate of decay of the TKE available for</span>
<span id="L1709">                                ! mechanical entrainment to the natural Ekman depth.</span>
<span id="L1710">NSTAR2 = 0.15                   !   [nondim] default = 0.15</span>
<span id="L1711">                                ! The portion of any potential energy released by convective adjustment that is</span>
<span id="L1712">                                ! available to drive entrainment at the base of mixed layer. By default</span>
<span id="L1713">                                ! NSTAR2=NSTAR.</span>
<span id="L1714">BULK_RI_CONVECTIVE = 0.05       !   [nondim] default = 0.05</span>
<span id="L1715">                                ! The efficiency with which convectively released mean kinetic energy is</span>
<span id="L1716">                                ! converted to turbulent kinetic energy.  By default</span>
<span id="L1717">                                ! BULK_RI_CONVECTIVE=BULK_RI_ML.</span>
<span id="L1718">HMIX_MIN = 2.0                  !   [m] default = 0.0</span>
<span id="L1719">                                ! The minimum mixed layer depth if the mixed layer depth is determined</span>
<span id="L1720">                                ! dynamically.</span>
<span id="L1721">MECH_TKE_FLOOR = 1.0E-150       !   [m3 s-2] default = 1.0E-150</span>
<span id="L1722">                                ! A tiny floor on the amount of turbulent kinetic energy that is used when the</span>
<span id="L1723">                                ! mixed layer does not yet contain HMIX_MIN fluid.  The default is so small that</span>
<span id="L1724">                                ! its actual value is irrelevant, so long as it is greater than 0.</span>
<span id="L1725">LIMIT_BUFFER_DETRAIN = True     !   [Boolean] default = False</span>
<span id="L1726">                                ! If true, limit the detrainment from the buffer layers to not be too different</span>
<span id="L1727">                                ! from the neighbors.</span>
<span id="L1728">ALLOWED_DETRAIN_TEMP_CHG = 0.5  !   [K] default = 0.5</span>
<span id="L1729">                                ! The amount by which temperature is allowed to exceed previous values during</span>
<span id="L1730">                                ! detrainment.</span>
<span id="L1731">ALLOWED_DETRAIN_SALT_CHG = 0.1  !   [ppt] default = 0.1</span>
<span id="L1732">                                ! The amount by which salinity is allowed to exceed previous values during</span>
<span id="L1733">                                ! detrainment.</span>
<span id="L1734">ML_DT_DS_WEIGHT = 6.0           !   [degC ppt-1] default = 6.0</span>
<span id="L1735">                                ! When forced to extrapolate T &amp; S to match the layer densities, this factor (in</span>
<span id="L1736">                                ! deg C / PSU) is combined with the derivatives of density with T &amp; S to</span>
<span id="L1737">                                ! determine what direction is orthogonal to density contours. It should be a</span>
<span id="L1738">                                ! typical value of (dR/dS) / (dR/dT) in oceanic profiles.</span>
<span id="L1739">BUFFER_LAYER_EXTRAP_LIMIT = -1.0 !   [nondim] default = -1.0</span>
<span id="L1740">                                ! A limit on the density range over which extrapolation can occur when</span>
<span id="L1741">                                ! detraining from the buffer layers, relative to the density range within the</span>
<span id="L1742">                                ! mixed and buffer layers, when the detrainment is going into the lightest</span>
<span id="L1743">                                ! interior layer, nondimensional, or a negative value not to apply this limit.</span>
<span id="L1744">BUFFER_LAYER_HMIN_THICK = 5.0   !   [m] default = 5.0</span>
<span id="L1745">                                ! The minimum buffer layer thickness when the mixed layer is very thick.</span>
<span id="L1746">BUFFER_LAYER_HMIN_REL = 0.05    !   [nondim] default = 0.05</span>
<span id="L1747">                                ! The minimum buffer layer thickness relative to the combined mixed land buffer</span>
<span id="L1748">                                ! ayer thicknesses when they are thin.</span>
<span id="L1749">BUFFER_LAY_DETRAIN_TIME = 1.44E+04 !   [s] default = 1.44E+04</span>
<span id="L1750">                                ! A timescale that characterizes buffer layer detrainment events.</span>
<span id="L1751">BUFFER_SPLIT_RHO_TOL = 0.1      !   [nondim] default = 0.1</span>
<span id="L1752">                                ! The fractional tolerance for matching layer target densities when splitting</span>
<span id="L1753">                                ! layers to deal with massive interior layers that are lighter than one of the</span>
<span id="L1754">                                ! mixed or buffer layers.</span>
<span id="L1755">DEPTH_LIMIT_FLUXES = 0.1        !   [m] default = 0.2</span>
<span id="L1756">                                ! The surface fluxes are scaled away when the total ocean depth is less than</span>
<span id="L1757">                                ! DEPTH_LIMIT_FLUXES.</span>
<span id="L1758">ML_RESORT = False               !   [Boolean] default = False</span>
<span id="L1759">                                ! If true, resort the topmost layers by potential density before the mixed layer</span>
<span id="L1760">                                ! calculations.</span>
<span id="L1761">BML_USTAR_MIN = 1.45842E-18     !   [m s-1] default = 1.45842E-18</span>
<span id="L1762">                                ! The minimum value of ustar that should be used by the bulk mixed layer model</span>
<span id="L1763">                                ! in setting vertical TKE decay scales. This must be greater than 0.</span>
<span id="L1764">BML_NONBOUSINESQ = False        !   [Boolean] default = False</span>
<span id="L1765">                                ! If true, use non-Boussinesq expressions for the energetic calculations used in</span>
<span id="L1766">                                ! the bulk mixed layer calculations.</span>
<span id="L1767">RESOLVE_EKMAN = False           !   [Boolean] default = False</span>
<span id="L1768">                                ! If true, the NKML&gt;1 layers in the mixed layer are chosen to optimally</span>
<span id="L1769">                                ! represent the impact of the Ekman transport on the mixed layer TKE budget.</span>
<span id="L1770">                                ! Otherwise, the sublayers are distributed uniformly through the mixed layer.</span>
<span id="L1771">CORRECT_ABSORPTION_DEPTH = True !   [Boolean] default = False</span>
<span id="L1772">                                ! If true, the average depth at which penetrating shortwave radiation is</span>
<span id="L1773">                                ! absorbed is adjusted to match the average heating depth of an exponential</span>
<span id="L1774">                                ! profile by moving some of the heating upward in the water column.</span>
<span id="L1775">DO_RIVERMIX = False             !   [Boolean] default = False</span>
<span id="L1776">                                ! If true, apply additional mixing wherever there is runoff, so that it is mixed</span>
<span id="L1777">                                ! down to RIVERMIX_DEPTH, if the ocean is that deep.</span>
<span id="L1778">USE_RIVER_HEAT_CONTENT = False  !   [Boolean] default = False</span>
<span id="L1779">                                ! If true, use the fluxes%runoff_Hflx field to set the heat carried by runoff,</span>
<span id="L1780">                                ! instead of using SST*CP*liq_runoff.</span>
<span id="L1781">USE_CALVING_HEAT_CONTENT = False !   [Boolean] default = False</span>
<span id="L1782">                                ! If true, use the fluxes%calving_Hflx field to set the heat carried by runoff,</span>
<span id="L1783">                                ! instead of using SST*CP*froz_runoff.</span>
<span id="L1784">BULKML_CONV_MOMENTUM_BUG = False !   [Boolean] default = False</span>
<span id="L1785">                                ! If true, use code with a bug that causes a loss of momentum conservation</span>
<span id="L1786">                                ! during mixedlayer convection.</span>
<span id="L1787">LIMIT_BUFFER_DET_DH_SFC = 0.5   !   [nondim] default = 0.5</span>
<span id="L1788">                                ! The fractional limit in the change between grid points of the surface region</span>
<span id="L1789">                                ! (mixed &amp; buffer layer) thickness.</span>
<span id="L1790">LIMIT_BUFFER_DET_DH_BATHY = 0.2 !   [nondim] default = 0.2</span>
<span id="L1791">                                ! The fraction of the total depth by which the thickness of the surface region</span>
<span id="L1792">                                ! (mixed &amp; buffer layer) is allowed to change between grid points.</span>
<span id="L1793"></span>
<span id="L1794">! === module MOM_regularize_layers ===</span>
<span id="L1795">REGULARIZE_SURFACE_LAYERS = False !   [Boolean] default = False</span>
<span id="L1796">                                ! If defined, vertically restructure the near-surface layers when they have too</span>
<span id="L1797">                                ! much lateral variations to allow for sensible lateral barotropic transports.</span>
<span id="L1798"></span>
<span id="L1799">! === module MOM_opacity ===</span>
<span id="L1800">EXP_OPACITY_SCHEME = &quot;SINGLE_EXP&quot; ! default = &quot;SINGLE_EXP&quot;</span>
<span id="L1801">                                ! This character string specifies which exponential opacity scheme to utilize.</span>
<span id="L1802">                                ! Currently valid options include:</span>
<span id="L1803">                                !        SINGLE_EXP - Single Exponent decay.</span>
<span id="L1804">                                !        DOUBLE_EXP - Double Exponent decay.</span>
<span id="L1805">PEN_SW_SCALE = 15.0             !   [m] default = 0.0</span>
<span id="L1806">                                ! The vertical absorption e-folding depth of the penetrating shortwave</span>
<span id="L1807">                                ! radiation.</span>
<span id="L1808">PEN_SW_FRAC = 0.42              !   [nondim] default = 0.0</span>
<span id="L1809">                                ! The fraction of the shortwave radiation that penetrates below the surface.</span>
<span id="L1810">PEN_SW_NBANDS = 1               ! default = 1</span>
<span id="L1811">                                ! The number of bands of penetrating shortwave radiation.</span>
<span id="L1812">OPTICS_ANSWER_DATE = 99991231   ! default = 99991231</span>
<span id="L1813">                                ! The vintage of the order of arithmetic and expressions in the optics</span>
<span id="L1814">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L1815">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L1816">PEN_SW_FLUX_ABSORB = 2.5E-11    !   [degC m s-1] default = 2.5E-11</span>
<span id="L1817">                                ! A minimum remaining shortwave heating rate that will be simply absorbed in the</span>
<span id="L1818">                                ! next sufficiently thick layers for computational efficiency, instead of</span>
<span id="L1819">                                ! continuing to penetrate.  The default, 2.5e-11 degC m s-1, is about 1e-4 W m-2</span>
<span id="L1820">                                ! or 0.08 degC m century-1, but 0 is also a valid value.</span>
<span id="L1821">PEN_SW_ABSORB_MINTHICK = 1.0    !   [m] default = 1.0</span>
<span id="L1822">                                ! A thickness that is used to absorb the remaining penetrating shortwave heat</span>
<span id="L1823">                                ! flux when it drops below PEN_SW_FLUX_ABSORB.</span>
<span id="L1824">OPACITY_LAND_VALUE = 10.0       !   [m-1] default = 10.0</span>
<span id="L1825">                                ! The value to use for opacity over land. The default is 10 m-1 - a value for</span>
<span id="L1826">                                ! muddy water.</span>
<span id="L1827"></span>
<span id="L1828">! === module MOM_tracer_advect ===</span>
<span id="L1829">TRACER_ADVECTION_SCHEME = &quot;PLM&quot; ! default = &quot;PLM&quot;</span>
<span id="L1830">                                ! The horizontal transport scheme for tracers:</span>
<span id="L1831">                                !   PLM    - Piecewise Linear Method</span>
<span id="L1832">                                !   PPM:H3 - Piecewise Parabolic Method (Huyhn 3rd order)</span>
<span id="L1833">                                !   PPM    - Piecewise Parabolic Method (Colella-Woodward)</span>
<span id="L1834"></span>
<span id="L1835">! === module MOM_tracer_hor_diff ===</span>
<span id="L1836">KHTR = 1.0                      !   [m2 s-1] default = 0.0</span>
<span id="L1837">                                ! The background along-isopycnal tracer diffusivity.</span>
<span id="L1838">KHTR_MIN = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L1839">                                ! The minimum along-isopycnal tracer diffusivity.</span>
<span id="L1840">KHTR_MAX = 900.0                !   [m2 s-1] default = 0.0</span>
<span id="L1841">                                ! The maximum along-isopycnal tracer diffusivity. Set to a positive value to</span>
<span id="L1842">                                ! activate.</span>
<span id="L1843">KHTR_PASSIVITY_COEFF = 0.0      !   [nondim] default = 0.0</span>
<span id="L1844">                                ! The coefficient that scales deformation radius over grid-spacing in passivity,</span>
<span id="L1845">                                ! where passivity is the ratio between along isopycnal mixing of tracers to</span>
<span id="L1846">                                ! thickness mixing. A non-zero value enables this parameterization.</span>
<span id="L1847">KHTR_PASSIVITY_MIN = 0.5        !   [nondim] default = 0.5</span>
<span id="L1848">                                ! The minimum passivity which is the ratio between along isopycnal mixing of</span>
<span id="L1849">                                ! tracers to thickness mixing.</span>
<span id="L1850">DIFFUSE_ML_TO_INTERIOR = True   !   [Boolean] default = False</span>
<span id="L1851">                                ! If true, enable epipycnal mixing between the surface boundary layer and the</span>
<span id="L1852">                                ! interior.</span>
<span id="L1853">CHECK_DIFFUSIVE_CFL = False     !   [Boolean] default = False</span>
<span id="L1854">                                ! If true, use enough iterations the diffusion to ensure that the diffusive</span>
<span id="L1855">                                ! equivalent of the CFL limit is not violated.  If false, always use the greater</span>
<span id="L1856">                                ! of 1 or MAX_TR_DIFFUSION_CFL iteration.</span>
<span id="L1857">MAX_TR_DIFFUSION_CFL = -1.0     !   [nondim] default = -1.0</span>
<span id="L1858">                                ! If positive, locally limit the along-isopycnal tracer diffusivity to keep the</span>
<span id="L1859">                                ! diffusive CFL locally at or below this value.  The number of diffusive</span>
<span id="L1860">                                ! iterations is often this value or the next greater integer.</span>
<span id="L1861">RECALC_NEUTRAL_SURF = False     !   [Boolean] default = False</span>
<span id="L1862">                                ! If true, then recalculate the neutral surfaces if the</span>
<span id="L1863">                                ! diffusive CFL is exceeded. If false, assume that the</span>
<span id="L1864">                                ! positions of the surfaces do not change</span>
<span id="L1865">HOR_DIFF_ANSWER_DATE = 20240101 ! default = 99991231</span>
<span id="L1866">                                ! The vintage of the order of arithmetic to use for the tracer diffusion.</span>
<span id="L1867">                                ! Values of 20240330 or below recover the answers from the original form of the</span>
<span id="L1868">                                ! along-isopycnal mixed layer to interior mixing code, while higher values use</span>
<span id="L1869">                                ! mathematically equivalent expressions that recover rotational symmetry when</span>
<span id="L1870">                                ! DIFFUSE_ML_TO_INTERIOR is true.</span>
<span id="L1871">HOR_DIFF_LIMIT_BUG = True       !   [Boolean] default = False</span>
<span id="L1872">                                ! If true and the answer date is 20240330 or below, use a rotational symmetry</span>
<span id="L1873">                                ! breaking bug when limiting the tracer properties in tracer_epipycnal_ML_diff.</span>
<span id="L1874">ML_KHTR_SCALE = 0.0             !   [nondim] default = 1.0</span>
<span id="L1875">                                ! With Diffuse_ML_interior, the ratio of the truly horizontal diffusivity in the</span>
<span id="L1876">                                ! mixed layer to the epipycnal diffusivity.  The valid range is 0 to 1.</span>
<span id="L1877"></span>
<span id="L1878">! === module MOM_neutral_diffusion ===</span>
<span id="L1879">! This module implements neutral diffusion of tracers</span>
<span id="L1880">USE_NEUTRAL_DIFFUSION = False   !   [Boolean] default = False</span>
<span id="L1881">                                ! If true, enables the neutral diffusion module.</span>
<span id="L1882"></span>
<span id="L1883">! === module MOM_hor_bnd_diffusion ===</span>
<span id="L1884">! This module implements horizontal diffusion of tracers near boundaries</span>
<span id="L1885">USE_HORIZONTAL_BOUNDARY_DIFFUSION = False !   [Boolean] default = False</span>
<span id="L1886">                                ! If true, enables the horizonal boundary tracer&#x27;s diffusion module.</span>
<span id="L1887">OBSOLETE_DIAGNOSTIC_IS_FATAL = True !   [Boolean] default = True</span>
<span id="L1888">                                ! If an obsolete diagnostic variable appears in the diag_table, cause a FATAL</span>
<span id="L1889">                                ! error rather than issue a WARNING.</span>
<span id="L1890"></span>
<span id="L1891">! === module MOM_sum_output ===</span>
<span id="L1892">CALCULATE_APE = True            !   [Boolean] default = True</span>
<span id="L1893">                                ! If true, calculate the available potential energy of the interfaces.  Setting</span>
<span id="L1894">                                ! this to false reduces the memory footprint of high-PE-count models</span>
<span id="L1895">                                ! dramatically.</span>
<span id="L1896">WRITE_STOCKS = True             !   [Boolean] default = True</span>
<span id="L1897">                                ! If true, write the integrated tracer amounts to stdout when the energy files</span>
<span id="L1898">                                ! are written.</span>
<span id="L1899">MAXTRUNC = 5000                 !   [truncations save_interval-1] default = 0</span>
<span id="L1900">                                ! The run will be stopped, and the day set to a very large value if the velocity</span>
<span id="L1901">                                ! is truncated more than MAXTRUNC times between energy saves.  Set MAXTRUNC to 0</span>
<span id="L1902">                                ! to stop if there is any truncation of velocities.</span>
<span id="L1903">MAX_ENERGY = 0.0                !   [m2 s-2] default = 0.0</span>
<span id="L1904">                                ! The maximum permitted average energy per unit mass; the model will be stopped</span>
<span id="L1905">                                ! if there is more energy than this.  If zero or negative, this is set to</span>
<span id="L1906">                                ! 10*MAXVEL^2.</span>
<span id="L1907">MAXVEL = 10.0                   !   [m s-1] default = 3.0E+08</span>
<span id="L1908">                                ! The maximum velocity allowed before the velocity components are truncated.</span>
<span id="L1909">ENERGYFILE = &quot;ocean.stats&quot;      ! default = &quot;ocean.stats&quot;</span>
<span id="L1910">                                ! The file to use to write the energies and globally summed diagnostics.</span>
<span id="L1911">DATE_STAMPED_STDOUT = True      !   [Boolean] default = True</span>
<span id="L1912">                                ! If true, use dates (not times) in messages to stdout</span>
<span id="L1913">ISO_DATE_STAMPED_STDOUT = False !   [Boolean] default = False</span>
<span id="L1914">                                ! If true, use ISO formatted dates in messages to stdout</span>
<span id="L1915">TIMEUNIT = 8.64E+04             !   [s] default = 8.64E+04</span>
<span id="L1916">                                ! The time unit in seconds a number of input fields</span>
<span id="L1917">READ_DEPTH_LIST = False         !   [Boolean] default = False</span>
<span id="L1918">                                ! Read the depth list from a file if it exists or create that file otherwise.</span>
<span id="L1919">DEPTH_LIST_MIN_INC = 1.0E-10    !   [m] default = 1.0E-10</span>
<span id="L1920">                                ! The minimum increment between the depths of the entries in the depth-list</span>
<span id="L1921">                                ! file.</span>
<span id="L1922">ENERGYSAVEDAYS = 0.25           !   [days] default = 1.0</span>
<span id="L1923">                                ! The interval in units of TIMEUNIT between saves of the energies of the run and</span>
<span id="L1924">                                ! other globally summed diagnostics.</span>
<span id="L1925">ENERGYSAVEDAYS_GEOMETRIC = 0.0  !   [days] default = 0.0</span>
<span id="L1926">                                ! The starting interval in units of TIMEUNIT for the first call to save the</span>
<span id="L1927">                                ! energies of the run and other globally summed diagnostics. The interval</span>
<span id="L1928">                                ! increases by a factor of 2. after each call to write_energy.</span>
<span id="L1929"></span>
<span id="L1930">! === module ocean_stochastics_init ===</span>
<span id="L1931">DO_SPPT = False                 !   [Boolean] default = False</span>
<span id="L1932">                                ! If true, then stochastically perturb the thermodynamic tendencies of T,S, amd</span>
<span id="L1933">                                ! h.  Amplitude and correlations are controlled by the nam_stoch namelist in the</span>
<span id="L1934">                                ! UFS model only.</span>
<span id="L1935">DO_SKEB = False                 !   [Boolean] default = False</span>
<span id="L1936">                                ! If true, then stochastically perturb the currents using the stochastic kinetic</span>
<span id="L1937">                                ! energy backscatter scheme.</span>
<span id="L1938">PERT_EPBL = False               !   [Boolean] default = False</span>
<span id="L1939">                                ! If true, then stochastically perturb the kinetic energy production and</span>
<span id="L1940">                                ! dissipation terms.  Amplitude and correlations are controlled by the nam_stoch</span>
<span id="L1941">                                ! namelist in the UFS model only.</span>
<span id="L1942"></span>
<span id="L1943">! === module MOM_surface_forcing ===</span>
<span id="L1944">VARIABLE_WINDS = True           !   [Boolean] default = True</span>
<span id="L1945">                                ! If true, the winds vary in time after the initialization.</span>
<span id="L1946">VARIABLE_BUOYFORCE = True       !   [Boolean] default = True</span>
<span id="L1947">                                ! If true, the buoyancy forcing varies in time after the initialization of the</span>
<span id="L1948">                                ! model.</span>
<span id="L1949">BUOY_CONFIG = &quot;linear&quot;          ! default = &quot;zero&quot;</span>
<span id="L1950">                                ! The character string that indicates how buoyancy forcing is specified.  Valid</span>
<span id="L1951">                                ! options include (file), (data_override), (zero), (const), (linear), (MESO),</span>
<span id="L1952">                                ! (SCM_CVmix_tests), (BFB), (dumbbell), (USER) and (NONE).</span>
<span id="L1953">WIND_CONFIG = &quot;gyres&quot;           ! default = &quot;zero&quot;</span>
<span id="L1954">                                ! The character string that indicates how wind forcing is specified.  Valid</span>
<span id="L1955">                                ! options include (file), (data_override), (2gyre), (1gyre), (gyres), (zero),</span>
<span id="L1956">                                ! (const), (Neverworld), (scurves), (ideal_hurr), (SCM_CVmix_tests) and (USER).</span>
<span id="L1957">TAUX_CONST = 0.0                !   [Pa] default = 0.0</span>
<span id="L1958">                                ! With the gyres wind_config, the constant offset in the zonal wind stress</span>
<span id="L1959">                                ! profile:   A in taux = A + B*sin(n*pi*y/L) + C*cos(n*pi*y/L).</span>
<span id="L1960">TAUX_SIN_AMP = 0.1              !   [Pa] default = 0.0</span>
<span id="L1961">                                ! With the gyres wind_config, the sine amplitude in the zonal wind stress</span>
<span id="L1962">                                ! profile:   B in taux = A + B*sin(n*pi*y/L) + C*cos(n*pi*y/L).</span>
<span id="L1963">TAUX_COS_AMP = 0.0              !   [Pa] default = 0.0</span>
<span id="L1964">                                ! With the gyres wind_config, the cosine amplitude in the zonal wind stress</span>
<span id="L1965">                                ! profile:   C in taux = A + B*sin(n*pi*y/L) + C*cos(n*pi*y/L).</span>
<span id="L1966">TAUX_N_PIS = 1.0                !   [nondim] default = 0.0</span>
<span id="L1967">                                ! With the gyres wind_config, the number of gyres in the zonal wind stress</span>
<span id="L1968">                                ! profile:   n in taux = A + B*sin(n*pi*y/L) + C*cos(n*pi*y/L).</span>
<span id="L1969">WIND_GYRES_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1970">                                ! The vintage of the expressions used to set gyre wind stresses. Values below</span>
<span id="L1971">                                ! 20190101 recover the answers from the end of 2018, while higher values use a</span>
<span id="L1972">                                ! form of the gyre wind stresses that are rotationally invariant and more likely</span>
<span id="L1973">                                ! to be the same between compilers.</span>
<span id="L1974">RESTOREBUOY = True              !   [Boolean] default = False</span>
<span id="L1975">                                ! If true, the buoyancy fluxes drive the model back toward some specified</span>
<span id="L1976">                                ! surface state with a rate given by FLUXCONST.</span>
<span id="L1977">LATENT_HEAT_FUSION = 3.34E+05   !   [J/kg] default = 3.34E+05</span>
<span id="L1978">                                ! The latent heat of fusion.</span>
<span id="L1979">LATENT_HEAT_VAPORIZATION = 2.5E+06 !   [J/kg] default = 2.5E+06</span>
<span id="L1980">                                ! The latent heat of fusion.</span>
<span id="L1981">FLUXCONST = 0.5                 !   [m day-1] default = 0.0</span>
<span id="L1982">                                ! The constant that relates the restoring surface fluxes to the relative surface</span>
<span id="L1983">                                ! anomalies (akin to a piston velocity).  Note the non-MKS units.</span>
<span id="L1984">FLUXCONST_T = 0.5               !   [m day-1] default = 0.5</span>
<span id="L1985">                                ! The constant that relates the restoring surface temperature flux to the</span>
<span id="L1986">                                ! relative surface anomaly (akin to a piston velocity).  Note the non-MKS units.</span>
<span id="L1987">FLUXCONST_S = 0.5               !   [m day-1] default = 0.5</span>
<span id="L1988">                                ! The constant that relates the restoring surface salinity flux to the relative</span>
<span id="L1989">                                ! surface anomaly (akin to a piston velocity).  Note the non-MKS units.</span>
<span id="L1990">SST_NORTH = 27.0                !   [degC] default = 0.0</span>
<span id="L1991">                                ! With buoy_config linear, the sea surface temperature at the northern end of</span>
<span id="L1992">                                ! the domain toward which to to restore.</span>
<span id="L1993">SST_SOUTH = 3.0                 !   [degC] default = 0.0</span>
<span id="L1994">                                ! With buoy_config linear, the sea surface temperature at the southern end of</span>
<span id="L1995">                                ! the domain toward which to to restore.</span>
<span id="L1996">SSS_NORTH = 35.0                !   [ppt] default = 35.0</span>
<span id="L1997">                                ! With buoy_config linear, the sea surface salinity at the northern end of the</span>
<span id="L1998">                                ! domain toward which to to restore.</span>
<span id="L1999">SSS_SOUTH = 35.0                !   [ppt] default = 35.0</span>
<span id="L2000">                                ! With buoy_config linear, the sea surface salinity at the southern end of the</span>
<span id="L2001">                                ! domain toward which to to restore.</span>
<span id="L2002">RESTORE_FLUX_RHO = 1035.0       !   [kg m-3] default = 1035.0</span>
<span id="L2003">                                ! The density that is used to convert piston velocities into salt or heat fluxes</span>
<span id="L2004">                                ! with RESTORE_SALINITY or RESTORE_TEMPERATURE.</span>
<span id="L2005">GUST_CONST = 0.02               !   [Pa] default = 0.0</span>
<span id="L2006">                                ! The background gustiness in the winds.</span>
<span id="L2007">USTAR_GUSTLESS_BUG = False      !   [Boolean] default = False</span>
<span id="L2008">                                ! If true include a bug in the time-averaging of the gustless wind friction</span>
<span id="L2009">                                ! velocity</span>
<span id="L2010">READ_GUST_2D = False            !   [Boolean] default = False</span>
<span id="L2011">                                ! If true, use a 2-dimensional gustiness supplied from an input file</span>
<span id="L2012"></span>
<span id="L2013">! === module MOM_restart ===</span>
<span id="L2014">USE_WAVES = False               !   [Boolean] default = False</span>
<span id="L2015">                                ! If true, enables surface wave modules.</span>
<span id="L2016"></span>
<span id="L2017">! === module MOM_main (MOM_driver) ===</span>
<span id="L2018">DT_FORCING = 3600.0             !   [s] default = 900.0</span>
<span id="L2019">                                ! The time step for changing forcing, coupling with other components, or</span>
<span id="L2020">                                ! potentially writing certain diagnostics. The default value is given by DT.</span>
<span id="L2021">DAYMAX = 1.0                    !   [days]</span>
<span id="L2022">                                ! The final time of the whole simulation, in units of TIMEUNIT seconds.  This</span>
<span id="L2023">                                ! also sets the potential end time of the present run segment if the end time is</span>
<span id="L2024">                                ! not set via ocean_solo_nml in input.nml.</span>
<span id="L2025">SINGLE_STEPPING_CALL = True     !   [Boolean] default = True</span>
<span id="L2026">                                ! If true, advance the state of MOM with a single step including both dynamics</span>
<span id="L2027">                                ! and thermodynamics.  If false the two phases are advanced with separate calls.</span>
<span id="L2028">RESTART_CONTROL = 3             ! default = 1</span>
<span id="L2029">                                ! An integer whose bits encode which restart files are written. Add 2 (bit 1)</span>
<span id="L2030">                                ! for a time-stamped file, and odd (bit 0) for a non-time-stamped file. A</span>
<span id="L2031">                                ! non-time-stamped restart file is saved at the end of the run segment for any</span>
<span id="L2032">                                ! non-negative value.</span>
<span id="L2033">RESTINT = 365.0                 !   [days] default = 0.0</span>
<span id="L2034">                                ! The interval between saves of the restart file in units of TIMEUNIT.  Use 0</span>
<span id="L2035">                                ! (the default) to not save incremental restart files at all.</span>
<span id="L2036">WRITE_CPU_STEPS = 1000          ! default = 1000</span>
<span id="L2037">                                ! The number of coupled timesteps between writing the cpu time. If this is not</span>
<span id="L2038">                                ! positive, do not check cpu time, and the segment run-length can not be set via</span>
<span id="L2039">                                ! an elapsed CPU time.</span>
<span id="L2040"></span>
<span id="L2041">! === module MOM_write_cputime ===</span>
<span id="L2042">MAXCPU = 2.88E+04               !   [wall-clock seconds] default = -1.0</span>
<span id="L2043">                                ! The maximum amount of cpu time per processor for which MOM should run before</span>
<span id="L2044">                                ! saving a restart file and quitting with a return value that indicates that a</span>
<span id="L2045">                                ! further run is required to complete the simulation. If automatic restarts are</span>
<span id="L2046">                                ! not desired, use a negative value for MAXCPU.  MAXCPU has units of wall-clock</span>
<span id="L2047">                                ! seconds, so the actual CPU time used is larger by a factor of the number of</span>
<span id="L2048">                                ! processors used.</span>
<span id="L2049">CPU_TIME_FILE = &quot;CPU_stats&quot;     ! default = &quot;CPU_stats&quot;</span>
<span id="L2050">                                ! The file into which CPU time is written.</span>
<span id="L2051"></span>
<span id="L2052">! === module MOM_file_parser ===</span>
<span id="L2053">SEND_LOG_TO_STDOUT = False      !   [Boolean] default = False</span>
<span id="L2054">                                ! If true, all log messages are also sent to stdout.</span>
<span id="L2055">DOCUMENT_FILE = &quot;MOM_parameter_doc&quot; ! default = &quot;MOM_parameter_doc&quot;</span>
<span id="L2056">                                ! The basename for files where run-time parameters, their settings, units and</span>
<span id="L2057">                                ! defaults are documented. Blank will disable all parameter documentation.</span>
<span id="L2058">COMPLETE_DOCUMENTATION = True   !   [Boolean] default = True</span>
<span id="L2059">                                ! If true, all run-time parameters are documented in MOM_parameter_doc.all .</span>
<span id="L2060">MINIMAL_DOCUMENTATION = True    !   [Boolean] default = True</span>
<span id="L2061">                                ! If true, non-default run-time parameters are documented in</span>
<span id="L2062">                                ! MOM_parameter_doc.short .</span>
</pre>
