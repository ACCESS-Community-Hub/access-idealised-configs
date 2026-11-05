---
search:
  exclude: true
---

# CVmix_SCM_tests-skin_warming_wind-KPP: MOM_parameter_doc.all

Every MOM6 parameter of the tested run of [CVmix_SCM_tests-skin_warming_wind-KPP](../mom6examples/CVmix_SCM_tests-skin_warming_wind-KPP.md), as MOM6 wrote it to `MOM_parameter_doc.all` in the run's output folder. Line numbers match the file.

<pre class="paramdoc"><span id="L1">! This file was written by the model and records all non-layout or debugging parameters used at run-time.</span>
<span id="L2"></span>
<span id="L3">! === module MOM ===</span>
<span id="L4">SPLIT = False                   !   [Boolean] default = True</span>
<span id="L5">                                ! Use the split time stepping if true.</span>
<span id="L6">USE_RK2 = False                 !   [Boolean] default = False</span>
<span id="L7">                                ! If true, use RK2 instead of RK3 in the unsplit time stepping.</span>
<span id="L8">CALC_RHO_FOR_SEA_LEVEL = False  !   [Boolean] default = False</span>
<span id="L9">                                ! If true, the in-situ density is used to calculate the effective sea level that</span>
<span id="L10">                                ! is returned to the coupler. If false, the Boussinesq parameter RHO_0 is used.</span>
<span id="L11">ENABLE_THERMODYNAMICS = True    !   [Boolean] default = True</span>
<span id="L12">                                ! If true, Temperature and salinity are used as state variables.</span>
<span id="L13">USE_EOS = True                  !   [Boolean] default = True</span>
<span id="L14">                                ! If true,  density is calculated from temperature and salinity with an equation</span>
<span id="L15">                                ! of state.  If USE_EOS is true, ENABLE_THERMODYNAMICS must be true as well.</span>
<span id="L16">DIABATIC_FIRST = False          !   [Boolean] default = False</span>
<span id="L17">                                ! If true, apply diabatic and thermodynamic processes, including buoyancy</span>
<span id="L18">                                ! forcing and mass gain or loss, before stepping the dynamics forward.</span>
<span id="L19">USE_CONTEMP_ABSSAL = False      !   [Boolean] default = False</span>
<span id="L20">                                ! If true, the prognostics T&amp;S are the conservative temperature and absolute</span>
<span id="L21">                                ! salinity. Care should be taken to convert them to potential temperature and</span>
<span id="L22">                                ! practical salinity before exchanging them with the coupler and/or reporting</span>
<span id="L23">                                ! T&amp;S diagnostics.</span>
<span id="L24">ADIABATIC = False               !   [Boolean] default = False</span>
<span id="L25">                                ! There are no diapycnal mass fluxes if ADIABATIC is true.  This assumes that KD</span>
<span id="L26">                                ! = 0.0 and that there is no buoyancy forcing, but makes the model faster by</span>
<span id="L27">                                ! eliminating subroutine calls.</span>
<span id="L28">DO_DYNAMICS = True              !   [Boolean] default = True</span>
<span id="L29">                                ! If False, skips the dynamics calls that update u &amp; v, as well as the gravity</span>
<span id="L30">                                ! wave adjustment to h. This may be a fragile feature, but can be useful during</span>
<span id="L31">                                ! development</span>
<span id="L32">OFFLINE_TRACER_MODE = False     !   [Boolean] default = False</span>
<span id="L33">                                ! If true, barotropic and baroclinic dynamics, thermodynamics are all bypassed</span>
<span id="L34">                                ! with all the fields necessary to integrate the tracer advection and diffusion</span>
<span id="L35">                                ! equation are read in from files stored from a previous integration of the</span>
<span id="L36">                                ! prognostic model. NOTE: This option only used in the ocean_solo_driver.</span>
<span id="L37">USE_REGRIDDING = True           !   [Boolean] default = False</span>
<span id="L38">                                ! If True, use the ALE algorithm (regridding/remapping). If False, use the</span>
<span id="L39">                                ! layered isopycnal algorithm.</span>
<span id="L40">REMAP_UV_USING_OLD_ALG = False  !   [Boolean] default = False</span>
<span id="L41">                                ! If true, uses the old remapping-via-a-delta-z method for remapping u and v. If</span>
<span id="L42">                                ! false, uses the new method that remaps between grids described by an old and</span>
<span id="L43">                                ! new thickness.</span>
<span id="L44">REMAP_AUXILIARY_VARS = False    !   [Boolean] default = False</span>
<span id="L45">                                ! If true, apply ALE remapping to all of the auxiliary 3-dimensional variables</span>
<span id="L46">                                ! that are needed to reproduce across restarts, similarly to what is already</span>
<span id="L47">                                ! being done with the primary state variables.  The default should be changed to</span>
<span id="L48">                                ! true.</span>
<span id="L49">BULKMIXEDLAYER = False          !   [Boolean] default = False</span>
<span id="L50">                                ! If true, use a Kraus-Turner-like bulk mixed layer with transitional buffer</span>
<span id="L51">                                ! layers.  Layers 1 through NKML+NKBL have variable densities. There must be at</span>
<span id="L52">                                ! least NKML+NKBL+1 layers if BULKMIXEDLAYER is true. BULKMIXEDLAYER can not be</span>
<span id="L53">                                ! used with USE_REGRIDDING. The default is influenced by ENABLE_THERMODYNAMICS.</span>
<span id="L54">USE_POROUS_BARRIER = False      !   [Boolean] default = False</span>
<span id="L55">                                ! If true, use porous barrier to constrain the widths and face areas at the</span>
<span id="L56">                                ! edges of the grid cells.</span>
<span id="L57">BATHYMETRY_AT_VEL = False       !   [Boolean] default = False</span>
<span id="L58">                                ! If true, there are separate values for the basin depths at velocity points.</span>
<span id="L59">                                ! Otherwise the effects of topography are entirely determined from thickness</span>
<span id="L60">                                ! points.</span>
<span id="L61">ENABLE_BUGS_BY_DEFAULT = True   !   [Boolean] default = True</span>
<span id="L62">                                ! If true, the defaults for certain recently added bug-fix flags are set to</span>
<span id="L63">                                ! recreate the bugs so that the code can be moved forward without changing</span>
<span id="L64">                                ! answers for existing configurations.  The defaults for groups of bug-fix flags</span>
<span id="L65">                                ! are periodcially changed to correct the bugs, at which point this parameter</span>
<span id="L66">                                ! will no longer be used to set their default.  Setting this to false means that</span>
<span id="L67">                                ! bugs are only used if they are actively selected, but it also means that</span>
<span id="L68">                                ! answers may change when code is updated due to newly found bugs.</span>
<span id="L69">DT = 1200.0                     !   [s]</span>
<span id="L70">                                ! The (baroclinic) dynamics time step.  The time-step that is actually used will</span>
<span id="L71">                                ! be an integer fraction of the forcing time-step (DT_FORCING in ocean-only mode</span>
<span id="L72">                                ! or the coupling timestep in coupled mode.)</span>
<span id="L73">DT_THERM = 1200.0               !   [s] default = 1200.0</span>
<span id="L74">                                ! The thermodynamic time step. Ideally DT_THERM should be an integer multiple of</span>
<span id="L75">                                ! DT and of DT_TRACER_ADVECT and less than the forcing or coupling time-step.</span>
<span id="L76">                                ! However, if THERMO_SPANS_COUPLING is true, DT_THERM can be an integer multiple</span>
<span id="L77">                                ! of the coupling timestep. By default DT_THERM is set to DT.</span>
<span id="L78">THERMO_SPANS_COUPLING = False   !   [Boolean] default = False</span>
<span id="L79">                                ! If true, the MOM will take thermodynamic timesteps that can be longer than the</span>
<span id="L80">                                ! coupling timestep. The actual thermodynamic timestep that is used in this case</span>
<span id="L81">                                ! is the largest integer multiple of the coupling timestep that is less than or</span>
<span id="L82">                                ! equal to DT_THERM.</span>
<span id="L83">DT_TRACER_ADVECT = 1200.0       !   [s] default = 1200.0</span>
<span id="L84">                                ! The tracer advection time step. Ideally DT_TRACER_ADVECT should be an integer</span>
<span id="L85">                                ! multiple of DT, less than DT_THERM, and less than the forcing or coupling</span>
<span id="L86">                                ! time-step. However, if TRADV_SPANS_COUPLING is true, DT_TRACER_ADVECT can be</span>
<span id="L87">                                ! longer than the coupling timestep. By default DT_TRACER_ADVECT is set to</span>
<span id="L88">                                ! DT_THERM.</span>
<span id="L89">TRADV_SPANS_COUPLING = False    !   [Boolean] default = False</span>
<span id="L90">                                ! If true, the MOM will take tracer advection timesteps that can be longer than</span>
<span id="L91">                                ! the coupling timestep. The actual tracer advection timestep that is used in</span>
<span id="L92">                                ! this case is the largest integer multiple of the coupling timestep that is</span>
<span id="L93">                                ! less than or equal to DT_TRACER_ADVECT.</span>
<span id="L94">THICKNESSDIFFUSE = False        !   [Boolean] default = False</span>
<span id="L95">                                ! If true, isopycnal surfaces are diffused with a Laplacian coefficient of KHTH.</span>
<span id="L96">APPLY_INTERFACE_FILTER = False  !   [Boolean] default = False</span>
<span id="L97">                                ! If true, model interface heights are subjected to a grid-scale dependent</span>
<span id="L98">                                ! spatial smoothing, often with biharmonic filter.</span>
<span id="L99">HMIX_SFC_PROP = 1.0             !   [m] default = 1.0</span>
<span id="L100">                                ! If BULKMIXEDLAYER is false, HMIX_SFC_PROP is the depth over which to average</span>
<span id="L101">                                ! to find surface properties like SST and SSS or density (but not surface</span>
<span id="L102">                                ! velocities).</span>
<span id="L103">HMIX_UV_SFC_PROP = 0.0          !   [m] default = 0.0</span>
<span id="L104">                                ! If BULKMIXEDLAYER is false, HMIX_UV_SFC_PROP is the depth over which to</span>
<span id="L105">                                ! average to find surface flow properties, SSU, SSV. A non-positive value</span>
<span id="L106">                                ! indicates no averaging.</span>
<span id="L107">HFREEZE = -1.0                  !   [m] default = -1.0</span>
<span id="L108">                                ! If HFREEZE &gt; 0, melt potential will be computed. The actual depth over which</span>
<span id="L109">                                ! melt potential is computed will be min(HFREEZE, OBLD), where OBLD is the</span>
<span id="L110">                                ! boundary layer depth. If HFREEZE &lt;= 0 (default), melt potential will not be</span>
<span id="L111">                                ! computed.</span>
<span id="L112">INTERPOLATE_P_SURF = False      !   [Boolean] default = False</span>
<span id="L113">                                ! If true, linearly interpolate the surface pressure over the coupling time</span>
<span id="L114">                                ! step, using the specified value at the end of the step.</span>
<span id="L115">FRAZIL = False                  !   [Boolean] default = False</span>
<span id="L116">                                ! If true, water freezes if it gets too cold, and the accumulated heat deficit</span>
<span id="L117">                                ! is returned in the surface state.  FRAZIL is only used if</span>
<span id="L118">                                ! ENABLE_THERMODYNAMICS is true.</span>
<span id="L119">DO_GEOTHERMAL = False           !   [Boolean] default = False</span>
<span id="L120">                                ! If true, apply geothermal heating.</span>
<span id="L121">BOUND_SALINITY = False          !   [Boolean] default = False</span>
<span id="L122">                                ! If true, limit salinity to being positive. (The sea-ice model may ask for more</span>
<span id="L123">                                ! salt than is available and drive the salinity negative otherwise.)</span>
<span id="L124">SALINITY_UNDERFLOW = 0.0        !   [PPT] default = 0.0</span>
<span id="L125">                                ! A tiny value of salinity below which the it is set to 0.  For reference, one</span>
<span id="L126">                                ! molecule of salt per square meter of ocean is of order 1e-29 ppt.</span>
<span id="L127">TEMPERATURE_UNDERFLOW = 0.0     !   [degC] default = 0.0</span>
<span id="L128">                                ! A tiny magnitude of temperatures below which they are set to 0.</span>
<span id="L129">C_P = 3992.10322329649          !   [J kg-1 K-1] default = 3991.86795711963</span>
<span id="L130">                                ! The heat capacity of sea water, approximated as a constant. This is only used</span>
<span id="L131">                                ! if ENABLE_THERMODYNAMICS is true. The default value is from the TEOS-10</span>
<span id="L132">                                ! definition of conservative temperature.</span>
<span id="L133">USE_PSURF_IN_EOS = True         !   [Boolean] default = True</span>
<span id="L134">                                ! If true, always include the surface pressure contributions in equation of</span>
<span id="L135">                                ! state calculations.</span>
<span id="L136">P_REF = 2.0E+07                 !   [Pa] default = 2.0E+07</span>
<span id="L137">                                ! The pressure that is used for calculating the coordinate density.  (1 Pa = 1e4</span>
<span id="L138">                                ! dbar, so 2e7 is commonly used.) This is only used if USE_EOS and</span>
<span id="L139">                                ! ENABLE_THERMODYNAMICS are true.</span>
<span id="L140">NONBLOCKING_P_SURF_BUG = True   !   [Boolean] default = True</span>
<span id="L141">                                ! If true, recover a bug in which the non-blocking halo update of the surface</span>
<span id="L142">                                ! pressure is not completed before the halo points of forces%p_surf are copied</span>
<span id="L143">                                ! into tv%p_surf, so that those halo points hold the surface pressure from the</span>
<span id="L144">                                ! previous coupling step, or zeros on the first step after a restart.  This is</span>
<span id="L145">                                ! only used if NONBLOCKING_UPDATES and USE_PSURF_IN_EOS are true</span>
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
<span id="L165">IC_OUTPUT_FILE = &quot;MOM_IC&quot;       ! default = &quot;MOM_IC&quot;</span>
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
<span id="L193">REENTRANT_Y = True              !   [Boolean] default = False</span>
<span id="L194">                                ! If true, the domain is meridionally reentrant.</span>
<span id="L195">TRIPOLAR_N = False              !   [Boolean] default = False</span>
<span id="L196">                                ! Use tripolar connectivity at the northern edge of the domain.  With</span>
<span id="L197">                                ! TRIPOLAR_N, NIGLOBAL must be even.</span>
<span id="L198">NIGLOBAL = 2                    !</span>
<span id="L199">                                ! The total number of thickness grid points in the x-direction in the physical</span>
<span id="L200">                                ! domain. With STATIC_MEMORY_ this is set in MOM_memory.h at compile time.</span>
<span id="L201">NJGLOBAL = 2                    !</span>
<span id="L202">                                ! The total number of thickness grid points in the y-direction in the physical</span>
<span id="L203">                                ! domain. With STATIC_MEMORY_ this is set in MOM_memory.h at compile time.</span>
<span id="L204">NIHALO = 2                      ! default = 4</span>
<span id="L205">                                ! The number of halo points on each side in the x-direction.  How this is set</span>
<span id="L206">                                ! varies with the calling component and static or dynamic memory configuration.</span>
<span id="L207">NJHALO = 2                      ! default = 4</span>
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
<span id="L220">INPUTDIR = &quot;.&quot;                  ! default = &quot;.&quot;</span>
<span id="L221">                                ! The directory in which input files are found.</span>
<span id="L222"></span>
<span id="L223">! === module MOM_grid_init ===</span>
<span id="L224">GRID_CONFIG = &quot;cartesian&quot;       !</span>
<span id="L225">                                ! A character string that determines the method for defining the horizontal</span>
<span id="L226">                                ! grid.  Current options are:</span>
<span id="L227">                                !     mosaic - read the grid from a mosaic (supergrid)</span>
<span id="L228">                                !              file set by GRID_FILE.</span>
<span id="L229">                                !     cartesian - use a (flat) Cartesian grid.</span>
<span id="L230">                                !     spherical - use a simple spherical grid.</span>
<span id="L231">                                !     mercator - use a Mercator spherical grid.</span>
<span id="L232">AXIS_UNITS = &quot;degrees&quot;          ! default = &quot;degrees&quot;</span>
<span id="L233">                                ! The units for the Cartesian axes. Valid entries are:</span>
<span id="L234">                                !     degrees - degrees of latitude and longitude</span>
<span id="L235">                                !     m or meter(s) - meters</span>
<span id="L236">                                !     k or km or kilometer(s) - kilometers</span>
<span id="L237">SOUTHLAT = 27.836               !   [degrees]</span>
<span id="L238">                                ! The southern latitude of the domain or the equivalent starting value for the</span>
<span id="L239">                                ! y-axis.</span>
<span id="L240">LENLAT = 2.0                    !   [degrees]</span>
<span id="L241">                                ! The latitudinal or y-direction length of the domain.</span>
<span id="L242">WESTLON = 0.0                   !   [degrees] default = 0.0</span>
<span id="L243">                                ! The western longitude of the domain or the equivalent starting value for the</span>
<span id="L244">                                ! x-axis.</span>
<span id="L245">LENLON = 2.0                    !   [degrees]</span>
<span id="L246">                                ! The longitudinal or x-direction length of the domain.</span>
<span id="L247">RAD_EARTH = 6.378E+06           !   [m] default = 6.378E+06</span>
<span id="L248">                                ! The radius of the Earth.</span>
<span id="L249">TOPO_CONFIG = &quot;flat&quot;            !</span>
<span id="L250">                                ! This specifies how bathymetry is specified:</span>
<span id="L251">                                !     file - read bathymetric information from the file</span>
<span id="L252">                                !       specified by (TOPO_FILE).</span>
<span id="L253">                                !     flat - flat bottom set to MAXIMUM_DEPTH.</span>
<span id="L254">                                !     bowl - an analytically specified bowl-shaped basin</span>
<span id="L255">                                !       ranging between MAXIMUM_DEPTH and MINIMUM_DEPTH.</span>
<span id="L256">                                !     spoon - a similar shape to &#x27;bowl&#x27;, but with an vertical</span>
<span id="L257">                                !       wall at the southern face.</span>
<span id="L258">                                !     halfpipe - a zonally uniform channel with a half-sine</span>
<span id="L259">                                !       profile in the meridional direction.</span>
<span id="L260">                                !     bbuilder - build topography from list of functions.</span>
<span id="L261">                                !     benchmark - use the benchmark test case topography.</span>
<span id="L262">                                !     Neverworld - use the Neverworld test case topography.</span>
<span id="L263">                                !     DOME - use a slope and channel configuration for the</span>
<span id="L264">                                !       DOME sill-overflow test case.</span>
<span id="L265">                                !     ISOMIP - use a slope and channel configuration for the</span>
<span id="L266">                                !       ISOMIP test case.</span>
<span id="L267">                                !     DOME2D - use a shelf and slope configuration for the</span>
<span id="L268">                                !       DOME2D gravity current/overflow test case.</span>
<span id="L269">                                !     Kelvin - flat but with rotated land mask.</span>
<span id="L270">                                !     seamount - Gaussian bump for spontaneous motion test case.</span>
<span id="L271">                                !     dumbbell - Sloshing channel with reservoirs on both ends.</span>
<span id="L272">                                !     shelfwave - exponential slope for shelfwave test case.</span>
<span id="L273">                                !     Phillips - ACC-like idealized topography used in the Phillips config.</span>
<span id="L274">                                !     dense - Denmark Strait-like dense water formation and overflow.</span>
<span id="L275">                                !     USER - call a user modified routine.</span>
<span id="L276">MINIMUM_DEPTH = 0.5             !   [m] default = 0.0</span>
<span id="L277">                                ! The minimum depth of the ocean.</span>
<span id="L278">MAXIMUM_DEPTH = 400.0           !   [m]</span>
<span id="L279">                                ! The maximum depth of the ocean.</span>
<span id="L280"></span>
<span id="L281">! === module MOM_open_boundary ===</span>
<span id="L282">! Controls where open boundaries are located, what kind of boundary condition to impose, and what data to apply,</span>
<span id="L283">! if any.</span>
<span id="L284">OBC_NUMBER_OF_SEGMENTS = 0      ! default = 0</span>
<span id="L285">                                ! The number of open boundary segments.</span>
<span id="L286">MASKING_DEPTH = -9999.0         !   [m] default = -9999.0</span>
<span id="L287">                                ! The depth below which to mask points as land points, for which all fluxes are</span>
<span id="L288">                                ! zeroed out. MASKING_DEPTH is ignored if it has the special default value.</span>
<span id="L289">CHANNEL_CONFIG = &quot;none&quot;         ! default = &quot;none&quot;</span>
<span id="L290">                                ! A parameter that determines which set of channels are</span>
<span id="L291">                                ! restricted to specific  widths.  Options are:</span>
<span id="L292">                                !     none - All channels have the grid width.</span>
<span id="L293">                                !     global_1deg - Sets 16 specific channels appropriate</span>
<span id="L294">                                !       for a 1-degree model, as used in CM2G.</span>
<span id="L295">                                !     list - Read the channel locations and widths from a</span>
<span id="L296">                                !       text file, like MOM_channel_list in the MOM_SIS</span>
<span id="L297">                                !       test case.</span>
<span id="L298">                                !     file - Read open face widths everywhere from a</span>
<span id="L299">                                !       NetCDF file on the model grid.</span>
<span id="L300">SUBGRID_TOPO_AT_VEL = False     !   [Boolean] default = False</span>
<span id="L301">                                ! If true, use variables from TOPO_AT_VEL_FILE as parameters for porous barrier.</span>
<span id="L302">ROTATION = &quot;betaplane&quot;          ! default = &quot;2omegasinlat&quot;</span>
<span id="L303">                                ! This specifies how the Coriolis parameter is specified:</span>
<span id="L304">                                !     2omegasinlat - Use twice the planetary rotation rate</span>
<span id="L305">                                !       times the sine of latitude.</span>
<span id="L306">                                !     betaplane - Use a beta-plane or f-plane.</span>
<span id="L307">                                !     USER - call a user modified routine.</span>
<span id="L308">F_0 = 1.0E-04                   !   [s-1] default = 0.0</span>
<span id="L309">                                ! The reference value of the Coriolis parameter with the betaplane option.</span>
<span id="L310">BETA = 0.0                      !   [m-1 s-1] default = 0.0</span>
<span id="L311">                                ! The northward gradient of the Coriolis parameter with the betaplane option.</span>
<span id="L312">BETA_LAT_REF = 0.0              !   [degrees] default = 0.0</span>
<span id="L313">                                ! The reference latitude (origin) of the beta-plane</span>
<span id="L314">GRID_ROTATION_ANGLE_BUGS = False !   [Boolean] default = False</span>
<span id="L315">                                ! If true, use an older algorithm to calculate the sine and cosines needed</span>
<span id="L316">                                ! rotate between grid-oriented directions and true north and east.  Differences</span>
<span id="L317">                                ! arise at the tripolar fold.</span>
<span id="L318"></span>
<span id="L319">! === module MOM_verticalGrid ===</span>
<span id="L320">! Parameters providing information about the vertical grid.</span>
<span id="L321">G_EARTH = 9.80616               !   [m s-2] default = 9.8</span>
<span id="L322">                                ! The gravitational acceleration of the Earth.</span>
<span id="L323">RHO_0 = 1000.0                  !   [kg m-3] default = 1035.0</span>
<span id="L324">                                ! The mean ocean density used with BOUSSINESQ true to calculate accelerations</span>
<span id="L325">                                ! and the mass for conservation properties, or with BOUSSINSEQ false to convert</span>
<span id="L326">                                ! some parameters from vertical units of m to kg m-2.</span>
<span id="L327">BOUSSINESQ = True               !   [Boolean] default = True</span>
<span id="L328">                                ! If true, make the Boussinesq approximation.</span>
<span id="L329">ANGSTROM = 1.0E-10              !   [m] default = 1.0E-10</span>
<span id="L330">                                ! The minimum layer thickness, usually one-Angstrom.</span>
<span id="L331">H_TO_M = 1.0                    !   [m H-1] default = 1.0</span>
<span id="L332">                                ! A constant that translates the model&#x27;s internal units of thickness into m.</span>
<span id="L333">NK = 400                        !   [nondim]</span>
<span id="L334">                                ! The number of model layers.</span>
<span id="L335">ADVECTION_SCHEME_VARIANCE_UNDERFLOW = 1.0E-23 !   [Conc2 (tracer dependent)] default = 1.0E-23</span>
<span id="L336">                                ! A tiny magnitude for variance used to determine when advection scheme variance</span>
<span id="L337">                                ! production is set to 0.</span>
<span id="L338"></span>
<span id="L339">! === module MOM_tracer_registry ===</span>
<span id="L340"></span>
<span id="L341">! === module MOM_EOS ===</span>
<span id="L342">EQN_OF_STATE = &quot;LINEAR&quot;         ! default = &quot;WRIGHT_FULL&quot;</span>
<span id="L343">                                ! EQN_OF_STATE determines which ocean equation of state should be used.</span>
<span id="L344">                                ! Currently, the valid choices are &quot;LINEAR&quot;, &quot;UNESCO&quot;, &quot;JACKETT_MCD&quot;, &quot;WRIGHT&quot;,</span>
<span id="L345">                                ! &quot;WRIGHT_REDUCED&quot;, &quot;WRIGHT_FULL&quot;, &quot;NEMO&quot;, &quot;ROQUET_RHO&quot;, &quot;ROQUET_SPV&quot; and</span>
<span id="L346">                                ! &quot;TEOS10&quot;.  This is only used if USE_EOS is true.</span>
<span id="L347">RHO_REF_LINEAR_EOS = 1000.0     !   [kg m-3] default = 1000.0</span>
<span id="L348">                                ! When EQN_OF_STATE=LINEAR, this is the density at T=T_REF_LINEAR_EOS,</span>
<span id="L349">                                ! S=S_REF_LINEAR_EOS and p=P_REF_LINEAR_EOS</span>
<span id="L350">T_REF_LINEAR_EOS = 0.0          !   [degC] default = 0.0</span>
<span id="L351">                                ! When EQN_OF_STATE=LINEAR, this is the reference temperature.</span>
<span id="L352">S_REF_LINEAR_EOS = 0.0          !   [psu] default = 0.0</span>
<span id="L353">                                ! When EQN_OF_STATE=LINEAR, this is the reference salinity.</span>
<span id="L354">P_REF_LINEAR_EOS = 0.0          !   [Pa] default = 0.0</span>
<span id="L355">                                ! When EQN_OF_STATE=LINEAR, this is the reference pressure.</span>
<span id="L356">DRHO_DT = -0.255                !   [kg m-3 K-1] default = -0.2</span>
<span id="L357">                                ! When EQN_OF_STATE=LINEAR, this is the partial derivative of density with</span>
<span id="L358">                                ! temperature.</span>
<span id="L359">DRHO_DS = 0.764                 !   [kg m-3 ppt-1] default = 0.8</span>
<span id="L360">                                ! When EQN_OF_STATE=LINEAR, this is the partial derivative of density with</span>
<span id="L361">                                ! salinity.</span>
<span id="L362">DRHO_DP = 0.0                   !   [s2 m-2] default = 0.0</span>
<span id="L363">                                ! When EQN_OF_STATE=LINEAR, this is the partial derivative of density with</span>
<span id="L364">                                ! pressure (the inverse of sound speed squared).</span>
<span id="L365">RHO_T0_S0 = 1000.0              !   [kg m-3] default = 1000.0</span>
<span id="L366">                                ! When EQN_OF_STATE=LINEAR, this is the density at T=0, S=0 and p=0.  If</span>
<span id="L367">                                ! RHO_TO_SO is specified, RHO_REF_LINEAR_EOS, T_REF_LINEAR_EOS, S_REF_LINEAR_EOS</span>
<span id="L368">                                ! and P_REF_LINEAR_EOS are not used.</span>
<span id="L369">EOS_QUADRATURE = False          !   [Boolean] default = False</span>
<span id="L370">                                ! If true, always use the generic (quadrature) code code for the integrals of</span>
<span id="L371">                                ! density.</span>
<span id="L372">TFREEZE_FORM = &quot;LINEAR&quot;         ! default = &quot;LINEAR&quot;</span>
<span id="L373">                                ! TFREEZE_FORM determines which expression should be used for the freezing</span>
<span id="L374">                                ! point.  Currently, the valid choices are &quot;LINEAR&quot;, &quot;MILLERO_78&quot;, &quot;TEOS_POLY&quot;,</span>
<span id="L375">                                ! &quot;TEOS10&quot;</span>
<span id="L376">TFREEZE_S0_P0 = 0.0             !   [degC] default = 0.0</span>
<span id="L377">                                ! When TFREEZE_FORM=LINEAR, this is the freezing potential temperature at S=0,</span>
<span id="L378">                                ! P=0.</span>
<span id="L379">DTFREEZE_DS = -0.054            !   [degC ppt-1] default = -0.054</span>
<span id="L380">                                ! When TFREEZE_FORM=LINEAR, this is the derivative of the freezing potential</span>
<span id="L381">                                ! temperature with salinity.</span>
<span id="L382">DTFREEZE_DP = 0.0               !   [degC Pa-1] default = 0.0</span>
<span id="L383">                                ! When TFREEZE_FORM=LINEAR, this is the derivative of the freezing potential</span>
<span id="L384">                                ! temperature with pressure.</span>
<span id="L385">TFREEZE_S_IS_PRACS = True       !   [Boolean] default = True</span>
<span id="L386">                                ! When True, the model will check if the model internal salinity is practical</span>
<span id="L387">                                ! salinity.  If the model uses absolute salinity, a conversion will be applied.</span>
<span id="L388">TFREEZE_T_IS_POTT = True        !   [Boolean] default = True</span>
<span id="L389">                                ! When True, the model will check if the model internal temperature is potential</span>
<span id="L390">                                ! temperature.  If the model uses conservative temperature, a conversion will be</span>
<span id="L391">                                ! applied.</span>
<span id="L392"></span>
<span id="L393">! === module MOM_restart ===</span>
<span id="L394">PARALLEL_RESTARTFILES = False   !   [Boolean] default = False</span>
<span id="L395">                                ! If true, the IO layout is used to group processors that write to the same</span>
<span id="L396">                                ! restart file or each processor writes its own (numbered) restart file. If</span>
<span id="L397">                                ! false, a single restart file is generated combining output from all PEs.</span>
<span id="L398">RESTARTFILE = &quot;MOM.res&quot;         ! default = &quot;MOM.res&quot;</span>
<span id="L399">                                ! The name-root of the restart file.</span>
<span id="L400">MAX_FIELDS = 100                ! default = 100</span>
<span id="L401">                                ! The maximum number of restart fields that can be used.</span>
<span id="L402">RESTART_CHECKSUMS_REQUIRED = True !   [Boolean] default = True</span>
<span id="L403">                                ! If true, require the restart checksums to match and error out otherwise. Users</span>
<span id="L404">                                ! may want to avoid this comparison if for example the restarts are made from a</span>
<span id="L405">                                ! run with a different mask_table than the current run, in which case the</span>
<span id="L406">                                ! checksums will not match and cause crash.</span>
<span id="L407">RESTART_SYMMETRIC_CHECKSUMS = False !   [Boolean] default = False</span>
<span id="L408">                                ! If true, do the restart checksums on all the edge points for a non-reentrant</span>
<span id="L409">                                ! grid.  This requires that SYMMETRIC_MEMORY_ is defined at compile time.</span>
<span id="L410">RESTART_UNSIGNED_ZEROS = False  !   [Boolean] default = False</span>
<span id="L411">                                ! If true, convert any negative zeros that would be written to the restart file</span>
<span id="L412">                                ! into ordinary unsigned zeros.  This does not change answers, but it can be</span>
<span id="L413">                                ! helpful in comparing restart files after grid rotation, for example.</span>
<span id="L414"></span>
<span id="L415">! === module MOM_tracer_flow_control ===</span>
<span id="L416">USE_USER_TRACER_EXAMPLE = False !   [Boolean] default = False</span>
<span id="L417">                                ! If true, use the USER_tracer_example tracer package.</span>
<span id="L418">USE_DOME_TRACER = False         !   [Boolean] default = False</span>
<span id="L419">                                ! If true, use the DOME_tracer tracer package.</span>
<span id="L420">USE_ISOMIP_TRACER = False       !   [Boolean] default = False</span>
<span id="L421">                                ! If true, use the ISOMIP_tracer tracer package.</span>
<span id="L422">USE_RGC_TRACER = False          !   [Boolean] default = False</span>
<span id="L423">                                ! If true, use the RGC_tracer tracer package.</span>
<span id="L424">USE_IDEAL_AGE_TRACER = False    !   [Boolean] default = False</span>
<span id="L425">                                ! If true, use the ideal_age_example tracer package.</span>
<span id="L426">USE_MARBL_TRACERS = False       !   [Boolean] default = False</span>
<span id="L427">                                ! If true, use the MARBL tracer package.</span>
<span id="L428">USE_REGIONAL_DYES = False       !   [Boolean] default = False</span>
<span id="L429">                                ! If true, use the regional_dyes tracer package.</span>
<span id="L430">USE_FILE_DYES = False           !   [Boolean] default = False</span>
<span id="L431">                                ! If true, use the file dyes tracer package.</span>
<span id="L432">USE_OIL_TRACER = False          !   [Boolean] default = False</span>
<span id="L433">                                ! If true, use the oil_tracer tracer package.</span>
<span id="L434">USE_ADVECTION_TEST_TRACER = False !   [Boolean] default = False</span>
<span id="L435">                                ! If true, use the advection_test_tracer tracer package.</span>
<span id="L436">USE_OCMIP2_CFC = False          !   [Boolean] default = False</span>
<span id="L437">                                ! If true, use the MOM_OCMIP2_CFC tracer package.</span>
<span id="L438">USE_CFC_CAP = False             !   [Boolean] default = False</span>
<span id="L439">                                ! If true, use the MOM_CFC_cap tracer package.</span>
<span id="L440">USE_generic_tracer = False      !   [Boolean] default = False</span>
<span id="L441">                                ! If true and _USE_GENERIC_TRACER is defined as a preprocessor macro, use the</span>
<span id="L442">                                ! MOM_generic_tracer packages.</span>
<span id="L443">USE_PSEUDO_SALT_TRACER = False  !   [Boolean] default = False</span>
<span id="L444">                                ! If true, use the pseudo salt tracer, typically run as a diagnostic.</span>
<span id="L445">USE_BOUNDARY_IMPULSE_TRACER = False !   [Boolean] default = False</span>
<span id="L446">                                ! If true, use the boundary impulse tracer.</span>
<span id="L447">USE_DYED_OBC_TRACER = False     !   [Boolean] default = False</span>
<span id="L448">                                ! If true, use the dyed_obc_tracer tracer package.</span>
<span id="L449">USE_NW2_TRACERS = False         !   [Boolean] default = False</span>
<span id="L450">                                ! If true, use the NeverWorld2 tracers.</span>
<span id="L451"></span>
<span id="L452">! === module MOM_coord_initialization ===</span>
<span id="L453">COORD_CONFIG = &quot;none&quot;           ! default = &quot;none&quot;</span>
<span id="L454">                                ! This specifies how layers are to be defined:</span>
<span id="L455">                                !     ALE or none - used to avoid defining layers in ALE mode</span>
<span id="L456">                                !     file - read coordinate information from the file</span>
<span id="L457">                                !       specified by (COORD_FILE).</span>
<span id="L458">                                !     BFB - Custom coords for buoyancy-forced basin case</span>
<span id="L459">                                !       based on SST_S, T_BOT and DRHO_DT.</span>
<span id="L460">                                !     linear - linear based on interfaces not layers</span>
<span id="L461">                                !     layer_ref - linear based on layer densities</span>
<span id="L462">                                !     ts_ref - use reference temperature and salinity</span>
<span id="L463">                                !     ts_range - use range of temperature and salinity</span>
<span id="L464">                                !       (T_REF and S_REF) to determine surface density</span>
<span id="L465">                                !       and GINT calculate internal densities.</span>
<span id="L466">                                !     gprime - use reference density (RHO_0) for surface</span>
<span id="L467">                                !       density and GINT calculate internal densities.</span>
<span id="L468">                                !     ts_profile - use temperature and salinity profiles</span>
<span id="L469">                                !       (read from COORD_FILE) to set layer densities.</span>
<span id="L470">                                !     USER - call a user modified routine.</span>
<span id="L471">GFS = 9.80616                   !   [m s-2] default = 9.80616</span>
<span id="L472">                                ! The reduced gravity at the free surface.</span>
<span id="L473">LIGHTEST_DENSITY = 1000.0       !   [kg m-3] default = 1000.0</span>
<span id="L474">                                ! The reference potential density used for layer 1.</span>
<span id="L475">REGRIDDING_COORDINATE_MODE = &quot;Z*&quot; ! default = &quot;LAYER&quot;</span>
<span id="L476">                                ! Coordinate mode for vertical regridding. Choose among the following</span>
<span id="L477">                                ! possibilities:  LAYER - Isopycnal or stacked shallow water layers</span>
<span id="L478">                                !  ZSTAR, Z* - stretched geopotential z*</span>
<span id="L479">                                !  SIGMA_SHELF_ZSTAR - stretched geopotential z* ignoring shelf</span>
<span id="L480">                                !  SIGMA - terrain following coordinates</span>
<span id="L481">                                !  RHO   - continuous isopycnal</span>
<span id="L482">                                !  HYCOM1 - HyCOM-like hybrid coordinate</span>
<span id="L483">                                !  HYBGEN - Hybrid coordinate from the Hycom hybgen code</span>
<span id="L484">                                !  ADAPTIVE - optimize for smooth neutral density surfaces</span>
<span id="L485">REGRIDDING_COORDINATE_UNITS = &quot;m&quot; ! default = &quot;m&quot;</span>
<span id="L486">                                ! Units of the regridding coordinate.</span>
<span id="L487">ALE_COORDINATE_CONFIG = &quot;UNIFORM&quot; ! default = &quot;UNIFORM&quot;</span>
<span id="L488">                                ! Determines how to specify the coordinate resolution. Valid options are:</span>
<span id="L489">                                !  PARAM       - use the vector-parameter ALE_RESOLUTION</span>
<span id="L490">                                !  UNIFORM[:N] - uniformly distributed</span>
<span id="L491">                                !  FILE:string - read from a file. The string specifies</span>
<span id="L492">                                !                the filename and variable name, separated</span>
<span id="L493">                                !                by a comma or space, e.g. FILE:lev.nc,dz</span>
<span id="L494">                                !                or FILE:lev.nc,interfaces=zw</span>
<span id="L495">                                !  WOA09[:N]   - the WOA09 vertical grid (approximately)</span>
<span id="L496">                                !  WOA09INT[:N] - layers spanned by the WOA09 depths</span>
<span id="L497">                                !  WOA23INT[:N] - layers spanned by the WOA23 depths</span>
<span id="L498">                                !  FNC1:string - FNC1:dz_min,H_total,power,precision</span>
<span id="L499">                                !  HYBRID:string - read from a file. The string specifies</span>
<span id="L500">                                !                the filename and two variable names, separated</span>
<span id="L501">                                !                by a comma or space, for sigma-2 and dz.</span>
<span id="L502">                                !                e.g. HYBRID:vgrid.nc,sigma2,dz</span>
<span id="L503">                                !  HYBRID_3D:string - read from a file. The string specifies</span>
<span id="L504">                                !                the filename and two 3D variable names, separated</span>
<span id="L505">                                !                by a comma or space, for sigma-2 and dz. The</span>
<span id="L506">                                !                latter can be FNC1:string which is used everywhere.</span>
<span id="L507">                                !                e.g. HYBRID_3D:vgrid.nc,sigma2,dz</span>
<span id="L508">                                !  HYBRID_MAP:string - read from a file. The string specifies</span>
<span id="L509">                                !                the filename and three variable names, separated</span>
<span id="L510">                                !                by a comma or space, for map, sigma-2 and dz.</span>
<span id="L511">                                !                Map is a spatial index array with, maxval(map)=N,</span>
<span id="L512">                                !                and the others are 2D arrays containing N profiles.</span>
<span id="L513">                                !                Map typically contains integer values, but it can</span>
<span id="L514">                                !                contain real values, I+w, which imply using</span>
<span id="L515">                                !                the weighted sum of profiles I and I+1.</span>
<span id="L516">                                !                Dz can be FNC1:string which is used everywhere.</span>
<span id="L517">                                !                e.g. HYBRID_MAP:vgrid.nc,map,sigma2,dz</span>
<span id="L518">!ALE_RESOLUTION = 400*1.0       !   [m]</span>
<span id="L519">                                ! The distribution of vertical resolution for the target</span>
<span id="L520">                                ! grid used for Eulerian-like coordinates. For example,</span>
<span id="L521">                                ! in z-coordinate mode, the parameter is a list of level</span>
<span id="L522">                                ! thicknesses (in m). In sigma-coordinate mode, the list</span>
<span id="L523">                                ! is of non-dimensional fractions of the water column.</span>
<span id="L524">MIN_THICKNESS = 0.001           !   [m] default = 0.001</span>
<span id="L525">                                ! When regridding, this is the minimum layer thickness allowed.</span>
<span id="L526">REMAPPING_SCHEME = &quot;PLM&quot;        ! default = &quot;PLM&quot;</span>
<span id="L527">                                ! This sets the reconstruction scheme used for vertical remapping for all</span>
<span id="L528">                                ! variables. It can be one of the following schemes:</span>
<span id="L529">                                ! PCM         (1st-order accurate)</span>
<span id="L530">                                ! PLM         (2nd-order accurate)</span>
<span id="L531">                                ! PLM_HYBGEN  (2nd-order accurate)</span>
<span id="L532">                                ! PPM_H4      (3rd-order accurate)</span>
<span id="L533">                                ! PPM_IH4     (3rd-order accurate)</span>
<span id="L534">                                ! PPM_HYBGEN  (3rd-order accurate)</span>
<span id="L535">                                ! WENO_HYBGEN (3rd-order accurate)</span>
<span id="L536">                                ! PQM_IH4IH3  (4th-order accurate)</span>
<span id="L537">                                ! PQM_IH6IH5  (5th-order accurate)</span>
<span id="L538">VELOCITY_REMAPPING_SCHEME = &quot;PLM&quot; ! default = &quot;PLM&quot;</span>
<span id="L539">                                ! This sets the reconstruction scheme used for vertical remapping of velocities.</span>
<span id="L540">                                ! By default it is the same as REMAPPING_SCHEME. It can be one of the following</span>
<span id="L541">                                ! schemes:</span>
<span id="L542">                                ! PCM         (1st-order accurate)</span>
<span id="L543">                                ! PLM         (2nd-order accurate)</span>
<span id="L544">                                ! PLM_HYBGEN  (2nd-order accurate)</span>
<span id="L545">                                ! PPM_H4      (3rd-order accurate)</span>
<span id="L546">                                ! PPM_IH4     (3rd-order accurate)</span>
<span id="L547">                                ! PPM_HYBGEN  (3rd-order accurate)</span>
<span id="L548">                                ! WENO_HYBGEN (3rd-order accurate)</span>
<span id="L549">                                ! PQM_IH4IH3  (4th-order accurate)</span>
<span id="L550">                                ! PQM_IH6IH5  (5th-order accurate)</span>
<span id="L551">FATAL_CHECK_RECONSTRUCTIONS = False !   [Boolean] default = False</span>
<span id="L552">                                ! If true, cell-by-cell reconstructions are checked for consistency and if</span>
<span id="L553">                                ! non-monotonicity or an inconsistency is detected then a FATAL error is issued.</span>
<span id="L554">FATAL_CHECK_REMAPPING = False   !   [Boolean] default = False</span>
<span id="L555">                                ! If true, the results of remapping are checked for conservation and new extrema</span>
<span id="L556">                                ! and if an inconsistency is detected then a FATAL error is issued.</span>
<span id="L557">REMAP_BOUND_INTERMEDIATE_VALUES = False !   [Boolean] default = False</span>
<span id="L558">                                ! If true, the values on the intermediate grid used for remapping are forced to</span>
<span id="L559">                                ! be bounded, which might not be the case due to round off.</span>
<span id="L560">REMAP_BOUNDARY_EXTRAP = False   !   [Boolean] default = False</span>
<span id="L561">                                ! If true, values at the interfaces of boundary cells are extrapolated instead</span>
<span id="L562">                                ! of piecewise constant</span>
<span id="L563">INIT_BOUNDARY_EXTRAP = False    !   [Boolean] default = False</span>
<span id="L564">                                ! If true, values at the interfaces of boundary cells are extrapolated instead</span>
<span id="L565">                                ! of piecewise constant during initialization.Defaults to REMAP_BOUNDARY_EXTRAP.</span>
<span id="L566">REMAPPING_USE_OM4_SUBCELLS = True !   [Boolean] default = True</span>
<span id="L567">                                ! This selects the remapping algorithm used in OM4 that does not use the full</span>
<span id="L568">                                ! reconstruction for the top- and lower-most sub-layers, but instead assumes</span>
<span id="L569">                                ! they are always vanished (untrue) and so just uses their edge values. We</span>
<span id="L570">                                ! recommend setting this option to false.</span>
<span id="L571">REMAPPING_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L572">                                ! The vintage of the expressions and order of arithmetic to use for remapping.</span>
<span id="L573">                                ! Values below 20190101 result in the use of older, less accurate expressions</span>
<span id="L574">                                ! that were in use at the end of 2018.  Higher values result in the use of more</span>
<span id="L575">                                ! robust and accurate forms of mathematically equivalent expressions.</span>
<span id="L576">PARTIAL_CELL_VELOCITY_REMAP = False !   [Boolean] default = False</span>
<span id="L577">                                ! If true, use partial cell thicknesses at velocity points that are masked out</span>
<span id="L578">                                ! where they extend below the shallower of the neighboring bathymetry for</span>
<span id="L579">                                ! remapping velocity.</span>
<span id="L580">REMAP_AFTER_INITIALIZATION = True !   [Boolean] default = True</span>
<span id="L581">                                ! If true, applies regridding and remapping immediately after initialization so</span>
<span id="L582">                                ! that the state is ALE consistent. This is a legacy step and should not be</span>
<span id="L583">                                ! needed if the initialization is consistent with the coordinate mode.</span>
<span id="L584">REGRID_TIME_SCALE = 0.0         !   [s] default = 0.0</span>
<span id="L585">                                ! The time-scale used in blending between the current (old) grid and the target</span>
<span id="L586">                                ! (new) grid. A short time-scale favors the target grid (0. or anything less</span>
<span id="L587">                                ! than DT_THERM) has no memory of the old grid. A very long time-scale makes the</span>
<span id="L588">                                ! model more Lagrangian.</span>
<span id="L589">REGRID_FILTER_SHALLOW_DEPTH = 0.0 !   [m] default = 0.0</span>
<span id="L590">                                ! The depth above which no time-filtering is applied. Above this depth final</span>
<span id="L591">                                ! grid exactly matches the target (new) grid.</span>
<span id="L592">REGRID_FILTER_DEEP_DEPTH = 0.0  !   [m] default = 0.0</span>
<span id="L593">                                ! The depth below which full time-filtering is applied with time-scale</span>
<span id="L594">                                ! REGRID_TIME_SCALE. Between depths REGRID_FILTER_SHALLOW_DEPTH and</span>
<span id="L595">                                ! REGRID_FILTER_SHALLOW_DEPTH the filter weights adopt a cubic profile.</span>
<span id="L596">REMAP_VEL_MASK_BBL_THICK = -0.001 !   [m] default = -0.001</span>
<span id="L597">                                ! A thickness of a bottom boundary layer below which velocities in thin layers</span>
<span id="L598">                                ! are zeroed out after remapping, following practice with Hybgen remapping, or a</span>
<span id="L599">                                ! negative value to avoid such filtering altogether.</span>
<span id="L600">REMAP_VEL_CONSERVE_KE = False   !   [Boolean] default = False</span>
<span id="L601">                                ! If true, a correction is applied to the baroclinic component of velocity after</span>
<span id="L602">                                ! remapping so that total KE is conserved. KE may not be conserved when</span>
<span id="L603">                                ! (CS%BBL_h_vel_mask &gt; 0.0) .and. (CS%h_vel_mask &gt; 0.0)</span>
<span id="L604"></span>
<span id="L605">! === module MOM_state_initialization ===</span>
<span id="L606">FATAL_INCONSISTENT_RESTART_TIME = False !   [Boolean] default = False</span>
<span id="L607">                                ! If true and a time_in value is provided to MOM_initialize_state, verify that</span>
<span id="L608">                                ! the time read from a restart file is the same as time_in, and issue a fatal</span>
<span id="L609">                                ! error if it is not.  Otherwise, simply set the time to time_in if present.</span>
<span id="L610">INIT_LAYERS_FROM_Z_FILE = False !   [Boolean] default = False</span>
<span id="L611">                                ! If true, initialize the layer thicknesses, temperatures, and salinities from a</span>
<span id="L612">                                ! Z-space file on a latitude-longitude grid.</span>
<span id="L613">THICKNESS_CONFIG = &quot;coord&quot;      ! default = &quot;uniform&quot;</span>
<span id="L614">                                ! A string that determines how the initial layer thicknesses are specified for a</span>
<span id="L615">                                ! new run:</span>
<span id="L616">                                !     file - read interface heights from the file specified</span>
<span id="L617">                                !       by (THICKNESS_FILE).</span>
<span id="L618">                                !     thickness_file - read thicknesses from the file specified</span>
<span id="L619">                                !       by (THICKNESS_FILE).</span>
<span id="L620">                                !     mass_file - read thicknesses in units of mass per unit area from the file</span>
<span id="L621">                                !       specified by (THICKNESS_FILE).</span>
<span id="L622">                                !     coord - determined by ALE coordinate.</span>
<span id="L623">                                !     uniform - uniform thickness layers evenly distributed</span>
<span id="L624">                                !       between the surface and MAXIMUM_DEPTH.</span>
<span id="L625">                                !     list - read a list of positive interface depths.</span>
<span id="L626">                                !     param - use thicknesses from parameter THICKNESS_INIT_VALUES.</span>
<span id="L627">                                !     DOME - use a slope and channel configuration for the</span>
<span id="L628">                                !       DOME sill-overflow test case.</span>
<span id="L629">                                !     ISOMIP - use a configuration for the</span>
<span id="L630">                                !       ISOMIP test case.</span>
<span id="L631">                                !     benchmark - use the benchmark test case thicknesses.</span>
<span id="L632">                                !     Neverworld - use the Neverworld test case thicknesses.</span>
<span id="L633">                                !     search - search a density profile for the interface</span>
<span id="L634">                                !       densities. This is not yet implemented.</span>
<span id="L635">                                !     circle_obcs - the circle_obcs test case is used.</span>
<span id="L636">                                !     DOME2D - 2D version of DOME initialization.</span>
<span id="L637">                                !     adjustment2d - 2D lock exchange thickness ICs.</span>
<span id="L638">                                !     sloshing - sloshing gravity thickness ICs.</span>
<span id="L639">                                !     seamount - no motion test with seamount ICs.</span>
<span id="L640">                                !     dumbbell - sloshing channel ICs.</span>
<span id="L641">                                !     soliton - Equatorial Rossby soliton.</span>
<span id="L642">                                !     rossby_front - a mixed layer front in thermal wind balance.</span>
<span id="L643">                                !     USER - call a user modified routine.</span>
<span id="L644">TS_CONFIG = &quot;SCM_CVMix_tests&quot;   !</span>
<span id="L645">                                ! A string that determines how the initial temperatures and salinities are</span>
<span id="L646">                                ! specified for a new run:</span>
<span id="L647">                                !     file - read velocities from the file specified</span>
<span id="L648">                                !       by (TS_FILE).</span>
<span id="L649">                                !     fit - find the temperatures that are consistent with</span>
<span id="L650">                                !       the layer densities and salinity S_REF.</span>
<span id="L651">                                !     TS_profile - use temperature and salinity profiles</span>
<span id="L652">                                !       (read from TS_FILE) to set layer densities.</span>
<span id="L653">                                !     benchmark - use the benchmark test case T &amp; S.</span>
<span id="L654">                                !     linear - linear in logical layer space.</span>
<span id="L655">                                !     DOME2D - 2D DOME initialization.</span>
<span id="L656">                                !     ISOMIP - ISOMIP initialization.</span>
<span id="L657">                                !     adjustment2d - 2d lock exchange T/S ICs.</span>
<span id="L658">                                !     sloshing - sloshing mode T/S ICs.</span>
<span id="L659">                                !     seamount - no motion test with seamount ICs.</span>
<span id="L660">                                !     dumbbell - sloshing channel ICs.</span>
<span id="L661">                                !     rossby_front - a mixed layer front in thermal wind balance.</span>
<span id="L662">                                !     SCM_CVMix_tests - used in the SCM CVMix tests.</span>
<span id="L663">                                !     USER - call a user modified routine.</span>
<span id="L664">SCM_TEMP_MLD = 0.0              !   [m] default = 0.0</span>
<span id="L665">                                ! Initial temp mixed layer depth</span>
<span id="L666">SCM_SALT_MLD = 0.0              !   [m] default = 0.0</span>
<span id="L667">                                ! Initial salt mixed layer depth</span>
<span id="L668">SCM_L1_SALT = 35.0              !   [ppt] default = 35.0</span>
<span id="L669">                                ! Layer 2 surface salinity</span>
<span id="L670">SCM_L1_TEMP = 15.0              !   [degC] default = 20.0</span>
<span id="L671">                                ! Layer 1 surface temperature</span>
<span id="L672">SCM_L2_SALT = 35.0              !   [ppt] default = 35.0</span>
<span id="L673">                                ! Layer 2 surface salinity</span>
<span id="L674">SCM_L2_TEMP = 15.0              !   [degC] default = 20.0</span>
<span id="L675">                                ! Layer 2 surface temperature</span>
<span id="L676">SCM_L2_DTDZ = 0.0               !   [C/m] default = 0.0</span>
<span id="L677">                                ! Initial temperature stratification in layer 2</span>
<span id="L678">SCM_L2_DSDZ = 0.0               !   [PPT/m] default = 0.0</span>
<span id="L679">                                ! Initial salinity stratification in layer 2</span>
<span id="L680">SCM_L2_MINTEMP = 4.0            !   [degC] default = 4.0</span>
<span id="L681">                                ! Layer 2 minimum temperature</span>
<span id="L682">DEPRESS_INITIAL_SURFACE = False !   [Boolean] default = False</span>
<span id="L683">                                ! If true,  depress the initial surface to avoid huge tsunamis when a large</span>
<span id="L684">                                ! surface pressure is applied.</span>
<span id="L685">TRIM_IC_FOR_P_SURF = False      !   [Boolean] default = False</span>
<span id="L686">                                ! If true, cuts way the top of the column for initial conditions at the depth</span>
<span id="L687">                                ! where the hydrostatic pressure matches the imposed surface pressure which is</span>
<span id="L688">                                ! read from file.</span>
<span id="L689">REGRID_ACCELERATE_INIT = False  !   [Boolean] default = False</span>
<span id="L690">                                ! If true, runs REGRID_ACCELERATE_ITERATIONS iterations of the regridding</span>
<span id="L691">                                ! algorithm to push the initial grid to be consistent with the initial</span>
<span id="L692">                                ! condition. Useful only for state-based and iterative coordinates.</span>
<span id="L693">VELOCITY_CONFIG = &quot;zero&quot;        ! default = &quot;zero&quot;</span>
<span id="L694">                                ! A string that determines how the initial velocities are specified for a new</span>
<span id="L695">                                ! run:</span>
<span id="L696">                                !     file - read velocities from the file specified</span>
<span id="L697">                                !       by (VELOCITY_FILE).</span>
<span id="L698">                                !     zero - the fluid is initially at rest.</span>
<span id="L699">                                !     uniform - the flow is uniform (determined by</span>
<span id="L700">                                !       parameters INITIAL_U_CONST and INITIAL_V_CONST).</span>
<span id="L701">                                !     rossby_front - a mixed layer front in thermal wind balance.</span>
<span id="L702">                                !     soliton - Equatorial Rossby soliton.</span>
<span id="L703">                                !     USER - call a user modified routine.</span>
<span id="L704">ODA_INCUPD = False              !   [Boolean] default = False</span>
<span id="L705">                                ! If true, oda incremental updates will be applied everywhere in the domain.</span>
<span id="L706">SPONGE = False                  !   [Boolean] default = False</span>
<span id="L707">                                ! If true, sponges may be applied anywhere in the domain. The exact location and</span>
<span id="L708">                                ! properties of those sponges are specified via SPONGE_CONFIG.</span>
<span id="L709"></span>
<span id="L710">! === module MOM_diag_mediator ===</span>
<span id="L711">NUM_DIAG_COORDS = 1             ! default = 1</span>
<span id="L712">                                ! The number of diagnostic vertical coordinates to use. For each coordinate, an</span>
<span id="L713">                                ! entry in DIAG_COORDS must be provided.</span>
<span id="L714">DIAG_REMAPPING_USE_OM4_SUBCELLS = True !   [Boolean] default = True</span>
<span id="L715">                                ! If true, use the OM4 remapping-via-subcells algorithm for diagnostics. See</span>
<span id="L716">                                ! REMAPPING_USE_OM4_SUBCELLS for details. We recommend setting this option to</span>
<span id="L717">                                ! false.</span>
<span id="L718">USE_INDEX_DIAGNOSTIC_AXES = False !   [Boolean] default = False</span>
<span id="L719">                                ! If true, use a grid index coordinate convention for diagnostic axes.</span>
<span id="L720">DIAG_COORDS = &quot;z Z ZSTAR&quot;       ! default = &quot;z Z ZSTAR&quot;</span>
<span id="L721">                                ! A list of string tuples associating diag_table modules to a coordinate</span>
<span id="L722">                                ! definition used for diagnostics. Each string is of the form &quot;MODULE_SUFFIX</span>
<span id="L723">                                ! PARAMETER_SUFFIX COORDINATE_NAME&quot;.</span>
<span id="L724">DIAG_MISVAL = 1.0E+20           !   [various] default = 1.0E+20</span>
<span id="L725">                                ! Set the default missing value to use for diagnostics.</span>
<span id="L726">DIAG_AS_CHKSUM = False          !   [Boolean] default = False</span>
<span id="L727">                                ! Instead of writing diagnostics to the diag manager, write a text file</span>
<span id="L728">                                ! containing the checksum (bitcount) of the array.</span>
<span id="L729">AVAILABLE_DIAGS_FILE = &quot;available_diags.000000&quot; ! default = &quot;available_diags.000000&quot;</span>
<span id="L730">                                ! A file into which to write a list of all available ocean diagnostics that can</span>
<span id="L731">                                ! be included in a diag_table.</span>
<span id="L732">DIAG_COORD_DEF_Z = &quot;UNIFORM&quot;    ! default = &quot;UNIFORM&quot;</span>
<span id="L733">                                ! Determines how to specify the coordinate resolution. Valid options are:</span>
<span id="L734">                                !  PARAM       - use the vector-parameter DIAG_COORD_RES_Z</span>
<span id="L735">                                !  UNIFORM[:N] - uniformly distributed</span>
<span id="L736">                                !  FILE:string - read from a file. The string specifies</span>
<span id="L737">                                !                the filename and variable name, separated</span>
<span id="L738">                                !                by a comma or space, e.g. FILE:lev.nc,dz</span>
<span id="L739">                                !                or FILE:lev.nc,interfaces=zw</span>
<span id="L740">                                !  WOA09[:N]   - the WOA09 vertical grid (approximately)</span>
<span id="L741">                                !  WOA09INT[:N] - layers spanned by the WOA09 depths</span>
<span id="L742">                                !  WOA23INT[:N] - layers spanned by the WOA23 depths</span>
<span id="L743">                                !  FNC1:string - FNC1:dz_min,H_total,power,precision</span>
<span id="L744">                                !  HYBRID:string - read from a file. The string specifies</span>
<span id="L745">                                !                the filename and two variable names, separated</span>
<span id="L746">                                !                by a comma or space, for sigma-2 and dz.</span>
<span id="L747">                                !                e.g. HYBRID:vgrid.nc,sigma2,dz</span>
<span id="L748">                                !  HYBRID_3D:string - read from a file. The string specifies</span>
<span id="L749">                                !                the filename and two 3D variable names, separated</span>
<span id="L750">                                !                by a comma or space, for sigma-2 and dz. The</span>
<span id="L751">                                !                latter can be FNC1:string which is used everywhere.</span>
<span id="L752">                                !                e.g. HYBRID_3D:vgrid.nc,sigma2,dz</span>
<span id="L753">                                !  HYBRID_MAP:string - read from a file. The string specifies</span>
<span id="L754">                                !                the filename and three variable names, separated</span>
<span id="L755">                                !                by a comma or space, for map, sigma-2 and dz.</span>
<span id="L756">                                !                Map is a spatial index array with, maxval(map)=N,</span>
<span id="L757">                                !                and the others are 2D arrays containing N profiles.</span>
<span id="L758">                                !                Map typically contains integer values, but it can</span>
<span id="L759">                                !                contain real values, I+w, which imply using</span>
<span id="L760">                                !                the weighted sum of profiles I and I+1.</span>
<span id="L761">                                !                Dz can be FNC1:string which is used everywhere.</span>
<span id="L762">                                !                e.g. HYBRID_MAP:vgrid.nc,map,sigma2,dz</span>
<span id="L763"></span>
<span id="L764">! === module MOM_MEKE ===</span>
<span id="L765">USE_MEKE = False                !   [Boolean] default = False</span>
<span id="L766">                                ! If true, turns on the MEKE scheme which calculates a sub-grid mesoscale eddy</span>
<span id="L767">                                ! kinetic energy budget.</span>
<span id="L768"></span>
<span id="L769">! === module MOM_lateral_mixing_coeffs ===</span>
<span id="L770">USE_VARIABLE_MIXING = False     !   [Boolean] default = False</span>
<span id="L771">                                ! If true, the variable mixing code will be called.  This allows diagnostics to</span>
<span id="L772">                                ! be created even if the scheme is not used.  If KHTR_SLOPE_CFF&gt;0 or</span>
<span id="L773">                                ! KhTh_Slope_Cff&gt;0, this is set to true regardless of what is in the parameter</span>
<span id="L774">                                ! file.</span>
<span id="L775">USE_VISBECK = False             !   [Boolean] default = False</span>
<span id="L776">                                ! If true, use the Visbeck et al. (1997) formulation for</span>
<span id="L777">                                ! thickness diffusivity.</span>
<span id="L778">RESOLN_SCALED_KH = False        !   [Boolean] default = False</span>
<span id="L779">                                ! If true, the Laplacian lateral viscosity is scaled away when the first</span>
<span id="L780">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L781">DEPTH_SCALED_KHTH = False       !   [Boolean] default = False</span>
<span id="L782">                                ! If true, KHTH is scaled away when the depth is shallowerthan a reference</span>
<span id="L783">                                ! depth: KHTH = MIN(1,H/H0)**N * KHTH, where H0 is a reference depth, controlled</span>
<span id="L784">                                ! via DEPTH_SCALED_KHTH_H0, and the exponent (N) is controlled via</span>
<span id="L785">                                ! DEPTH_SCALED_KHTH_EXP.</span>
<span id="L786">RESOLN_SCALED_KHTH = False      !   [Boolean] default = False</span>
<span id="L787">                                ! If true, the interface depth diffusivity is scaled away when the first</span>
<span id="L788">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L789">RESOLN_SCALED_KHTR = False      !   [Boolean] default = False</span>
<span id="L790">                                ! If true, the epipycnal tracer diffusivity is scaled away when the first</span>
<span id="L791">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L792">RESOLN_USE_EBT = False          !   [Boolean] default = False</span>
<span id="L793">                                ! If true, uses the equivalent barotropic wave speed instead of first baroclinic</span>
<span id="L794">                                ! wave for calculating the resolution fn.</span>
<span id="L795">BACKSCAT_EBT_POWER = 0.0        !   [nondim] default = 0.0</span>
<span id="L796">                                ! Power to raise EBT vertical structure to when backscatter has vertical</span>
<span id="L797">                                ! structure.</span>
<span id="L798">BS_USE_SQG_STRUCT = False       !   [Boolean] default = False</span>
<span id="L799">                                ! If true, the SQG vertical structure is used for backscatter on the condition</span>
<span id="L800">                                ! that BS_EBT_power=0</span>
<span id="L801">KHTH_USE_EBT_STRUCT = False     !   [Boolean] default = False</span>
<span id="L802">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L803">                                ! thickness diffusivity.</span>
<span id="L804">KHTH_USE_SQG_STRUCT = False     !   [Boolean] default = False</span>
<span id="L805">                                ! If true, uses the surface quasigeostrophic structure as the vertical structure</span>
<span id="L806">                                ! of thickness diffusivity.</span>
<span id="L807">KHTR_USE_EBT_STRUCT = False     !   [Boolean] default = False</span>
<span id="L808">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L809">                                ! tracer diffusivity.</span>
<span id="L810">KHTR_USE_SQG_STRUCT = False     !   [Boolean] default = False</span>
<span id="L811">                                ! If true, uses the surface quasigeostrophic structure as the vertical structure</span>
<span id="L812">                                ! of tracer diffusivity.</span>
<span id="L813">KD_GL90_USE_EBT_STRUCT = False  !   [Boolean] default = False</span>
<span id="L814">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L815">                                ! diffusivity in the GL90 scheme.</span>
<span id="L816">KD_GL90_USE_SQG_STRUCT = False  !   [Boolean] default = False</span>
<span id="L817">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L818">                                ! diffusivity in the GL90 scheme.</span>
<span id="L819">KHTH_SLOPE_CFF = 0.0            !   [nondim] default = 0.0</span>
<span id="L820">                                ! The nondimensional coefficient in the Visbeck formula for the interface depth</span>
<span id="L821">                                ! diffusivity</span>
<span id="L822">KHTR_SLOPE_CFF = 0.0            !   [nondim] default = 0.0</span>
<span id="L823">                                ! The nondimensional coefficient in the Visbeck formula for the epipycnal tracer</span>
<span id="L824">                                ! diffusivity</span>
<span id="L825">USE_STORED_SLOPES = False       !   [Boolean] default = False</span>
<span id="L826">                                ! If true, the isopycnal slopes are calculated once and stored for re-use. This</span>
<span id="L827">                                ! uses more memory but avoids calling the equation of state more times than</span>
<span id="L828">                                ! should be necessary.</span>
<span id="L829">VERY_SMALL_FREQUENCY = 1.0E-17  !   [s-1] default = 1.0E-17</span>
<span id="L830">                                ! A miniscule frequency that is used to avoid division by 0.  The default value</span>
<span id="L831">                                ! is roughly (pi / (the age of the universe)).</span>
<span id="L832">USE_STANLEY_ISO = False         !   [Boolean] default = False</span>
<span id="L833">                                ! If true, turn on Stanley SGS T variance parameterization in isopycnal slope</span>
<span id="L834">                                ! code.</span>
<span id="L835">KD_SMOOTH = 1.0E-06             !   [m2 s-1] default = 1.0E-06</span>
<span id="L836">                                ! A diapycnal diffusivity that is used to interpolate more sensible values of T</span>
<span id="L837">                                ! &amp; S into thin layers.</span>
<span id="L838">USE_QG_LEITH_GM = False         !   [Boolean] default = False</span>
<span id="L839">                                ! If true, use the QG Leith viscosity as the GM coefficient.</span>
<span id="L840"></span>
<span id="L841">! === module MOM_set_visc ===</span>
<span id="L842">SET_VISC_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L843">                                ! The vintage of the order of arithmetic and expressions in the set viscosity</span>
<span id="L844">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L845">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L846">BOTTOMDRAGLAW = True            !   [Boolean] default = True</span>
<span id="L847">                                ! If true, the bottom stress is calculated with a drag law of the form</span>
<span id="L848">                                ! c_drag*|u|*u. The velocity magnitude may be an assumed value or it may be</span>
<span id="L849">                                ! based on the actual velocity in the bottommost HBBL, depending on LINEAR_DRAG.</span>
<span id="L850">DRAG_AS_BODY_FORCE = False      !   [Boolean] default = False</span>
<span id="L851">                                ! If true, the bottom stress is imposed as an explicit body force applied over a</span>
<span id="L852">                                ! fixed distance from the bottom, rather than as an implicit calculation based</span>
<span id="L853">                                ! on an enhanced near-bottom viscosity. The thickness of the bottom boundary</span>
<span id="L854">                                ! layer is HBBL.</span>
<span id="L855">CHANNEL_DRAG = False            !   [Boolean] default = False</span>
<span id="L856">                                ! If true, the bottom drag is exerted directly on each layer proportional to the</span>
<span id="L857">                                ! fraction of the bottom it overlies.</span>
<span id="L858">LINEAR_DRAG = False             !   [Boolean] default = False</span>
<span id="L859">                                ! If LINEAR_DRAG and BOTTOMDRAGLAW are defined the drag law is</span>
<span id="L860">                                ! cdrag*DRAG_BG_VEL*u.</span>
<span id="L861">DYNAMIC_VISCOUS_ML = False      !   [Boolean] default = False</span>
<span id="L862">                                ! If true, use a bulk Richardson number criterion to determine the mixed layer</span>
<span id="L863">                                ! thickness for viscosity.</span>
<span id="L864">OMEGA = 7.2921E-05              !   [s-1] default = 7.2921E-05</span>
<span id="L865">                                ! The rotation rate of the earth.</span>
<span id="L866">HBBL = 10.0                     !   [m]</span>
<span id="L867">                                ! The thickness of a bottom boundary layer with a viscosity increased by</span>
<span id="L868">                                ! KV_EXTRA_BBL if BOTTOMDRAGLAW is not defined, or the thickness over which</span>
<span id="L869">                                ! near-bottom velocities are averaged for the drag law if BOTTOMDRAGLAW is</span>
<span id="L870">                                ! defined but LINEAR_DRAG is not.</span>
<span id="L871">CDRAG = 0.0                     !   [nondim] default = 0.003</span>
<span id="L872">                                ! CDRAG is the drag coefficient relating the magnitude of the velocity field to</span>
<span id="L873">                                ! the bottom stress. CDRAG is only used if BOTTOMDRAGLAW is defined.</span>
<span id="L874">BBL_USE_TIDAL_BG = False        !   [Boolean] default = False</span>
<span id="L875">                                ! Flag to use the tidal RMS amplitude in place of constant background velocity</span>
<span id="L876">                                ! for computing u* in the BBL. This flag is only used when BOTTOMDRAGLAW is true</span>
<span id="L877">                                ! and LINEAR_DRAG is false.</span>
<span id="L878">DRAG_BG_VEL = 0.1               !   [m s-1] default = 0.0</span>
<span id="L879">                                ! DRAG_BG_VEL is either the assumed bottom velocity (with LINEAR_DRAG) or an</span>
<span id="L880">                                ! unresolved  velocity that is combined with the resolved velocity to estimate</span>
<span id="L881">                                ! the velocity magnitude.  DRAG_BG_VEL is only used when BOTTOMDRAGLAW is</span>
<span id="L882">                                ! defined.</span>
<span id="L883">BBL_USE_EOS = True              !   [Boolean] default = True</span>
<span id="L884">                                ! If true, use the equation of state in determining the properties of the bottom</span>
<span id="L885">                                ! boundary layer.  Otherwise use the layer target potential densities.  The</span>
<span id="L886">                                ! default of this parameter is the value of USE_EOS.</span>
<span id="L887">BBL_THICK_MIN = 0.1             !   [m] default = 0.0</span>
<span id="L888">                                ! The minimum bottom boundary layer thickness that can be used with</span>
<span id="L889">                                ! BOTTOMDRAGLAW. This might be Kv/(cdrag*drag_bg_vel) to give Kv as the minimum</span>
<span id="L890">                                ! near-bottom viscosity.</span>
<span id="L891">HTBL_SHELF_MIN = 0.1            !   [m] default = 0.1</span>
<span id="L892">                                ! The minimum top boundary layer thickness that can be used with BOTTOMDRAGLAW.</span>
<span id="L893">                                ! This might be Kv/(cdrag*drag_bg_vel) to give Kv as the minimum near-top</span>
<span id="L894">                                ! viscosity.</span>
<span id="L895">HTBL_SHELF = 10.0               !   [m] default = 10.0</span>
<span id="L896">                                ! The thickness over which near-surface velocities are averaged for the drag law</span>
<span id="L897">                                ! under an ice shelf.  By default this is the same as HBBL</span>
<span id="L898">KV = 0.0                        !   [m2 s-1]</span>
<span id="L899">                                ! The background kinematic viscosity in the interior. The molecular value, ~1e-6</span>
<span id="L900">                                ! m2 s-1, may be used.</span>
<span id="L901">KV_BBL_MIN = 0.0                !   [m2 s-1] default = 0.0</span>
<span id="L902">                                ! The minimum viscosities in the bottom boundary layer.</span>
<span id="L903">KV_TBL_MIN = 0.0                !   [m2 s-1] default = 0.0</span>
<span id="L904">                                ! The minimum viscosities in the top boundary layer.</span>
<span id="L905">CORRECT_BBL_BOUNDS = False      !   [Boolean] default = False</span>
<span id="L906">                                ! If true, uses the correct bounds on the BBL thickness and viscosity so that</span>
<span id="L907">                                ! the bottom layer feels the intended drag.</span>
<span id="L908"></span>
<span id="L909">! === module MOM_thickness_diffuse ===</span>
<span id="L910">KHTH = 0.0                      !   [m2 s-1] default = 0.0</span>
<span id="L911">                                ! The background horizontal thickness diffusivity.</span>
<span id="L912">READ_KHTH = False               !   [Boolean] default = False</span>
<span id="L913">                                ! If true, read a file (given by KHTH_FILE) containing the spatially varying</span>
<span id="L914">                                ! horizontal isopycnal height diffusivity.</span>
<span id="L915">KHTH_MIN = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L916">                                ! The minimum horizontal thickness diffusivity.</span>
<span id="L917">KHTH_MAX = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L918">                                ! The maximum horizontal thickness diffusivity.</span>
<span id="L919">KHTH_MAX_CFL = 0.8              !   [nondimensional] default = 0.8</span>
<span id="L920">                                ! The maximum value of the local diffusive CFL ratio that is permitted for the</span>
<span id="L921">                                ! thickness diffusivity. 1.0 is the marginally unstable value in a pure layered</span>
<span id="L922">                                ! model, but much smaller numbers (e.g. 0.1) seem to work better for ALE-based</span>
<span id="L923">                                ! models.</span>
<span id="L924">KH_ETA_CONST = 0.0              !   [m2 s-1] default = 0.0</span>
<span id="L925">                                ! The background horizontal diffusivity of the interface heights (without</span>
<span id="L926">                                ! considering the layer density structure).  If diffusive CFL limits are</span>
<span id="L927">                                ! encountered, the diffusivities of the isopycnals and the interfaces heights</span>
<span id="L928">                                ! are scaled back proportionately.</span>
<span id="L929">KH_ETA_VEL_SCALE = 0.0          !   [m s-1] default = 0.0</span>
<span id="L930">                                ! A velocity scale that is multiplied by the grid spacing to give a contribution</span>
<span id="L931">                                ! to the horizontal diffusivity of the interface heights (without considering</span>
<span id="L932">                                ! the layer density structure).</span>
<span id="L933">DETANGLE_INTERFACES = False     !   [Boolean] default = False</span>
<span id="L934">                                ! If defined add 3-d structured enhanced interface height diffusivities to</span>
<span id="L935">                                ! horizontally smooth jagged layers.</span>
<span id="L936">KHTH_SLOPE_MAX = 0.01           !   [nondim] default = 0.01</span>
<span id="L937">                                ! A slope beyond which the calculated isopycnal slope is not reliable and is</span>
<span id="L938">                                ! scaled away.</span>
<span id="L939">KHTH_USE_FGNV_STREAMFUNCTION = False !   [Boolean] default = False</span>
<span id="L940">                                ! If true, use the streamfunction formulation of Ferrari et al., 2010, which</span>
<span id="L941">                                ! effectively emphasizes graver vertical modes by smoothing in the vertical.</span>
<span id="L942">USE_STANLEY_GM = False          !   [Boolean] default = False</span>
<span id="L943">                                ! If true, turn on Stanley SGS T variance parameterization in GM code.</span>
<span id="L944">MEKE_GM_SRC_ALT = False         !   [Boolean] default = False</span>
<span id="L945">                                ! If true, use the GM energy conversion form S^2*N^2*kappa rather than the</span>
<span id="L946">                                ! streamfunction for the GM source term.</span>
<span id="L947">MEKE_GEOMETRIC = False          !   [Boolean] default = False</span>
<span id="L948">                                ! If true, uses the GM coefficient formulation from the GEOMETRIC framework</span>
<span id="L949">                                ! (Marshall et al., 2012).</span>
<span id="L950">USE_GME = False                 !   [Boolean] default = False</span>
<span id="L951">                                ! If true, use the GM+E backscatter scheme in association with the Gent and</span>
<span id="L952">                                ! McWilliams parameterization.</span>
<span id="L953">USE_GM_WORK_BUG = False         !   [Boolean] default = False</span>
<span id="L954">                                ! If true, compute the top-layer work tendency on the u-grid with the incorrect</span>
<span id="L955">                                ! sign, for legacy reproducibility.</span>
<span id="L956">STOCH_EOS = False               !   [Boolean] default = False</span>
<span id="L957">                                ! If true, stochastic perturbations are applied to the EOS in the PGF.</span>
<span id="L958">STANLEY_COEFF = -1.0            !   [nondim] default = -1.0</span>
<span id="L959">                                ! Coefficient correlating the temperature gradient and SGS T variance.</span>
<span id="L960"></span>
<span id="L961">! === module MOM_dynamics_unsplit ===</span>
<span id="L962">UNSPLIT_DT_VISC_BUG = False     !   [Boolean] default = False</span>
<span id="L963">                                ! If false, use the correct timestep in the viscous terms applied in the first</span>
<span id="L964">                                ! predictor step with the unsplit time stepping scheme, and in the calculation</span>
<span id="L965">                                ! of the turbulent mixed layer properties for viscosity with unsplit or</span>
<span id="L966">                                ! unsplit_RK2.  If true, an older incorrect value is used.</span>
<span id="L967">TIDES = False                   !   [Boolean] default = False</span>
<span id="L968">                                ! If true, apply tidal momentum forcing.</span>
<span id="L969">CALCULATE_SAL = False           !   [Boolean] default = False</span>
<span id="L970">                                ! If true, calculate self-attraction and loading.</span>
<span id="L971"></span>
<span id="L972">! === module MOM_continuity_PPM ===</span>
<span id="L973">MONOTONIC_CONTINUITY = False    !   [Boolean] default = False</span>
<span id="L974">                                ! If true, CONTINUITY_PPM uses the Colella and Woodward monotonic limiter.  The</span>
<span id="L975">                                ! default (false) is to use a simple positive definite limiter.</span>
<span id="L976">SIMPLE_2ND_PPM_CONTINUITY = False !   [Boolean] default = False</span>
<span id="L977">                                ! If true, CONTINUITY_PPM uses a simple 2nd order (arithmetic mean)</span>
<span id="L978">                                ! interpolation of the edge values. This may give better PV conservation</span>
<span id="L979">                                ! properties. While it formally reduces the accuracy of the continuity solver</span>
<span id="L980">                                ! itself in the strongly advective limit, it does not reduce the overall order</span>
<span id="L981">                                ! of accuracy of the dynamic core.</span>
<span id="L982">UPWIND_1ST_CONTINUITY = True    !   [Boolean] default = False</span>
<span id="L983">                                ! If true, CONTINUITY_PPM becomes a 1st-order upwind continuity solver.  This</span>
<span id="L984">                                ! scheme is highly diffusive but may be useful for debugging or in single-column</span>
<span id="L985">                                ! mode where its minimal stencil is useful.</span>
<span id="L986">ETA_TOLERANCE = 1.0E-06         !   [m] default = 2.0E-08</span>
<span id="L987">                                ! The tolerance for the differences between the barotropic and baroclinic</span>
<span id="L988">                                ! estimates of the sea surface height due to the fluxes through each face.  The</span>
<span id="L989">                                ! total tolerance for SSH is 4 times this value.  The default is</span>
<span id="L990">                                ! 0.5*NK*ANGSTROM, and this should not be set less than about</span>
<span id="L991">                                ! 10^-15*MAXIMUM_DEPTH.</span>
<span id="L992">VELOCITY_TOLERANCE = 3.0E+08    !   [m s-1] default = 3.0E+08</span>
<span id="L993">                                ! The tolerance for barotropic velocity discrepancies between the barotropic</span>
<span id="L994">                                ! solution and  the sum of the layer thicknesses.</span>
<span id="L995">CONT_PPM_AGGRESS_ADJUST = False !   [Boolean] default = False</span>
<span id="L996">                                ! If true, allow the adjusted velocities to have a relative CFL change up to</span>
<span id="L997">                                ! 0.5.</span>
<span id="L998">CONT_PPM_VOLUME_BASED_CFL = False !   [Boolean] default = False</span>
<span id="L999">                                ! If true, use the ratio of the open face lengths to the tracer cell areas when</span>
<span id="L1000">                                ! estimating CFL numbers.  The default is set by CONT_PPM_AGGRESS_ADJUST.</span>
<span id="L1001">CONTINUITY_CFL_LIMIT = 0.5      !   [nondim] default = 0.5</span>
<span id="L1002">                                ! The maximum CFL of the adjusted velocities.</span>
<span id="L1003">CONT_PPM_BETTER_ITER = True     !   [Boolean] default = True</span>
<span id="L1004">                                ! If true, stop corrective iterations using a velocity based criterion and only</span>
<span id="L1005">                                ! stop if the iteration is better than all predecessors.</span>
<span id="L1006">CONT_PPM_USE_VISC_REM_MAX = True !   [Boolean] default = True</span>
<span id="L1007">                                ! If true, use more appropriate limiting bounds for corrections in strongly</span>
<span id="L1008">                                ! viscous columns.</span>
<span id="L1009">CONT_PPM_MARGINAL_FACE_AREAS = True !   [Boolean] default = True</span>
<span id="L1010">                                ! If true, use the marginal face areas from the continuity solver for use as the</span>
<span id="L1011">                                ! weights in the barotropic solver. Otherwise use the transport averaged areas.</span>
<span id="L1012"></span>
<span id="L1013">! === module MOM_CoriolisAdv ===</span>
<span id="L1014">NOSLIP = False                  !   [Boolean] default = False</span>
<span id="L1015">                                ! If true, no slip boundary conditions are used; otherwise free slip boundary</span>
<span id="L1016">                                ! conditions are assumed. The implementation of the free slip BCs on a C-grid is</span>
<span id="L1017">                                ! much cleaner than the no slip BCs. The use of free slip BCs is strongly</span>
<span id="L1018">                                ! encouraged, and no slip BCs are not used with the biharmonic viscosity.</span>
<span id="L1019">CORIOLIS_EN_DIS = True          !   [Boolean] default = False</span>
<span id="L1020">                                ! If true, two estimates of the thickness fluxes are used to estimate the</span>
<span id="L1021">                                ! Coriolis term, and the one that dissipates energy relative to the other one is</span>
<span id="L1022">                                ! used.</span>
<span id="L1023">CORIOLIS_SCHEME = &quot;SADOURNY75_ENERGY&quot; ! default = &quot;SADOURNY75_ENERGY&quot;</span>
<span id="L1024">                                ! CORIOLIS_SCHEME selects the discretization for the Coriolis terms. Valid</span>
<span id="L1025">                                ! values are:</span>
<span id="L1026">                                !    SADOURNY75_ENERGY - Sadourny, 1975; energy cons.</span>
<span id="L1027">                                !    ARAKAWA_HSU90     - Arakawa &amp; Hsu, 1990</span>
<span id="L1028">                                !    SADOURNY75_ENSTRO - Sadourny, 1975; enstrophy cons.</span>
<span id="L1029">                                !    ARAKAWA_LAMB81    - Arakawa &amp; Lamb, 1981; En. + Enst.</span>
<span id="L1030">                                !    ARAKAWA_LAMB_BLEND - A blend of Arakawa &amp; Lamb with</span>
<span id="L1031">                                !                         Arakawa &amp; Hsu and Sadourny energy</span>
<span id="L1032">                                !    WENOVI5TH_PV_ENSTRO   - 5th-order WENO PV enstrophy</span>
<span id="L1033">                                !    WENOVI3RD_PV_ENSTRO   - 3rd-order WENO PV enstrophy</span>
<span id="L1034">                                !    WENOVI7TH_PV_ENSTRO  - 7th-order WENO PV enstrophy</span>
<span id="L1035">BOUND_CORIOLIS = True           !   [Boolean] default = False</span>
<span id="L1036">                                ! If true, the Coriolis terms at u-points are bounded by the four estimates of</span>
<span id="L1037">                                ! (f+rv)v from the four neighboring v-points, and similarly at v-points.  This</span>
<span id="L1038">                                ! option is always effectively false with CORIOLIS_EN_DIS defined and</span>
<span id="L1039">                                ! CORIOLIS_SCHEME set to SADOURNY75_ENERGY.</span>
<span id="L1040">KE_SCHEME = &quot;KE_ARAKAWA&quot;        ! default = &quot;KE_ARAKAWA&quot;</span>
<span id="L1041">                                ! KE_SCHEME selects the discretization for acceleration due to the kinetic</span>
<span id="L1042">                                ! energy gradient. Valid values are:</span>
<span id="L1043">                                !    KE_ARAKAWA, KE_SIMPLE_GUDONOV, KE_GUDONOV, KE_UP3</span>
<span id="L1044">PV_ADV_SCHEME = &quot;PV_ADV_CENTERED&quot; ! default = &quot;PV_ADV_CENTERED&quot;</span>
<span id="L1045">                                ! PV_ADV_SCHEME selects the discretization for PV advection. Valid values are:</span>
<span id="L1046">                                !    PV_ADV_CENTERED - centered (aka Sadourny, 75)</span>
<span id="L1047">                                !    PV_ADV_UPWIND1  - upwind, first order</span>
<span id="L1048"></span>
<span id="L1049">! === module MOM_PressureForce ===</span>
<span id="L1050">ANALYTIC_FV_PGF = True          !   [Boolean] default = True</span>
<span id="L1051">                                ! If true the pressure gradient forces are calculated with a finite volume form</span>
<span id="L1052">                                ! that analytically integrates the equations of state in pressure to avoid any</span>
<span id="L1053">                                ! possibility of numerical thermobaric instability, as described in Adcroft et</span>
<span id="L1054">                                ! al., O. Mod. (2008).</span>
<span id="L1055"></span>
<span id="L1056">! === module MOM_PressureForce_FV ===</span>
<span id="L1057">RHO_PGF_REF = 1000.0            !   [kg m-3] default = 1000.0</span>
<span id="L1058">                                ! The reference density that is subtracted off when calculating pressure</span>
<span id="L1059">                                ! gradient forces.  Its inverse is subtracted off of specific volumes when in</span>
<span id="L1060">                                ! non-Boussinesq mode.  The default is RHO_0.</span>
<span id="L1061">RHO_PGF_REF_BUG = True          !   [Boolean] default = True</span>
<span id="L1062">                                ! If true, recover a bug that RHO_0 (the mean seawater density in Boussinesq</span>
<span id="L1063">                                ! mode) and RHO_PGF_REF (the subtracted reference density in finite volume</span>
<span id="L1064">                                ! pressure gradient forces) are incorrectly interchanged in several instances in</span>
<span id="L1065">                                ! Boussinesq mode.</span>
<span id="L1066">SSH_IN_EOS_PRESSURE_FOR_PGF = False !   [Boolean] default = False</span>
<span id="L1067">                                ! If true, include contributions from the sea surface height in the height-based</span>
<span id="L1068">                                ! pressure used in the equation of state calculations for the Boussinesq</span>
<span id="L1069">                                ! pressure gradient forces, including adjustments for atmospheric or sea-ice</span>
<span id="L1070">                                ! pressure.</span>
<span id="L1071">MASS_WEIGHT_IN_PRESSURE_GRADIENT = False !   [Boolean] default = False</span>
<span id="L1072">                                ! If true, use mass weighting when interpolating T/S for integrals near the</span>
<span id="L1073">                                ! bathymetry in FV pressure gradient calculations.</span>
<span id="L1074">MASS_WEIGHT_IN_PRESSURE_GRADIENT_TOP = False !   [Boolean] default = False</span>
<span id="L1075">                                ! If true and MASS_WEIGHT_IN_PRESSURE_GRADIENT is true, use mass weighting when</span>
<span id="L1076">                                ! interpolating T/S for integrals near the top of the water column in FV</span>
<span id="L1077">                                ! pressure gradient calculations.</span>
<span id="L1078">MASS_WEIGHT_IN_PGF_VANISHED_ONLY = False !   [Boolean] default = False</span>
<span id="L1079">                                ! If true, use mass weighting when interpolating T/S for integrals only if one</span>
<span id="L1080">                                ! side is vanished according to RESET_INTXPA_H_NONVANISHED.</span>
<span id="L1081">CORRECTION_INTXPA = False       !   [Boolean] default = False</span>
<span id="L1082">                                ! If true, use a correction for surface pressure curvature in intx_pa.</span>
<span id="L1083">RESET_INTXPA_INTEGRAL = False   !   [Boolean] default = False</span>
<span id="L1084">                                ! If true, reset INTXPA to match pressures at first nonvanished cell. Includes</span>
<span id="L1085">                                ! pressure correction.</span>
<span id="L1086">RESET_INTXPA_INTEGRAL_FLATTEST = False !   [Boolean] default = False</span>
<span id="L1087">                                ! If true, use flattest interface as reference interface where there is no</span>
<span id="L1088">                                ! better choice for RESET_INTXPA_INTEGRAL. Otherwise, use surface interface.</span>
<span id="L1089">USE_INACCURATE_PGF_RHO_ANOM = False !   [Boolean] default = False</span>
<span id="L1090">                                ! If true, use a form of the PGF that uses the reference density in an</span>
<span id="L1091">                                ! inaccurate way. This is not recommended.</span>
<span id="L1092">RECONSTRUCT_FOR_PRESSURE = True !   [Boolean] default = True</span>
<span id="L1093">                                ! If True, use vertical reconstruction of T &amp; S within the integrals of the FV</span>
<span id="L1094">                                ! pressure gradient calculation. If False, use the constant-by-layer algorithm.</span>
<span id="L1095">                                ! The default is set by USE_REGRIDDING.</span>
<span id="L1096">PRESSURE_RECONSTRUCTION_SCHEME = 1 ! default = 1</span>
<span id="L1097">                                ! Order of vertical reconstruction of T/S to use in the integrals within the FV</span>
<span id="L1098">                                ! pressure gradient calculation.</span>
<span id="L1099">                                !  0: PCM or no reconstruction.</span>
<span id="L1100">                                !  1: PLM reconstruction.</span>
<span id="L1101">                                !  2: PPM reconstruction.</span>
<span id="L1102">BOUNDARY_EXTRAPOLATION_PRESSURE = True !   [Boolean] default = True</span>
<span id="L1103">                                ! If true, the reconstruction of T &amp; S for pressure in boundary cells is</span>
<span id="L1104">                                ! extrapolated, rather than using PCM in these cells. If true, the same order</span>
<span id="L1105">                                ! polynomial is used as is used for the interior cells.</span>
<span id="L1106">USE_STANLEY_PGF = False         !   [Boolean] default = False</span>
<span id="L1107">                                ! If true, turn on Stanley SGS T variance parameterization in PGF code.</span>
<span id="L1108"></span>
<span id="L1109">! === module MOM_Zanna_Bolton ===</span>
<span id="L1110">USE_ZB2020 = False              !   [Boolean] default = False</span>
<span id="L1111">                                ! If true, turns on Zanna-Bolton-2020 (ZB) subgrid momentum parameterization of</span>
<span id="L1112">                                ! mesoscale eddies.</span>
<span id="L1113"></span>
<span id="L1114">! === module MOM_hor_visc ===</span>
<span id="L1115">USE_CIRCULATION_IN_HORVISC = False !   [Boolean] default = False</span>
<span id="L1116">                                ! Use circulation theorem to compute vorticity in horvisc module (for ZB20 or</span>
<span id="L1117">                                ! Leith)</span>
<span id="L1118">USE_CONT_THICKNESS = False      !   [Boolean] default = False</span>
<span id="L1119">                                ! If true, use thickness at velocity points from continuity solver. This option</span>
<span id="L1120">                                ! currently only works with split mode.</span>
<span id="L1121">LAPLACIAN = False               !   [Boolean] default = False</span>
<span id="L1122">                                ! If true, use a Laplacian horizontal viscosity.</span>
<span id="L1123">BIHARMONIC = False              !   [Boolean] default = True</span>
<span id="L1124">                                ! If true, use a biharmonic horizontal viscosity. BIHARMONIC may be used with</span>
<span id="L1125">                                ! LAPLACIAN.</span>
<span id="L1126">USE_LEITHY = False              !   [Boolean] default = False</span>
<span id="L1127">                                ! If true, use a biharmonic Leith nonlinear eddy viscosity together with a</span>
<span id="L1128">                                ! harmonic backscatter.</span>
<span id="L1129">USE_LAND_MASK_FOR_HVISC = True  !   [Boolean] default = True</span>
<span id="L1130">                                ! If true, use the land mask for the computation of thicknesses at velocity</span>
<span id="L1131">                                ! locations. This eliminates the dependence on arbitrary values over land or</span>
<span id="L1132">                                ! outside of the domain.</span>
<span id="L1133">FRICTWORK_BUG = False           !   [Boolean] default = False</span>
<span id="L1134">                                ! If true, retain an answer-changing bug in calculating the FrictWork, which</span>
<span id="L1135">                                ! cancels the h in thickness flux and the h at velocity point. This isnot</span>
<span id="L1136">                                ! recommended.</span>
<span id="L1137"></span>
<span id="L1138">! === module MOM_vert_friction ===</span>
<span id="L1139">VERT_FRICTION_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1140">                                ! The vintage of the order of arithmetic and expressions in the viscous</span>
<span id="L1141">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L1142">                                ! while higher values use expressions that do not use an arbitrary hard-coded</span>
<span id="L1143">                                ! maximum viscous coupling coefficient between layers.  Values below 20230601</span>
<span id="L1144">                                ! recover a form of the viscosity within the mixed layer that breaks up the</span>
<span id="L1145">                                ! magnitude of the wind stress in some non-Boussinesq cases.</span>
<span id="L1146">DIRECT_STRESS = False           !   [Boolean] default = False</span>
<span id="L1147">                                ! If true, the wind stress is distributed over the topmost HMIX_STRESS of fluid</span>
<span id="L1148">                                ! (like in HYCOM), and an added mixed layer viscosity or a physically based</span>
<span id="L1149">                                ! boundary layer turbulence parameterization is not needed for stability.</span>
<span id="L1150">FIXED_DEPTH_LOTW_ML = False     !   [Boolean] default = False</span>
<span id="L1151">                                ! If true, use a Law-of-the-wall prescription for the mixed layer viscosity</span>
<span id="L1152">                                ! within a boundary layer that is the lesser of HMIX_FIXED and the total depth</span>
<span id="L1153">                                ! of the ocean in a column.</span>
<span id="L1154">LOTW_VISCOUS_ML_FLOOR = False   !   [Boolean] default = False</span>
<span id="L1155">                                ! If true, use a Law-of-the-wall prescription to set a lower bound on the</span>
<span id="L1156">                                ! viscous coupling between layers within the surface boundary layer, based the</span>
<span id="L1157">                                ! distance of interfaces from the surface.  This only acts when there are large</span>
<span id="L1158">                                ! changes in the thicknesses of successive layers or when the viscosity is set</span>
<span id="L1159">                                ! externally and the wind stress has subsequently increased.</span>
<span id="L1160">VON_KARMAN_CONST = 0.41         !   [nondim] default = 0.41</span>
<span id="L1161">                                ! The value the von Karman constant as used for mixed layer viscosity.</span>
<span id="L1162">HARMONIC_VISC = True            !   [Boolean] default = False</span>
<span id="L1163">                                ! If true, use the harmonic mean thicknesses for calculating the vertical</span>
<span id="L1164">                                ! viscosity.</span>
<span id="L1165">HARMONIC_BL_SCALE = 0.0         !   [nondim] default = 0.0</span>
<span id="L1166">                                ! A scale to determine when water is in the boundary layers based solely on</span>
<span id="L1167">                                ! harmonic mean thicknesses for the purpose of determining the extent to which</span>
<span id="L1168">                                ! the thicknesses used in the viscosities are upwinded.</span>
<span id="L1169">HMIX_FIXED = 0.01               !   [m]</span>
<span id="L1170">                                ! The prescribed depth over which the near-surface viscosity and diffusivity are</span>
<span id="L1171">                                ! elevated when the bulk mixed layer is not used.</span>
<span id="L1172">USE_GL90_IN_SSW = False         !   [Boolean] default = False</span>
<span id="L1173">                                ! If true, use simpler method to calculate 1/N^2 in GL90 vertical viscosity</span>
<span id="L1174">                                ! coefficient. This method is valid in stacked shallow water mode.</span>
<span id="L1175">KV_ML_INVZ2 = 0.0               !   [m2 s-1] default = 0.0</span>
<span id="L1176">                                ! An extra kinematic viscosity in a mixed layer of thickness HMIX_FIXED, with</span>
<span id="L1177">                                ! the actual viscosity scaling as 1/(z*HMIX_FIXED)^2, where z is the distance</span>
<span id="L1178">                                ! from the surface, to allow for finite wind stresses to be transmitted through</span>
<span id="L1179">                                ! infinitesimally thin surface layers.  This is an older option for numerical</span>
<span id="L1180">                                ! convenience without a strong physical basis, and its use is now discouraged.</span>
<span id="L1181">CFL_TRUNCATE = 0.5              !   [nondim] default = 0.5</span>
<span id="L1182">                                ! The value of the CFL number that will cause velocity components to be</span>
<span id="L1183">                                ! truncated; instability can occur past 0.5.</span>
<span id="L1184">CFL_REPORT = 0.5                !   [nondim] default = 0.5</span>
<span id="L1185">                                ! The value of the CFL number that causes accelerations to be reported; the</span>
<span id="L1186">                                ! default is CFL_TRUNCATE.</span>
<span id="L1187">CFL_TRUNCATE_RAMP_TIME = 0.0    !   [s] default = 0.0</span>
<span id="L1188">                                ! The time over which the CFL truncation value is ramped up at the beginning of</span>
<span id="L1189">                                ! the run.</span>
<span id="L1190">CFL_TRUNCATE_START = 0.0        !   [nondim] default = 0.0</span>
<span id="L1191">                                ! The start value of the truncation CFL number used when ramping up CFL_TRUNC.</span>
<span id="L1192">STOKES_MIXING_COMBINED = False  !   [Boolean] default = False</span>
<span id="L1193">                                ! Flag to use Stokes drift Mixing via the Lagrangian  current (Eulerian plus</span>
<span id="L1194">                                ! Stokes drift).  Still needs work and testing, so not recommended for use.</span>
<span id="L1195">VEL_UNDERFLOW = 1.0E-30         !   [m s-1] default = 0.0</span>
<span id="L1196">                                ! A negligibly small velocity magnitude below which velocity components are set</span>
<span id="L1197">                                ! to 0.  A reasonable value might be 1e-30 m/s, which is less than an Angstrom</span>
<span id="L1198">                                ! divided by the age of the universe.</span>
<span id="L1199"></span>
<span id="L1200">! === module MOM_mixed_layer_restrat ===</span>
<span id="L1201">MIXEDLAYER_RESTRAT = False      !   [Boolean] default = False</span>
<span id="L1202">                                ! If true, a density-gradient dependent re-stratifying flow is imposed in the</span>
<span id="L1203">                                ! mixed layer. Can be used in ALE mode without restriction but in layer mode can</span>
<span id="L1204">                                ! only be used if BULKMIXEDLAYER is true.</span>
<span id="L1205"></span>
<span id="L1206">! === module MOM_diagnostics ===</span>
<span id="L1207">DIAG_EBT_MONO_N2_COLUMN_FRACTION = 0.0 !   [nondim] default = 0.0</span>
<span id="L1208">                                ! The lower fraction of water column over which N2 is limited as monotonic for</span>
<span id="L1209">                                ! the purposes of calculating the equivalent barotropic wave speed.</span>
<span id="L1210">DIAG_EBT_MONO_N2_DEPTH = -1.0   !   [m] default = -1.0</span>
<span id="L1211">                                ! The depth below which N2 is limited as monotonic for the purposes of</span>
<span id="L1212">                                ! calculating the equivalent barotropic wave speed.</span>
<span id="L1213">INTERNAL_WAVE_SPEED_TOL = 0.001 !   [nondim] default = 0.001</span>
<span id="L1214">                                ! The fractional tolerance for finding the wave speeds.</span>
<span id="L1215">INTERNAL_WAVE_SPEED_MIN = 0.0   !   [m s-1] default = 0.0</span>
<span id="L1216">                                ! A floor in the first mode speed below which 0 used instead.</span>
<span id="L1217">INTERNAL_WAVE_SPEED_BETTER_EST = True !   [Boolean] default = True</span>
<span id="L1218">                                ! If true, use a more robust estimate of the first mode wave speed as the</span>
<span id="L1219">                                ! starting point for iterations.</span>
<span id="L1220">INTWAVE_REMAPPING_USE_OM4_SUBCELLS = True !   [Boolean] default = True</span>
<span id="L1221">                                ! If true, use the OM4 remapping-via-subcells algorithm for calculating EBT</span>
<span id="L1222">                                ! structure. See REMAPPING_USE_OM4_SUBCELLS for details. We recommend setting</span>
<span id="L1223">                                ! this option to false.</span>
<span id="L1224"></span>
<span id="L1225">! === module MOM_diabatic_driver ===</span>
<span id="L1226">! The following parameters are used for diabatic processes.</span>
<span id="L1227">USE_LEGACY_DIABATIC_DRIVER = True !   [Boolean] default = True</span>
<span id="L1228">                                ! If true, use a legacy version of the diabatic subroutine. This is temporary</span>
<span id="L1229">                                ! and is needed to avoid change in answers.</span>
<span id="L1230">ENERGETICS_SFC_PBL = False      !   [Boolean] default = False</span>
<span id="L1231">                                ! If true, use an implied energetics planetary boundary layer scheme to</span>
<span id="L1232">                                ! determine the diffusivity and viscosity in the surface boundary layer.</span>
<span id="L1233">EPBL_IS_ADDITIVE = True         !   [Boolean] default = True</span>
<span id="L1234">                                ! If true, the diffusivity from ePBL is added to all other diffusivities.</span>
<span id="L1235">                                ! Otherwise, the larger of kappa-shear and ePBL diffusivities are used.</span>
<span id="L1236">INTERNAL_TIDES = False          !   [Boolean] default = False</span>
<span id="L1237">                                ! If true, use the code that advances a separate set of equations for the</span>
<span id="L1238">                                ! internal tide energy density.</span>
<span id="L1239">MASSLESS_MATCH_TARGETS = True   !   [Boolean] default = True</span>
<span id="L1240">                                ! If true, the temperature and salinity of massless layers are kept consistent</span>
<span id="L1241">                                ! with their target densities. Otherwise the properties of massless layers</span>
<span id="L1242">                                ! evolve diffusively to match massive neighboring layers.</span>
<span id="L1243">AGGREGATE_FW_FORCING = True     !   [Boolean] default = True</span>
<span id="L1244">                                ! If true, the net incoming and outgoing fresh water fluxes are combined and</span>
<span id="L1245">                                ! applied as either incoming or outgoing depending on the sign of the net. If</span>
<span id="L1246">                                ! false, the net incoming fresh water flux is added to the model and thereafter</span>
<span id="L1247">                                ! the net outgoing is removed from the topmost non-vanished layers of the</span>
<span id="L1248">                                ! updated state.</span>
<span id="L1249">MIX_BOUNDARY_TRACERS = True     !   [Boolean] default = True</span>
<span id="L1250">                                ! If true, mix the passive tracers in massless layers at the bottom into the</span>
<span id="L1251">                                ! interior as though a diffusivity of KD_MIN_TR were operating.</span>
<span id="L1252">MIX_BOUNDARY_TRACER_ALE = False !   [Boolean] default = False</span>
<span id="L1253">                                ! If true and in ALE mode, mix the passive tracers in massless layers at the</span>
<span id="L1254">                                ! bottom into the interior as though a diffusivity of KD_MIN_TR were operating.</span>
<span id="L1255">KD_MIN_TR = 0.0                 !   [m2 s-1] default = 0.0</span>
<span id="L1256">                                ! A minimal diffusivity that should always be applied to tracers, especially in</span>
<span id="L1257">                                ! massless layers near the bottom. The default is 0.1*KD.</span>
<span id="L1258">KD_BBL_TR = 0.0                 !   [m2 s-1] default = 0.0</span>
<span id="L1259">                                ! A bottom boundary layer tracer diffusivity that will allow for explicitly</span>
<span id="L1260">                                ! specified bottom fluxes. The entrainment at the bottom is at least</span>
<span id="L1261">                                ! sqrt(Kd_BBL_tr*dt) over the same distance.</span>
<span id="L1262">TRACER_TRIDIAG = False          !   [Boolean] default = False</span>
<span id="L1263">                                ! If true, use the passive tracer tridiagonal solver for T and S</span>
<span id="L1264">MINIMUM_FORCING_DEPTH = 0.001   !   [m] default = 0.001</span>
<span id="L1265">                                ! The smallest depth over which forcing can be applied. This only takes effect</span>
<span id="L1266">                                ! when near-surface layers become thin relative to this scale, in which case the</span>
<span id="L1267">                                ! forcing tendencies scaled down by distributing the forcing over this depth</span>
<span id="L1268">                                ! scale.</span>
<span id="L1269">EVAP_CFL_LIMIT = 0.8            !   [nondim] default = 0.8</span>
<span id="L1270">                                ! The largest fraction of a layer than can be lost to forcing (e.g. evaporation,</span>
<span id="L1271">                                ! sea-ice formation) in one time-step. The unused mass loss is passed down</span>
<span id="L1272">                                ! through the column.</span>
<span id="L1273">MLD_EN_VALS = 25.0, 2500.0, 2.5E+05 !   [J/m2] default = 25.0, 2500.0, 2.5E+05</span>
<span id="L1274">                                ! The energy values used to compute MLDs.  If not set (or all set to 0.), the</span>
<span id="L1275">                                ! default will overwrite to 25., 2500., 250000.</span>
<span id="L1276">BMLD_EN_VALS = 25.0, 2500.0, 2.5E+05 !   [J/m2] default = 25.0, 2500.0, 2.5E+05</span>
<span id="L1277">                                ! The energy values used to compute Bottom MLDs.  If not set (or all set to 0.),</span>
<span id="L1278">                                ! the default will overwrite to 25., 2500., 250000.</span>
<span id="L1279">HREF_FOR_MLD = 0.0              !   [m] default = 0.0</span>
<span id="L1280">                                ! Reference depth used to calculate the potential density used to find the mixed</span>
<span id="L1281">                                ! layer depth based on a delta rho = 0.03 kg/m3.</span>
<span id="L1282">DIAG_MLD_DENSITY_DIFF = 0.1     !   [kg/m3] default = 0.1</span>
<span id="L1283">                                ! The density difference used to determine a diagnostic mixed layer depth,</span>
<span id="L1284">                                ! MLD_user, following the definition of Levitus 1982. The MLD is the depth at</span>
<span id="L1285">                                ! which the density is larger than the surface density by the specified amount.</span>
<span id="L1286">DIAG_DEPTH_SUBML_N2 = 50.0      !   [m] default = 50.0</span>
<span id="L1287">                                ! The distance over which to calculate a diagnostic of the stratification at the</span>
<span id="L1288">                                ! base of the mixed layer.</span>
<span id="L1289"></span>
<span id="L1290">! === module MOM_CVMix_KPP ===</span>
<span id="L1291">! This is the MOM wrapper to CVMix:KPP</span>
<span id="L1292">! See http://cvmix.github.io/</span>
<span id="L1293">USE_KPP = True                  !   [Boolean] default = False</span>
<span id="L1294">                                ! If true, turns on the [CVMix] KPP scheme of Large et al., 1994, to calculate</span>
<span id="L1295">                                ! diffusivities and non-local transport in the OBL.</span>
<span id="L1296">KPP%</span>
<span id="L1297">PASSIVE = False                 !   [Boolean] default = False</span>
<span id="L1298">                                ! If True, puts KPP into a passive-diagnostic mode.</span>
<span id="L1299">APPLY_NONLOCAL_TRANSPORT = True !   [Boolean] default = True</span>
<span id="L1300">                                ! If True, applies the non-local transport to all tracers. If False, calculates</span>
<span id="L1301">                                ! the non-local transport and tendencies but purely for diagnostic purposes.</span>
<span id="L1302">N_SMOOTH = 0                    ! default = 0</span>
<span id="L1303">                                ! The number of times the 1-1-4-1-1 Laplacian filter is applied on OBL depth.</span>
<span id="L1304">RI_CRIT = 0.3                   !   [nondim] default = 0.3</span>
<span id="L1305">                                ! Critical bulk Richardson number used to define depth of the surface Ocean</span>
<span id="L1306">                                ! Boundary Layer (OBL).</span>
<span id="L1307">VON_KARMAN = 0.4                !   [nondim] default = 0.4</span>
<span id="L1308">                                ! von Karman constant.</span>
<span id="L1309">ENHANCE_DIFFUSION = True        !   [Boolean] default = True</span>
<span id="L1310">                                ! If True, adds enhanced diffusion at the based of the boundary layer.</span>
<span id="L1311">INTERP_TYPE = &quot;cubic&quot;           ! default = &quot;quadratic&quot;</span>
<span id="L1312">                                ! Type of interpolation to determine the OBL depth.</span>
<span id="L1313">                                ! Allowed types are: linear, quadratic, cubic.</span>
<span id="L1314">INTERP_TYPE2 = &quot;LMD94&quot;          ! default = &quot;LMD94&quot;</span>
<span id="L1315">                                ! Type of interpolation to compute diff and visc at OBL_depth.</span>
<span id="L1316">                                ! Allowed types are: linear, quadratic, cubic or LMD94.</span>
<span id="L1317">STOKES_MOST = False             !   [Boolean] default = False</span>
<span id="L1318">                                ! If True, use Stokes Similarity package.</span>
<span id="L1319">COMPUTE_EKMAN = False           !   [Boolean] default = False</span>
<span id="L1320">                                ! If True, limit OBL depth to be no deeper than Ekman depth.</span>
<span id="L1321">COMPUTE_MONIN_OBUKHOV = False   !   [Boolean] default = False</span>
<span id="L1322">                                ! If True, limit the OBL depth to be no deeper than Monin-Obukhov depth.</span>
<span id="L1323">CS = 98.96                      !   [nondim] default = 98.96</span>
<span id="L1324">                                ! Parameter for computing velocity scale function.</span>
<span id="L1325">CS2 = 6.32739901508             !   [nondim] default = 6.32739901508</span>
<span id="L1326">                                ! Parameter for computing non-local term.</span>
<span id="L1327">DEEP_OBL_OFFSET = 0.0           !   [m] default = 0.0</span>
<span id="L1328">                                ! If non-zero, the distance above the bottom to which the OBL is clipped if it</span>
<span id="L1329">                                ! would otherwise reach the bottom. The smaller of this and 0.1D is used.</span>
<span id="L1330">FIXED_OBLDEPTH = False          !   [Boolean] default = False</span>
<span id="L1331">                                ! If True, fix the OBL depth to FIXED_OBLDEPTH_VALUE rather than using the OBL</span>
<span id="L1332">                                ! depth from CVMix. This option is just for testing purposes.</span>
<span id="L1333">FIXED_OBLDEPTH_VALUE = 30.0     !   [m] default = 30.0</span>
<span id="L1334">                                ! Value for the fixed OBL depth when fixedOBLdepth==True. This parameter is for</span>
<span id="L1335">                                ! just for testing purposes. It will over-ride the OBLdepth computed from CVMix.</span>
<span id="L1336">SURF_LAYER_EXTENT = 0.1         !   [nondim] default = 0.1</span>
<span id="L1337">                                ! Fraction of OBL depth considered in the surface layer.</span>
<span id="L1338">MINIMUM_OBL_DEPTH = 0.0         !   [m] default = 0.0</span>
<span id="L1339">                                ! If non-zero, a minimum depth to use for KPP OBL depth. Independent of this</span>
<span id="L1340">                                ! parameter, the OBL depth is always at least as deep as the first layer.</span>
<span id="L1341">MINIMUM_VT2 = 1.0E-10           !   [m2/s2] default = 1.0E-10</span>
<span id="L1342">                                ! Min of the unresolved velocity Vt2 used in Rib CVMix calculation.</span>
<span id="L1343">                                ! Scaling: MINIMUM_VT2 = const1*d*N*ws, with d=1m, N=1e-5/s, ws=1e-6 m/s.</span>
<span id="L1344">NLT_SHAPE = &quot;CVMix&quot;             ! default = &quot;CVMix&quot;</span>
<span id="L1345">                                ! MOM6 method to set nonlocal transport profile. Over-rides the result from</span>
<span id="L1346">                                ! CVMix.  Allowed values are:</span>
<span id="L1347">                                !    CVMix     - Uses the profiles from CVMix specified by MATCH_TECHNIQUE</span>
<span id="L1348">                                !    LINEAR    - A linear profile, 1-sigma</span>
<span id="L1349">                                !    PARABOLIC - A parablic profile, (1-sigma)^2</span>
<span id="L1350">                                !    CUBIC     - A cubic profile, (1-sigma)^2(1+2*sigma)</span>
<span id="L1351">                                !    CUBIC_LMD - The original KPP profile</span>
<span id="L1352">MATCH_TECHNIQUE = &quot;SimpleShapes&quot; ! default = &quot;SimpleShapes&quot;</span>
<span id="L1353">                                ! CVMix method to set profile function for diffusivity and NLT, as well as</span>
<span id="L1354">                                ! matching across OBL base. Allowed values are:</span>
<span id="L1355">                                !    SimpleShapes      = sigma*(1-sigma)^2 for both diffusivity and NLT</span>
<span id="L1356">                                !    MatchGradient     = sigma*(1-sigma)^2 for NLT; diffusivity profile from</span>
<span id="L1357">                                !      matching</span>
<span id="L1358">                                !    MatchBoth         = match gradient for both diffusivity and NLT</span>
<span id="L1359">                                !    ParabolicNonLocal = sigma*(1-sigma)^2 for diffusivity; (1-sigma)^2 for NLT</span>
<span id="L1360">KPP_ZERO_DIFFUSIVITY = False    !   [Boolean] default = False</span>
<span id="L1361">                                ! If True, zeroes the KPP diffusivity and viscosity; for testing purpose.</span>
<span id="L1362">KPP_IS_ADDITIVE = True          !   [Boolean] default = True</span>
<span id="L1363">                                ! If true, adds KPP diffusivity to diffusivity from other schemes.</span>
<span id="L1364">                                ! If false, KPP is the only diffusivity wherever KPP is non-zero.</span>
<span id="L1365">KPP_SHORTWAVE_METHOD = &quot;MXL_SW&quot; ! default = &quot;MXL_SW&quot;</span>
<span id="L1366">                                ! Determines contribution of shortwave radiation to KPP surface buoyancy flux.</span>
<span id="L1367">                                ! Options include:</span>
<span id="L1368">                                !   ALL_SW: use total shortwave radiation</span>
<span id="L1369">                                !   MXL_SW: use shortwave radiation absorbed by mixing layer</span>
<span id="L1370">                                !   LV1_SW: use shortwave radiation absorbed by top model layer</span>
<span id="L1371">CVMix_ZERO_H_WORK_AROUND = 0.0  !   [m] default = 0.0</span>
<span id="L1372">                                ! A minimum thickness used to avoid division by small numbers in the vicinity of</span>
<span id="L1373">                                ! vanished layers. This is independent of MIN_THICKNESS used in other parts of</span>
<span id="L1374">                                ! MOM.</span>
<span id="L1375">USE_KPP_LT_K = False            !   [Boolean] default = False</span>
<span id="L1376">                                ! Flag for Langmuir turbulence enhancement of turbulentmixing coefficient.</span>
<span id="L1377">STOKES_MIXING = False           !   [Boolean] default = False</span>
<span id="L1378">                                ! Flag for Langmuir turbulence enhancement of turbulentmixing coefficient.</span>
<span id="L1379">USE_KPP_LT_VT2 = False          !   [Boolean] default = False</span>
<span id="L1380">                                ! Flag for Langmuir turbulence enhancement of Vt2in Bulk Richardson Number.</span>
<span id="L1381">KPP_CVt2 = 1.6                  !   [nondim] default = 1.6</span>
<span id="L1382">                                ! Parameter for Stokes MOST convection entrainment</span>
<span id="L1383">ANSWER_DATE = 20251231          ! default = 99991231</span>
<span id="L1384">                                ! The vintage of the order of arithmetic in the CVMix KPP calculations.  Values</span>
<span id="L1385">                                ! below 20240501 recover the answers from early in 2024, while higher values use</span>
<span id="L1386">                                ! expressions that have been refactored for rotational symmetry.</span>
<span id="L1387">%KPP</span>
<span id="L1388"></span>
<span id="L1389">! === module MOM_CVMix_conv ===</span>
<span id="L1390">! Parameterization of enhanced mixing due to convection via CVMix</span>
<span id="L1391">USE_CVMix_CONVECTION = False    !   [Boolean] default = False</span>
<span id="L1392">                                ! If true, turns on the enhanced mixing due to convection via CVMix. This scheme</span>
<span id="L1393">                                ! increases diapycnal diffs./viscs. at statically unstable interfaces. Relevant</span>
<span id="L1394">                                ! parameters are contained in the CVMix_CONVECTION% parameter block.</span>
<span id="L1395"></span>
<span id="L1396">! === module MOM_set_diffusivity ===</span>
<span id="L1397">FLUX_RI_MAX = 0.2               !   [nondim] default = 0.2</span>
<span id="L1398">                                ! The flux Richardson number where the stratification is large enough that N2 &gt;</span>
<span id="L1399">                                ! omega2.  The full expression for the Flux Richardson number is usually</span>
<span id="L1400">                                ! FLUX_RI_MAX*N2/(N2+OMEGA2).</span>
<span id="L1401">SET_DIFF_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1402">                                ! The vintage of the order of arithmetic and expressions in the set diffusivity</span>
<span id="L1403">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L1404">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L1405">                                ! Values above 20250301 also use less confusing expressions to set the</span>
<span id="L1406">                                ! bottom-drag generated diffusivity when USE_LOTW_BBL_DIFFUSIVITY is false.</span>
<span id="L1407"></span>
<span id="L1408">! === module MOM_tidal_mixing ===</span>
<span id="L1409">! Vertical Tidal Mixing Parameterization</span>
<span id="L1410">USE_CVMix_TIDAL = False         !   [Boolean] default = False</span>
<span id="L1411">                                ! If true, turns on tidal mixing via CVMix</span>
<span id="L1412">INT_TIDE_DISSIPATION = False    !   [Boolean] default = False</span>
<span id="L1413">                                ! If true, use an internal tidal dissipation scheme to drive diapycnal mixing,</span>
<span id="L1414">                                ! along the lines of St. Laurent et al. (2002) and Simmons et al. (2004).</span>
<span id="L1415">ML_RADIATION = False            !   [Boolean] default = False</span>
<span id="L1416">                                ! If true, allow a fraction of TKE available from wind work to penetrate below</span>
<span id="L1417">                                ! the base of the mixed layer with a vertical decay scale determined by the</span>
<span id="L1418">                                ! minimum of: (1) The depth of the mixed layer, (2) an Ekman length scale.</span>
<span id="L1419">BBL_EFFIC = 0.2                 !   [nondim] default = 0.2</span>
<span id="L1420">                                ! The efficiency with which the energy extracted by bottom drag drives BBL</span>
<span id="L1421">                                ! diffusion.  This is only used if BOTTOMDRAGLAW is true.</span>
<span id="L1422">BBL_MIXING_MAX_DECAY = 200.0    !   [m] default = 200.0</span>
<span id="L1423">                                ! The maximum decay scale for the BBL diffusion, or 0 to allow the mixing to</span>
<span id="L1424">                                ! penetrate as far as stratification and rotation permit.  The default for now</span>
<span id="L1425">                                ! is 200 m. This is only used if BOTTOMDRAGLAW is true.</span>
<span id="L1426">BBL_MIXING_AS_MAX = True        !   [Boolean] default = True</span>
<span id="L1427">                                ! If true, take the maximum of the diffusivity from the BBL mixing and the other</span>
<span id="L1428">                                ! diffusivities. Otherwise, diffusivity from the BBL_mixing is simply added.</span>
<span id="L1429">USE_LOTW_BBL_DIFFUSIVITY = False !   [Boolean] default = False</span>
<span id="L1430">                                ! If true, uses a simple, imprecise but non-coordinate dependent, model of BBL</span>
<span id="L1431">                                ! mixing diffusivity based on Law of the Wall. Otherwise, uses the original BBL</span>
<span id="L1432">                                ! scheme.</span>
<span id="L1433">DRAG_DIFFUSIVITY_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1434">                                ! The vintage of the order of arithmetic in the drag diffusivity calculations.</span>
<span id="L1435">                                ! Values above 20250301 use less confusing expressions to set the bottom-drag</span>
<span id="L1436">                                ! generated diffusivity when USE_LOTW_BBL_DIFFUSIVITY is false.</span>
<span id="L1437">DZ_BBL_AVG_MIN = 0.0            !   [m] default = 0.0</span>
<span id="L1438">                                ! A minimal distance over which to average to determine the average bottom</span>
<span id="L1439">                                ! boundary layer density.</span>
<span id="L1440">SIMPLE_TKE_TO_KD = False        !   [Boolean] default = False</span>
<span id="L1441">                                ! If true, uses a simple estimate of Kd/TKE that will work for arbitrary</span>
<span id="L1442">                                ! vertical coordinates. If false, calculates Kd/TKE and bounds based on exact</span>
<span id="L1443">                                ! energetics for an isopycnal layer-formulation.</span>
<span id="L1444"></span>
<span id="L1445">! === module MOM_bkgnd_mixing ===</span>
<span id="L1446">! Adding static vertical background mixing coefficients</span>
<span id="L1447">KD = 0.0                        !   [m2 s-1] default = 0.0</span>
<span id="L1448">                                ! The background diapycnal diffusivity of density in the interior. Zero or the</span>
<span id="L1449">                                ! molecular value, ~1e-7 m2 s-1, may be used.</span>
<span id="L1450">KD_MIN = 0.0                    !   [m2 s-1] default = 0.0</span>
<span id="L1451">                                ! The minimum diapycnal diffusivity.</span>
<span id="L1452">BRYAN_LEWIS_DIFFUSIVITY = False !   [Boolean] default = False</span>
<span id="L1453">                                ! If true, use a Bryan &amp; Lewis (JGR 1979) like tanh profile of background</span>
<span id="L1454">                                ! diapycnal diffusivity with depth. This is done via CVMix.</span>
<span id="L1455">HORIZ_VARYING_BACKGROUND = False !   [Boolean] default = False</span>
<span id="L1456">                                ! If true, apply vertically uniform, latitude-dependent background diffusivity,</span>
<span id="L1457">                                ! as described in Danabasoglu et al., 2012</span>
<span id="L1458">PRANDTL_BKGND = 1.0             !   [nondim] default = 1.0</span>
<span id="L1459">                                ! Turbulent Prandtl number used to convert vertical background diffusivities</span>
<span id="L1460">                                ! into viscosities.</span>
<span id="L1461">HENYEY_IGW_BACKGROUND = False   !   [Boolean] default = False</span>
<span id="L1462">                                ! If true, use a latitude-dependent scaling for the near surface background</span>
<span id="L1463">                                ! diffusivity, as described in Harrison &amp; Hallberg, JPO 2008.</span>
<span id="L1464">KD_TANH_LAT_FN = False          !   [Boolean] default = False</span>
<span id="L1465">                                ! If true, use a tanh dependence of Kd_sfc on latitude, like CM2.1/CM2M.  There</span>
<span id="L1466">                                ! is no physical justification for this form, and it can not be used with</span>
<span id="L1467">                                ! HENYEY_IGW_BACKGROUND.</span>
<span id="L1468">KD_MAX = -1.0                   !   [m2 s-1] default = -1.0</span>
<span id="L1469">                                ! The maximum permitted increment for the diapycnal diffusivity from TKE-based</span>
<span id="L1470">                                ! parameterizations, or a negative value for no limit.</span>
<span id="L1471">KD_ADD = 0.0                    !   [m2 s-1] default = 0.0</span>
<span id="L1472">                                ! A uniform diapycnal diffusivity that is added everywhere without any filtering</span>
<span id="L1473">                                ! or scaling.</span>
<span id="L1474">USER_CHANGE_DIFFUSIVITY = False !   [Boolean] default = False</span>
<span id="L1475">                                ! If true, call user-defined code to change the diffusivity.</span>
<span id="L1476">DISSIPATION_MIN = 0.0           !   [W m-3] default = 0.0</span>
<span id="L1477">                                ! The minimum dissipation by which to determine a lower bound of Kd (a floor).</span>
<span id="L1478">DISSIPATION_N0 = 0.0            !   [W m-3] default = 0.0</span>
<span id="L1479">                                ! The intercept when N=0 of the N-dependent expression used to set a minimum</span>
<span id="L1480">                                ! dissipation by which to determine a lower bound of Kd (a floor): A in eps_min</span>
<span id="L1481">                                ! = A + B*N.</span>
<span id="L1482">DISSIPATION_N1 = 0.0            !   [J m-3] default = 0.0</span>
<span id="L1483">                                ! The coefficient multiplying N, following Gargett, used to set a minimum</span>
<span id="L1484">                                ! dissipation by which to determine a lower bound of Kd (a floor): B in eps_min</span>
<span id="L1485">                                ! = A + B*N</span>
<span id="L1486">DISSIPATION_KD_MIN = 0.0        !   [m2 s-1] default = 0.0</span>
<span id="L1487">                                ! The minimum vertical diffusivity applied as a floor.</span>
<span id="L1488">DOUBLE_DIFFUSION = False        !   [Boolean] default = False</span>
<span id="L1489">                                ! If true, increase diffusivites for temperature or salinity based on the</span>
<span id="L1490">                                ! double-diffusive parameterization described in Large et al. (1994).</span>
<span id="L1491"></span>
<span id="L1492">! === module MOM_kappa_shear ===</span>
<span id="L1493">! Parameterization of shear-driven turbulence following Jackson, Hallberg and Legg, JPO 2008</span>
<span id="L1494">USE_JACKSON_PARAM = False       !   [Boolean] default = False</span>
<span id="L1495">                                ! If true, use the Jackson-Hallberg-Legg (JPO 2008) shear mixing</span>
<span id="L1496">                                ! parameterization.</span>
<span id="L1497">VERTEX_SHEAR_THICKNESS_MEAN = False !   [Boolean] default = False</span>
<span id="L1498">                                ! If true, apply thickness weighting to horizontal averagings of diffusivity to</span>
<span id="L1499">                                ! tracer points in the kappa shear solver.</span>
<span id="L1500">KD_SEED_KAPPA_SHEAR = 1.0       !   [m2 s-1] default = 1.0</span>
<span id="L1501">                                ! A moderately large seed value of diapycnal diffusivity that is used as a</span>
<span id="L1502">                                ! starting turbulent diffusivity in the iterations to find an energetically</span>
<span id="L1503">                                ! constrained solution for the shear-driven diffusivity.</span>
<span id="L1504">LZ_RESCALE = 1.0                !   [nondim] default = 1.0</span>
<span id="L1505">                                ! A coefficient to rescale the distance to the nearest solid boundary. This</span>
<span id="L1506">                                ! adjustment is to account for regions where 3 dimensional turbulence prevents</span>
<span id="L1507">                                ! the growth of shear instabilies [nondim].</span>
<span id="L1508">TKE_BACKGROUND = 0.0            !   [m2 s-2] default = 0.0</span>
<span id="L1509">                                ! A background level of TKE used in the first iteration of the kappa equation.</span>
<span id="L1510">                                ! TKE_BACKGROUND could be 0.</span>
<span id="L1511"></span>
<span id="L1512">! === module MOM_CVMix_shear ===</span>
<span id="L1513">! Parameterization of shear-driven turbulence via CVMix (various options)</span>
<span id="L1514">USE_LMD94 = False               !   [Boolean] default = False</span>
<span id="L1515">                                ! If true, use the Large-McWilliams-Doney (JGR 1994) shear mixing</span>
<span id="L1516">                                ! parameterization.</span>
<span id="L1517">USE_PP81 = False                !   [Boolean] default = False</span>
<span id="L1518">                                ! If true, use the Pacanowski and Philander (JPO 1981) shear mixing</span>
<span id="L1519">                                ! parameterization.</span>
<span id="L1520"></span>
<span id="L1521">! === module MOM_CVMix_ddiff ===</span>
<span id="L1522">! Parameterization of mixing due to double diffusion processes via CVMix</span>
<span id="L1523">USE_CVMIX_DDIFF = False         !   [Boolean] default = False</span>
<span id="L1524">                                ! If true, turns on double diffusive processes via CVMix. Note that double</span>
<span id="L1525">                                ! diffusive processes on viscosity are ignored in CVMix, see</span>
<span id="L1526">                                ! http://cvmix.github.io/ for justification.</span>
<span id="L1527"></span>
<span id="L1528">! === module MOM_diabatic_aux ===</span>
<span id="L1529">! The following parameters are used for auxiliary diabatic processes.</span>
<span id="L1530">RECLAIM_FRAZIL = False          !   [Boolean] default = True</span>
<span id="L1531">                                ! If true, try to use any frazil heat deficit to cool any overlying layers down</span>
<span id="L1532">                                ! to the freezing point, thereby avoiding the creation of thin ice when the SST</span>
<span id="L1533">                                ! is above the freezing point.</span>
<span id="L1534">SALT_EXTRACTION_LIMIT = 0.9999  !   [nondim] default = 0.9999</span>
<span id="L1535">                                ! An upper limit on the fraction of the salt in a layer that can be lost to the</span>
<span id="L1536">                                ! net surface salt fluxes within a timestep.</span>
<span id="L1537">PRESSURE_DEPENDENT_FRAZIL = False !   [Boolean] default = False</span>
<span id="L1538">                                ! If true, use a pressure dependent freezing temperature when making frazil. The</span>
<span id="L1539">                                ! default is false, which will be faster but is inappropriate with ice-shelf</span>
<span id="L1540">                                ! cavities.</span>
<span id="L1541">USE_RIVER_HEAT_CONTENT = False  !   [Boolean] default = False</span>
<span id="L1542">                                ! If true, use the fluxes%runoff_Hflx field to set the heat carried by runoff,</span>
<span id="L1543">                                ! instead of using SST*CP*liq_runoff.</span>
<span id="L1544">USE_CALVING_HEAT_CONTENT = False !   [Boolean] default = False</span>
<span id="L1545">                                ! If true, use the fluxes%calving_Hflx field to set the heat carried by runoff,</span>
<span id="L1546">                                ! instead of using SST*CP*froz_runoff.</span>
<span id="L1547">DO_BRINE_PLUME = False          !   [Boolean] default = False</span>
<span id="L1548">                                ! If true, use a brine plume parameterization from Nguyen et al., 2009.</span>
<span id="L1549">VAR_PEN_SW = False              !   [Boolean] default = False</span>
<span id="L1550">                                ! If true, use one of the CHL_A schemes specified by OPACITY_SCHEME to determine</span>
<span id="L1551">                                ! the e-folding depth of incoming short wave radiation.</span>
<span id="L1552"></span>
<span id="L1553">! === module MOM_regularize_layers ===</span>
<span id="L1554">REGULARIZE_SURFACE_LAYERS = False !   [Boolean] default = False</span>
<span id="L1555">                                ! If defined, vertically restructure the near-surface layers when they have too</span>
<span id="L1556">                                ! much lateral variations to allow for sensible lateral barotropic transports.</span>
<span id="L1557"></span>
<span id="L1558">! === module MOM_opacity ===</span>
<span id="L1559">EXP_OPACITY_SCHEME = &quot;SINGLE_EXP&quot; ! default = &quot;SINGLE_EXP&quot;</span>
<span id="L1560">                                ! This character string specifies which exponential opacity scheme to utilize.</span>
<span id="L1561">                                ! Currently valid options include:</span>
<span id="L1562">                                !        SINGLE_EXP - Single Exponent decay.</span>
<span id="L1563">                                !        DOUBLE_EXP - Double Exponent decay.</span>
<span id="L1564">PEN_SW_SCALE = 0.0              !   [m] default = 0.0</span>
<span id="L1565">                                ! The vertical absorption e-folding depth of the penetrating shortwave</span>
<span id="L1566">                                ! radiation.</span>
<span id="L1567">PEN_SW_FRAC = 0.0               !   [nondim] default = 0.0</span>
<span id="L1568">                                ! The fraction of the shortwave radiation that penetrates below the surface.</span>
<span id="L1569">PEN_SW_NBANDS = 1               ! default = 1</span>
<span id="L1570">                                ! The number of bands of penetrating shortwave radiation.</span>
<span id="L1571">OPTICS_ANSWER_DATE = 99991231   ! default = 99991231</span>
<span id="L1572">                                ! The vintage of the order of arithmetic and expressions in the optics</span>
<span id="L1573">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L1574">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L1575">PEN_SW_FLUX_ABSORB = 2.5E-11    !   [degC m s-1] default = 2.5E-11</span>
<span id="L1576">                                ! A minimum remaining shortwave heating rate that will be simply absorbed in the</span>
<span id="L1577">                                ! next sufficiently thick layers for computational efficiency, instead of</span>
<span id="L1578">                                ! continuing to penetrate.  The default, 2.5e-11 degC m s-1, is about 1e-4 W m-2</span>
<span id="L1579">                                ! or 0.08 degC m century-1, but 0 is also a valid value.</span>
<span id="L1580">PEN_SW_ABSORB_MINTHICK = 1.0    !   [m] default = 1.0</span>
<span id="L1581">                                ! A thickness that is used to absorb the remaining penetrating shortwave heat</span>
<span id="L1582">                                ! flux when it drops below PEN_SW_FLUX_ABSORB.</span>
<span id="L1583">OPACITY_LAND_VALUE = 10.0       !   [m-1] default = 10.0</span>
<span id="L1584">                                ! The value to use for opacity over land. The default is 10 m-1 - a value for</span>
<span id="L1585">                                ! muddy water.</span>
<span id="L1586"></span>
<span id="L1587">! === module MOM_tracer_advect ===</span>
<span id="L1588">TRACER_ADVECTION_SCHEME = &quot;PLM&quot; ! default = &quot;PLM&quot;</span>
<span id="L1589">                                ! The horizontal transport scheme for tracers:</span>
<span id="L1590">                                !   PLM    - Piecewise Linear Method</span>
<span id="L1591">                                !   PPM:H3 - Piecewise Parabolic Method (Huyhn 3rd order)</span>
<span id="L1592">                                !   PPM    - Piecewise Parabolic Method (Colella-Woodward)</span>
<span id="L1593"></span>
<span id="L1594">! === module MOM_tracer_hor_diff ===</span>
<span id="L1595">KHTR = 600.0                    !   [m2 s-1] default = 0.0</span>
<span id="L1596">                                ! The background along-isopycnal tracer diffusivity.</span>
<span id="L1597">KHTR_MIN = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L1598">                                ! The minimum along-isopycnal tracer diffusivity.</span>
<span id="L1599">KHTR_MAX = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L1600">                                ! The maximum along-isopycnal tracer diffusivity. Set to a positive value to</span>
<span id="L1601">                                ! activate.</span>
<span id="L1602">KHTR_PASSIVITY_COEFF = 0.0      !   [nondim] default = 0.0</span>
<span id="L1603">                                ! The coefficient that scales deformation radius over grid-spacing in passivity,</span>
<span id="L1604">                                ! where passivity is the ratio between along isopycnal mixing of tracers to</span>
<span id="L1605">                                ! thickness mixing. A non-zero value enables this parameterization.</span>
<span id="L1606">KHTR_PASSIVITY_MIN = 0.5        !   [nondim] default = 0.5</span>
<span id="L1607">                                ! The minimum passivity which is the ratio between along isopycnal mixing of</span>
<span id="L1608">                                ! tracers to thickness mixing.</span>
<span id="L1609">DIFFUSE_ML_TO_INTERIOR = False  !   [Boolean] default = False</span>
<span id="L1610">                                ! If true, enable epipycnal mixing between the surface boundary layer and the</span>
<span id="L1611">                                ! interior.</span>
<span id="L1612">CHECK_DIFFUSIVE_CFL = False     !   [Boolean] default = False</span>
<span id="L1613">                                ! If true, use enough iterations the diffusion to ensure that the diffusive</span>
<span id="L1614">                                ! equivalent of the CFL limit is not violated.  If false, always use the greater</span>
<span id="L1615">                                ! of 1 or MAX_TR_DIFFUSION_CFL iteration.</span>
<span id="L1616">MAX_TR_DIFFUSION_CFL = -1.0     !   [nondim] default = -1.0</span>
<span id="L1617">                                ! If positive, locally limit the along-isopycnal tracer diffusivity to keep the</span>
<span id="L1618">                                ! diffusive CFL locally at or below this value.  The number of diffusive</span>
<span id="L1619">                                ! iterations is often this value or the next greater integer.</span>
<span id="L1620">RECALC_NEUTRAL_SURF = False     !   [Boolean] default = False</span>
<span id="L1621">                                ! If true, then recalculate the neutral surfaces if the</span>
<span id="L1622">                                ! diffusive CFL is exceeded. If false, assume that the</span>
<span id="L1623">                                ! positions of the surfaces do not change</span>
<span id="L1624"></span>
<span id="L1625">! === module MOM_neutral_diffusion ===</span>
<span id="L1626">! This module implements neutral diffusion of tracers</span>
<span id="L1627">USE_NEUTRAL_DIFFUSION = False   !   [Boolean] default = False</span>
<span id="L1628">                                ! If true, enables the neutral diffusion module.</span>
<span id="L1629"></span>
<span id="L1630">! === module MOM_hor_bnd_diffusion ===</span>
<span id="L1631">! This module implements horizontal diffusion of tracers near boundaries</span>
<span id="L1632">USE_HORIZONTAL_BOUNDARY_DIFFUSION = False !   [Boolean] default = False</span>
<span id="L1633">                                ! If true, enables the horizonal boundary tracer&#x27;s diffusion module.</span>
<span id="L1634">OBSOLETE_DIAGNOSTIC_IS_FATAL = True !   [Boolean] default = True</span>
<span id="L1635">                                ! If an obsolete diagnostic variable appears in the diag_table, cause a FATAL</span>
<span id="L1636">                                ! error rather than issue a WARNING.</span>
<span id="L1637"></span>
<span id="L1638">! === module MOM_sum_output ===</span>
<span id="L1639">CALCULATE_APE = True            !   [Boolean] default = True</span>
<span id="L1640">                                ! If true, calculate the available potential energy of the interfaces.  Setting</span>
<span id="L1641">                                ! this to false reduces the memory footprint of high-PE-count models</span>
<span id="L1642">                                ! dramatically.</span>
<span id="L1643">WRITE_STOCKS = True             !   [Boolean] default = True</span>
<span id="L1644">                                ! If true, write the integrated tracer amounts to stdout when the energy files</span>
<span id="L1645">                                ! are written.</span>
<span id="L1646">MAXTRUNC = 5000                 !   [truncations save_interval-1] default = 0</span>
<span id="L1647">                                ! The run will be stopped, and the day set to a very large value if the velocity</span>
<span id="L1648">                                ! is truncated more than MAXTRUNC times between energy saves.  Set MAXTRUNC to 0</span>
<span id="L1649">                                ! to stop if there is any truncation of velocities.</span>
<span id="L1650">MAX_ENERGY = 0.0                !   [m2 s-2] default = 0.0</span>
<span id="L1651">                                ! The maximum permitted average energy per unit mass; the model will be stopped</span>
<span id="L1652">                                ! if there is more energy than this.  If zero or negative, this is set to</span>
<span id="L1653">                                ! 10*MAXVEL^2.</span>
<span id="L1654">MAXVEL = 6.0                    !   [m s-1] default = 3.0E+08</span>
<span id="L1655">                                ! The maximum velocity allowed before the velocity components are truncated.</span>
<span id="L1656">ENERGYFILE = &quot;ocean.stats&quot;      ! default = &quot;ocean.stats&quot;</span>
<span id="L1657">                                ! The file to use to write the energies and globally summed diagnostics.</span>
<span id="L1658">DATE_STAMPED_STDOUT = False     !   [Boolean] default = True</span>
<span id="L1659">                                ! If true, use dates (not times) in messages to stdout</span>
<span id="L1660">ISO_DATE_STAMPED_STDOUT = False !   [Boolean] default = False</span>
<span id="L1661">                                ! If true, use ISO formatted dates in messages to stdout</span>
<span id="L1662">TIMEUNIT = 8.64E+04             !   [s] default = 8.64E+04</span>
<span id="L1663">                                ! The time unit in seconds a number of input fields</span>
<span id="L1664">READ_DEPTH_LIST = False         !   [Boolean] default = False</span>
<span id="L1665">                                ! Read the depth list from a file if it exists or create that file otherwise.</span>
<span id="L1666">DEPTH_LIST_MIN_INC = 1.0E-10    !   [m] default = 1.0E-10</span>
<span id="L1667">                                ! The minimum increment between the depths of the entries in the depth-list</span>
<span id="L1668">                                ! file.</span>
<span id="L1669">ENERGYSAVEDAYS = 0.25           !   [days] default = 1.0</span>
<span id="L1670">                                ! The interval in units of TIMEUNIT between saves of the energies of the run and</span>
<span id="L1671">                                ! other globally summed diagnostics.</span>
<span id="L1672">ENERGYSAVEDAYS_GEOMETRIC = 0.0  !   [days] default = 0.0</span>
<span id="L1673">                                ! The starting interval in units of TIMEUNIT for the first call to save the</span>
<span id="L1674">                                ! energies of the run and other globally summed diagnostics. The interval</span>
<span id="L1675">                                ! increases by a factor of 2. after each call to write_energy.</span>
<span id="L1676"></span>
<span id="L1677">! === module ocean_stochastics_init ===</span>
<span id="L1678">DO_SPPT = False                 !   [Boolean] default = False</span>
<span id="L1679">                                ! If true, then stochastically perturb the thermodynamic tendencies of T,S, amd</span>
<span id="L1680">                                ! h.  Amplitude and correlations are controlled by the nam_stoch namelist in the</span>
<span id="L1681">                                ! UFS model only.</span>
<span id="L1682">DO_SKEB = False                 !   [Boolean] default = False</span>
<span id="L1683">                                ! If true, then stochastically perturb the currents using the stochastic kinetic</span>
<span id="L1684">                                ! energy backscatter scheme.</span>
<span id="L1685">PERT_EPBL = False               !   [Boolean] default = False</span>
<span id="L1686">                                ! If true, then stochastically perturb the kinetic energy production and</span>
<span id="L1687">                                ! dissipation terms.  Amplitude and correlations are controlled by the nam_stoch</span>
<span id="L1688">                                ! namelist in the UFS model only.</span>
<span id="L1689"></span>
<span id="L1690">! === module MOM_surface_forcing ===</span>
<span id="L1691">VARIABLE_WINDS = False          !   [Boolean] default = True</span>
<span id="L1692">                                ! If true, the winds vary in time after the initialization.</span>
<span id="L1693">VARIABLE_BUOYFORCE = True       !   [Boolean] default = True</span>
<span id="L1694">                                ! If true, the buoyancy forcing varies in time after the initialization of the</span>
<span id="L1695">                                ! model.</span>
<span id="L1696">BUOY_CONFIG = &quot;const&quot;           ! default = &quot;zero&quot;</span>
<span id="L1697">                                ! The character string that indicates how buoyancy forcing is specified.  Valid</span>
<span id="L1698">                                ! options include (file), (data_override), (zero), (const), (linear), (MESO),</span>
<span id="L1699">                                ! (SCM_CVmix_tests), (BFB), (dumbbell), (USER) and (NONE).</span>
<span id="L1700">SENSIBLE_HEAT_FLUX = 100.0      !   [W/m2]</span>
<span id="L1701">                                ! A constant heat forcing (positive into ocean) applied through the sensible</span>
<span id="L1702">                                ! heat flux field.</span>
<span id="L1703">WIND_CONFIG = &quot;const&quot;           ! default = &quot;zero&quot;</span>
<span id="L1704">                                ! The character string that indicates how wind forcing is specified.  Valid</span>
<span id="L1705">                                ! options include (file), (data_override), (2gyre), (1gyre), (gyres), (zero),</span>
<span id="L1706">                                ! (const), (Neverworld), (scurves), (ideal_hurr), (SCM_CVmix_tests) and (USER).</span>
<span id="L1707">RESTOREBUOY = False             !   [Boolean] default = False</span>
<span id="L1708">                                ! If true, the buoyancy fluxes drive the model back toward some specified</span>
<span id="L1709">                                ! surface state with a rate given by FLUXCONST.</span>
<span id="L1710">LATENT_HEAT_FUSION = 3.34E+05   !   [J/kg] default = 3.34E+05</span>
<span id="L1711">                                ! The latent heat of fusion.</span>
<span id="L1712">LATENT_HEAT_VAPORIZATION = 2.5E+06 !   [J/kg] default = 2.5E+06</span>
<span id="L1713">                                ! The latent heat of fusion.</span>
<span id="L1714">GUST_CONST = 0.0                !   [Pa] default = 0.0</span>
<span id="L1715">                                ! The background gustiness in the winds.</span>
<span id="L1716">USTAR_GUSTLESS_BUG = False      !   [Boolean] default = False</span>
<span id="L1717">                                ! If true include a bug in the time-averaging of the gustless wind friction</span>
<span id="L1718">                                ! velocity</span>
<span id="L1719">READ_GUST_2D = False            !   [Boolean] default = False</span>
<span id="L1720">                                ! If true, use a 2-dimensional gustiness supplied from an input file</span>
<span id="L1721">CONST_WIND_TAUX = 0.1           !   [Pa]</span>
<span id="L1722">                                ! With wind_config const, this is the constant zonal wind-stress</span>
<span id="L1723">CONST_WIND_TAUY = 0.0           !   [Pa]</span>
<span id="L1724">                                ! With wind_config const, this is the constant meridional wind-stress</span>
<span id="L1725"></span>
<span id="L1726">! === module MOM_restart ===</span>
<span id="L1727">USE_WAVES = False               !   [Boolean] default = False</span>
<span id="L1728">                                ! If true, enables surface wave modules.</span>
<span id="L1729"></span>
<span id="L1730">! === module MOM_main (MOM_driver) ===</span>
<span id="L1731">DT_FORCING = 1200.0             !   [s] default = 1200.0</span>
<span id="L1732">                                ! The time step for changing forcing, coupling with other components, or</span>
<span id="L1733">                                ! potentially writing certain diagnostics. The default value is given by DT.</span>
<span id="L1734">DAYMAX = 5.0                    !   [days]</span>
<span id="L1735">                                ! The final time of the whole simulation, in units of TIMEUNIT seconds.  This</span>
<span id="L1736">                                ! also sets the potential end time of the present run segment if the end time is</span>
<span id="L1737">                                ! not set via ocean_solo_nml in input.nml.</span>
<span id="L1738">SINGLE_STEPPING_CALL = True     !   [Boolean] default = True</span>
<span id="L1739">                                ! If true, advance the state of MOM with a single step including both dynamics</span>
<span id="L1740">                                ! and thermodynamics.  If false the two phases are advanced with separate calls.</span>
<span id="L1741">RESTART_CONTROL = 0             ! default = 1</span>
<span id="L1742">                                ! An integer whose bits encode which restart files are written. Add 2 (bit 1)</span>
<span id="L1743">                                ! for a time-stamped file, and odd (bit 0) for a non-time-stamped file. A</span>
<span id="L1744">                                ! non-time-stamped restart file is saved at the end of the run segment for any</span>
<span id="L1745">                                ! non-negative value.</span>
<span id="L1746">RESTINT = 3650.0                !   [days] default = 0.0</span>
<span id="L1747">                                ! The interval between saves of the restart file in units of TIMEUNIT.  Use 0</span>
<span id="L1748">                                ! (the default) to not save incremental restart files at all.</span>
<span id="L1749">WRITE_CPU_STEPS = 1000          ! default = 1000</span>
<span id="L1750">                                ! The number of coupled timesteps between writing the cpu time. If this is not</span>
<span id="L1751">                                ! positive, do not check cpu time, and the segment run-length can not be set via</span>
<span id="L1752">                                ! an elapsed CPU time.</span>
<span id="L1753"></span>
<span id="L1754">! === module MOM_write_cputime ===</span>
<span id="L1755">MAXCPU = -1.0                   !   [wall-clock seconds] default = -1.0</span>
<span id="L1756">                                ! The maximum amount of cpu time per processor for which MOM should run before</span>
<span id="L1757">                                ! saving a restart file and quitting with a return value that indicates that a</span>
<span id="L1758">                                ! further run is required to complete the simulation. If automatic restarts are</span>
<span id="L1759">                                ! not desired, use a negative value for MAXCPU.  MAXCPU has units of wall-clock</span>
<span id="L1760">                                ! seconds, so the actual CPU time used is larger by a factor of the number of</span>
<span id="L1761">                                ! processors used.</span>
<span id="L1762">CPU_TIME_FILE = &quot;CPU_stats&quot;     ! default = &quot;CPU_stats&quot;</span>
<span id="L1763">                                ! The file into which CPU time is written.</span>
<span id="L1764"></span>
<span id="L1765">! === module MOM_file_parser ===</span>
<span id="L1766">SEND_LOG_TO_STDOUT = False      !   [Boolean] default = False</span>
<span id="L1767">                                ! If true, all log messages are also sent to stdout.</span>
<span id="L1768">DOCUMENT_FILE = &quot;MOM_parameter_doc&quot; ! default = &quot;MOM_parameter_doc&quot;</span>
<span id="L1769">                                ! The basename for files where run-time parameters, their settings, units and</span>
<span id="L1770">                                ! defaults are documented. Blank will disable all parameter documentation.</span>
<span id="L1771">COMPLETE_DOCUMENTATION = True   !   [Boolean] default = True</span>
<span id="L1772">                                ! If true, all run-time parameters are documented in MOM_parameter_doc.all .</span>
<span id="L1773">MINIMAL_DOCUMENTATION = True    !   [Boolean] default = True</span>
<span id="L1774">                                ! If true, non-default run-time parameters are documented in</span>
<span id="L1775">                                ! MOM_parameter_doc.short .</span>
</pre>
