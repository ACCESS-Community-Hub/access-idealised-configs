---
search:
  exclude: true
---

# adjustment2d-rho: MOM_parameter_doc.all

Every MOM6 parameter of the tested run of [adjustment2d-rho](../mom6examples/adjustment2d-rho.md), as MOM6 wrote it to `MOM_parameter_doc.all` in the run's output folder. Line numbers match the file.

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
<span id="L39">USE_REGRIDDING = True           !   [Boolean] default = False</span>
<span id="L40">                                ! If True, use the ALE algorithm (regridding/remapping). If False, use the</span>
<span id="L41">                                ! layered isopycnal algorithm.</span>
<span id="L42">REMAP_UV_USING_OLD_ALG = False  !   [Boolean] default = False</span>
<span id="L43">                                ! If true, uses the old remapping-via-a-delta-z method for remapping u and v. If</span>
<span id="L44">                                ! false, uses the new method that remaps between grids described by an old and</span>
<span id="L45">                                ! new thickness.</span>
<span id="L46">REMAP_AUXILIARY_VARS = False    !   [Boolean] default = False</span>
<span id="L47">                                ! If true, apply ALE remapping to all of the auxiliary 3-dimensional variables</span>
<span id="L48">                                ! that are needed to reproduce across restarts, similarly to what is already</span>
<span id="L49">                                ! being done with the primary state variables.  The default should be changed to</span>
<span id="L50">                                ! true.</span>
<span id="L51">BULKMIXEDLAYER = False          !   [Boolean] default = False</span>
<span id="L52">                                ! If true, use a Kraus-Turner-like bulk mixed layer with transitional buffer</span>
<span id="L53">                                ! layers.  Layers 1 through NKML+NKBL have variable densities. There must be at</span>
<span id="L54">                                ! least NKML+NKBL+1 layers if BULKMIXEDLAYER is true. BULKMIXEDLAYER can not be</span>
<span id="L55">                                ! used with USE_REGRIDDING. The default is influenced by ENABLE_THERMODYNAMICS.</span>
<span id="L56">USE_POROUS_BARRIER = False      !   [Boolean] default = False</span>
<span id="L57">                                ! If true, use porous barrier to constrain the widths and face areas at the</span>
<span id="L58">                                ! edges of the grid cells.</span>
<span id="L59">BATHYMETRY_AT_VEL = False       !   [Boolean] default = False</span>
<span id="L60">                                ! If true, there are separate values for the basin depths at velocity points.</span>
<span id="L61">                                ! Otherwise the effects of topography are entirely determined from thickness</span>
<span id="L62">                                ! points.</span>
<span id="L63">ENABLE_BUGS_BY_DEFAULT = True   !   [Boolean] default = True</span>
<span id="L64">                                ! If true, the defaults for certain recently added bug-fix flags are set to</span>
<span id="L65">                                ! recreate the bugs so that the code can be moved forward without changing</span>
<span id="L66">                                ! answers for existing configurations.  The defaults for groups of bug-fix flags</span>
<span id="L67">                                ! are periodcially changed to correct the bugs, at which point this parameter</span>
<span id="L68">                                ! will no longer be used to set their default.  Setting this to false means that</span>
<span id="L69">                                ! bugs are only used if they are actively selected, but it also means that</span>
<span id="L70">                                ! answers may change when code is updated due to newly found bugs.</span>
<span id="L71">DT = 150.0                      !   [s]</span>
<span id="L72">                                ! The (baroclinic) dynamics time step.  The time-step that is actually used will</span>
<span id="L73">                                ! be an integer fraction of the forcing time-step (DT_FORCING in ocean-only mode</span>
<span id="L74">                                ! or the coupling timestep in coupled mode.)</span>
<span id="L75">DT_THERM = 300.0                !   [s] default = 150.0</span>
<span id="L76">                                ! The thermodynamic time step. Ideally DT_THERM should be an integer multiple of</span>
<span id="L77">                                ! DT and of DT_TRACER_ADVECT and less than the forcing or coupling time-step.</span>
<span id="L78">                                ! However, if THERMO_SPANS_COUPLING is true, DT_THERM can be an integer multiple</span>
<span id="L79">                                ! of the coupling timestep. By default DT_THERM is set to DT.</span>
<span id="L80">THERMO_SPANS_COUPLING = False   !   [Boolean] default = False</span>
<span id="L81">                                ! If true, the MOM will take thermodynamic timesteps that can be longer than the</span>
<span id="L82">                                ! coupling timestep. The actual thermodynamic timestep that is used in this case</span>
<span id="L83">                                ! is the largest integer multiple of the coupling timestep that is less than or</span>
<span id="L84">                                ! equal to DT_THERM.</span>
<span id="L85">DT_TRACER_ADVECT = 300.0        !   [s] default = 300.0</span>
<span id="L86">                                ! The tracer advection time step. Ideally DT_TRACER_ADVECT should be an integer</span>
<span id="L87">                                ! multiple of DT, less than DT_THERM, and less than the forcing or coupling</span>
<span id="L88">                                ! time-step. However, if TRADV_SPANS_COUPLING is true, DT_TRACER_ADVECT can be</span>
<span id="L89">                                ! longer than the coupling timestep. By default DT_TRACER_ADVECT is set to</span>
<span id="L90">                                ! DT_THERM.</span>
<span id="L91">TRADV_SPANS_COUPLING = False    !   [Boolean] default = False</span>
<span id="L92">                                ! If true, the MOM will take tracer advection timesteps that can be longer than</span>
<span id="L93">                                ! the coupling timestep. The actual tracer advection timestep that is used in</span>
<span id="L94">                                ! this case is the largest integer multiple of the coupling timestep that is</span>
<span id="L95">                                ! less than or equal to DT_TRACER_ADVECT.</span>
<span id="L96">THICKNESSDIFFUSE = False        !   [Boolean] default = False</span>
<span id="L97">                                ! If true, isopycnal surfaces are diffused with a Laplacian coefficient of KHTH.</span>
<span id="L98">APPLY_INTERFACE_FILTER = False  !   [Boolean] default = False</span>
<span id="L99">                                ! If true, model interface heights are subjected to a grid-scale dependent</span>
<span id="L100">                                ! spatial smoothing, often with biharmonic filter.</span>
<span id="L101">HMIX_SFC_PROP = 1.0             !   [m] default = 1.0</span>
<span id="L102">                                ! If BULKMIXEDLAYER is false, HMIX_SFC_PROP is the depth over which to average</span>
<span id="L103">                                ! to find surface properties like SST and SSS or density (but not surface</span>
<span id="L104">                                ! velocities).</span>
<span id="L105">HMIX_UV_SFC_PROP = 0.0          !   [m] default = 0.0</span>
<span id="L106">                                ! If BULKMIXEDLAYER is false, HMIX_UV_SFC_PROP is the depth over which to</span>
<span id="L107">                                ! average to find surface flow properties, SSU, SSV. A non-positive value</span>
<span id="L108">                                ! indicates no averaging.</span>
<span id="L109">HFREEZE = -1.0                  !   [m] default = -1.0</span>
<span id="L110">                                ! If HFREEZE &gt; 0, melt potential will be computed. The actual depth over which</span>
<span id="L111">                                ! melt potential is computed will be min(HFREEZE, OBLD), where OBLD is the</span>
<span id="L112">                                ! boundary layer depth. If HFREEZE &lt;= 0 (default), melt potential will not be</span>
<span id="L113">                                ! computed.</span>
<span id="L114">INTERPOLATE_P_SURF = False      !   [Boolean] default = False</span>
<span id="L115">                                ! If true, linearly interpolate the surface pressure over the coupling time</span>
<span id="L116">                                ! step, using the specified value at the end of the step.</span>
<span id="L117">DTBT_RESET_PERIOD = -1.0        !   [s] default = -1.0</span>
<span id="L118">                                ! The period between recalculations of DTBT (if DTBT &lt;= 0). If DTBT_RESET_PERIOD</span>
<span id="L119">                                ! is negative, DTBT is set based only on information available at</span>
<span id="L120">                                ! initialization.  If 0, DTBT will be set every dynamics time step. The default</span>
<span id="L121">                                ! is set by DT_THERM.  This is only used if SPLIT is true.</span>
<span id="L122">FRAZIL = False                  !   [Boolean] default = False</span>
<span id="L123">                                ! If true, water freezes if it gets too cold, and the accumulated heat deficit</span>
<span id="L124">                                ! is returned in the surface state.  FRAZIL is only used if</span>
<span id="L125">                                ! ENABLE_THERMODYNAMICS is true.</span>
<span id="L126">DO_GEOTHERMAL = False           !   [Boolean] default = False</span>
<span id="L127">                                ! If true, apply geothermal heating.</span>
<span id="L128">BOUND_SALINITY = False          !   [Boolean] default = False</span>
<span id="L129">                                ! If true, limit salinity to being positive. (The sea-ice model may ask for more</span>
<span id="L130">                                ! salt than is available and drive the salinity negative otherwise.)</span>
<span id="L131">SALINITY_UNDERFLOW = 0.0        !   [PPT] default = 0.0</span>
<span id="L132">                                ! A tiny value of salinity below which the it is set to 0.  For reference, one</span>
<span id="L133">                                ! molecule of salt per square meter of ocean is of order 1e-29 ppt.</span>
<span id="L134">TEMPERATURE_UNDERFLOW = 0.0     !   [degC] default = 0.0</span>
<span id="L135">                                ! A tiny magnitude of temperatures below which they are set to 0.</span>
<span id="L136">C_P = 3925.0                    !   [J kg-1 K-1] default = 3991.86795711963</span>
<span id="L137">                                ! The heat capacity of sea water, approximated as a constant. This is only used</span>
<span id="L138">                                ! if ENABLE_THERMODYNAMICS is true. The default value is from the TEOS-10</span>
<span id="L139">                                ! definition of conservative temperature.</span>
<span id="L140">USE_PSURF_IN_EOS = True         !   [Boolean] default = True</span>
<span id="L141">                                ! If true, always include the surface pressure contributions in equation of</span>
<span id="L142">                                ! state calculations.</span>
<span id="L143">P_REF = 2.0E+07                 !   [Pa] default = 2.0E+07</span>
<span id="L144">                                ! The pressure that is used for calculating the coordinate density.  (1 Pa = 1e4</span>
<span id="L145">                                ! dbar, so 2e7 is commonly used.) This is only used if USE_EOS and</span>
<span id="L146">                                ! ENABLE_THERMODYNAMICS are true.</span>
<span id="L147">NONBLOCKING_P_SURF_BUG = True   !   [Boolean] default = True</span>
<span id="L148">                                ! If true, recover a bug in which the non-blocking halo update of the surface</span>
<span id="L149">                                ! pressure is not completed before the halo points of forces%p_surf are copied</span>
<span id="L150">                                ! into tv%p_surf, so that those halo points hold the surface pressure from the</span>
<span id="L151">                                ! previous coupling step, or zeros on the first step after a restart.  This is</span>
<span id="L152">                                ! only used if NONBLOCKING_UPDATES and USE_PSURF_IN_EOS are true</span>
<span id="L153">FIRST_DIRECTION = 0             ! default = 0</span>
<span id="L154">                                ! An integer that indicates which direction goes first in parts of the code that</span>
<span id="L155">                                ! use directionally split updates, with even numbers (or 0) used for x- first</span>
<span id="L156">                                ! and odd numbers used for y-first.</span>
<span id="L157">ALTERNATE_FIRST_DIRECTION = False !   [Boolean] default = False</span>
<span id="L158">                                ! If true, after every dynamic timestep alternate whether the x- or y- direction</span>
<span id="L159">                                ! updates occur first in directionally split parts of the calculation. If this</span>
<span id="L160">                                ! is true, FIRST_DIRECTION applies at the start of a new run or if the next</span>
<span id="L161">                                ! first direction can not be found in the restart file.</span>
<span id="L162">CHECK_BAD_SURFACE_VALS = False  !   [Boolean] default = False</span>
<span id="L163">                                ! If true, check the surface state for ridiculous values.</span>
<span id="L164">DEFAULT_ANSWER_DATE = 99991231  ! default = 99991231</span>
<span id="L165">                                ! This sets the default value for the various _ANSWER_DATE parameters.</span>
<span id="L166">SURFACE_ANSWER_DATE = 99991231  ! default = 99991231</span>
<span id="L167">                                ! The vintage of the expressions for the surface properties.  Values below</span>
<span id="L168">                                ! 20190101 recover the answers from the end of 2018, while higher values use</span>
<span id="L169">                                ! updated and more robust forms of the same expressions.</span>
<span id="L170">SAVE_INITIAL_CONDS = True       !   [Boolean] default = False</span>
<span id="L171">                                ! If true, write the initial conditions to a file given by IC_OUTPUT_FILE.</span>
<span id="L172">IC_OUTPUT_FILE = &quot;Initial_state&quot; ! default = &quot;MOM_IC&quot;</span>
<span id="L173">                                ! The file into which to write the initial conditions.</span>
<span id="L174">WRITE_GEOM = 1                  ! default = 1</span>
<span id="L175">                                ! If =0, never write the geometry and vertical grid files. If =1, write the</span>
<span id="L176">                                ! geometry and vertical grid files only for a new simulation. If =2, always</span>
<span id="L177">                                ! write the geometry and vertical grid files. Other values are invalid.</span>
<span id="L178">GEOM_FILE = &quot;ocean_geometry&quot;    ! default = &quot;ocean_geometry&quot;</span>
<span id="L179">                                ! The file into which to write the ocean geometry.</span>
<span id="L180">USE_DBCLIENT = False            !   [Boolean] default = False</span>
<span id="L181">                                ! If true, initialize a client to a remote database that can be used for online</span>
<span id="L182">                                ! analysis and machine-learning inference.</span>
<span id="L183">ICE_SHELF = False               !   [Boolean] default = False</span>
<span id="L184">                                ! If true, enables the ice shelf model.</span>
<span id="L185">USE_PARTICLES = False           !   [Boolean] default = False</span>
<span id="L186">                                ! If true, use the particles package.</span>
<span id="L187">USE_UH_PARTICLES = False        !   [Boolean] default = False</span>
<span id="L188">                                ! If true, use the uh velocity in the particles package.</span>
<span id="L189">ENSEMBLE_OCEAN = False          !   [Boolean] default = False</span>
<span id="L190">                                ! If False, The model is being run in serial mode as a single realization. If</span>
<span id="L191">                                ! True, The current model realization is part of a larger ensemble and at the</span>
<span id="L192">                                ! end of step MOM, we will perform a gather of the ensemble members for</span>
<span id="L193">                                ! statistical evaluation and/or data assimilation.</span>
<span id="L194">HOMOGENIZE_FORCINGS = False     !   [Boolean] default = False</span>
<span id="L195">                                ! If True, homogenize the forces and fluxes.</span>
<span id="L196"></span>
<span id="L197">! === module MOM_domains ===</span>
<span id="L198">REENTRANT_X = False             !   [Boolean] default = True</span>
<span id="L199">                                ! If true, the domain is zonally reentrant.</span>
<span id="L200">REENTRANT_Y = True              !   [Boolean] default = False</span>
<span id="L201">                                ! If true, the domain is meridionally reentrant.</span>
<span id="L202">TRIPOLAR_N = False              !   [Boolean] default = False</span>
<span id="L203">                                ! Use tripolar connectivity at the northern edge of the domain.  With</span>
<span id="L204">                                ! TRIPOLAR_N, NIGLOBAL must be even.</span>
<span id="L205">NIGLOBAL = 128                  !</span>
<span id="L206">                                ! The total number of thickness grid points in the x-direction in the physical</span>
<span id="L207">                                ! domain. With STATIC_MEMORY_ this is set in MOM_memory.h at compile time.</span>
<span id="L208">NJGLOBAL = 4                    !</span>
<span id="L209">                                ! The total number of thickness grid points in the y-direction in the physical</span>
<span id="L210">                                ! domain. With STATIC_MEMORY_ this is set in MOM_memory.h at compile time.</span>
<span id="L211">NIHALO = 4                      ! default = 4</span>
<span id="L212">                                ! The number of halo points on each side in the x-direction.  How this is set</span>
<span id="L213">                                ! varies with the calling component and static or dynamic memory configuration.</span>
<span id="L214">NJHALO = 4                      ! default = 4</span>
<span id="L215">                                ! The number of halo points on each side in the y-direction.  How this is set</span>
<span id="L216">                                ! varies with the calling component and static or dynamic memory configuration.</span>
<span id="L217"></span>
<span id="L218">! === module MOM_hor_index ===</span>
<span id="L219">! Sets the horizontal array index types.</span>
<span id="L220"></span>
<span id="L221">! === module MOM_grid ===</span>
<span id="L222">! Parameters providing information about the lateral grid.</span>
<span id="L223">REFERENCE_HEIGHT = 0.0          !   [m] default = 0.0</span>
<span id="L224">                                ! A reference value for geometric height fields, such as bathyT.</span>
<span id="L225"></span>
<span id="L226">! === module MOM_fixed_initialization ===</span>
<span id="L227">INPUTDIR = &quot;INPUT&quot;              ! default = &quot;.&quot;</span>
<span id="L228">                                ! The directory in which input files are found.</span>
<span id="L229"></span>
<span id="L230">! === module MOM_grid_init ===</span>
<span id="L231">GRID_CONFIG = &quot;cartesian&quot;       !</span>
<span id="L232">                                ! A character string that determines the method for defining the horizontal</span>
<span id="L233">                                ! grid.  Current options are:</span>
<span id="L234">                                !     mosaic - read the grid from a mosaic (supergrid)</span>
<span id="L235">                                !              file set by GRID_FILE.</span>
<span id="L236">                                !     cartesian - use a (flat) Cartesian grid.</span>
<span id="L237">                                !     spherical - use a simple spherical grid.</span>
<span id="L238">                                !     mercator - use a Mercator spherical grid.</span>
<span id="L239">AXIS_UNITS = &quot;k&quot;                ! default = &quot;degrees&quot;</span>
<span id="L240">                                ! The units for the Cartesian axes. Valid entries are:</span>
<span id="L241">                                !     degrees - degrees of latitude and longitude</span>
<span id="L242">                                !     m or meter(s) - meters</span>
<span id="L243">                                !     k or km or kilometer(s) - kilometers</span>
<span id="L244">SOUTHLAT = 30.0                 !   [km]</span>
<span id="L245">                                ! The southern latitude of the domain or the equivalent starting value for the</span>
<span id="L246">                                ! y-axis.</span>
<span id="L247">LENLAT = 40.0                   !   [km]</span>
<span id="L248">                                ! The latitudinal or y-direction length of the domain.</span>
<span id="L249">WESTLON = 0.0                   !   [km] default = 0.0</span>
<span id="L250">                                ! The western longitude of the domain or the equivalent starting value for the</span>
<span id="L251">                                ! x-axis.</span>
<span id="L252">LENLON = 64.0                   !   [km]</span>
<span id="L253">                                ! The longitudinal or x-direction length of the domain.</span>
<span id="L254">RAD_EARTH = 6.378E+06           !   [m] default = 6.378E+06</span>
<span id="L255">                                ! The radius of the Earth.</span>
<span id="L256">TOPO_CONFIG = &quot;flat&quot;            !</span>
<span id="L257">                                ! This specifies how bathymetry is specified:</span>
<span id="L258">                                !     file - read bathymetric information from the file</span>
<span id="L259">                                !       specified by (TOPO_FILE).</span>
<span id="L260">                                !     flat - flat bottom set to MAXIMUM_DEPTH.</span>
<span id="L261">                                !     bowl - an analytically specified bowl-shaped basin</span>
<span id="L262">                                !       ranging between MAXIMUM_DEPTH and MINIMUM_DEPTH.</span>
<span id="L263">                                !     spoon - a similar shape to &#x27;bowl&#x27;, but with an vertical</span>
<span id="L264">                                !       wall at the southern face.</span>
<span id="L265">                                !     halfpipe - a zonally uniform channel with a half-sine</span>
<span id="L266">                                !       profile in the meridional direction.</span>
<span id="L267">                                !     bbuilder - build topography from list of functions.</span>
<span id="L268">                                !     benchmark - use the benchmark test case topography.</span>
<span id="L269">                                !     Neverworld - use the Neverworld test case topography.</span>
<span id="L270">                                !     DOME - use a slope and channel configuration for the</span>
<span id="L271">                                !       DOME sill-overflow test case.</span>
<span id="L272">                                !     ISOMIP - use a slope and channel configuration for the</span>
<span id="L273">                                !       ISOMIP test case.</span>
<span id="L274">                                !     DOME2D - use a shelf and slope configuration for the</span>
<span id="L275">                                !       DOME2D gravity current/overflow test case.</span>
<span id="L276">                                !     Kelvin - flat but with rotated land mask.</span>
<span id="L277">                                !     seamount - Gaussian bump for spontaneous motion test case.</span>
<span id="L278">                                !     dumbbell - Sloshing channel with reservoirs on both ends.</span>
<span id="L279">                                !     shelfwave - exponential slope for shelfwave test case.</span>
<span id="L280">                                !     Phillips - ACC-like idealized topography used in the Phillips config.</span>
<span id="L281">                                !     dense - Denmark Strait-like dense water formation and overflow.</span>
<span id="L282">                                !     USER - call a user modified routine.</span>
<span id="L283">MINIMUM_DEPTH = 0.1             !   [m] default = 0.0</span>
<span id="L284">                                ! The minimum depth of the ocean.</span>
<span id="L285">MAXIMUM_DEPTH = 20.0            !   [m]</span>
<span id="L286">                                ! The maximum depth of the ocean.</span>
<span id="L287"></span>
<span id="L288">! === module MOM_open_boundary ===</span>
<span id="L289">! Controls where open boundaries are located, what kind of boundary condition to impose, and what data to apply,</span>
<span id="L290">! if any.</span>
<span id="L291">OBC_NUMBER_OF_SEGMENTS = 0      ! default = 0</span>
<span id="L292">                                ! The number of open boundary segments.</span>
<span id="L293">MASKING_DEPTH = -9999.0         !   [m] default = -9999.0</span>
<span id="L294">                                ! The depth below which to mask points as land points, for which all fluxes are</span>
<span id="L295">                                ! zeroed out. MASKING_DEPTH is ignored if it has the special default value.</span>
<span id="L296">CHANNEL_CONFIG = &quot;none&quot;         ! default = &quot;none&quot;</span>
<span id="L297">                                ! A parameter that determines which set of channels are</span>
<span id="L298">                                ! restricted to specific  widths.  Options are:</span>
<span id="L299">                                !     none - All channels have the grid width.</span>
<span id="L300">                                !     global_1deg - Sets 16 specific channels appropriate</span>
<span id="L301">                                !       for a 1-degree model, as used in CM2G.</span>
<span id="L302">                                !     list - Read the channel locations and widths from a</span>
<span id="L303">                                !       text file, like MOM_channel_list in the MOM_SIS</span>
<span id="L304">                                !       test case.</span>
<span id="L305">                                !     file - Read open face widths everywhere from a</span>
<span id="L306">                                !       NetCDF file on the model grid.</span>
<span id="L307">SUBGRID_TOPO_AT_VEL = False     !   [Boolean] default = False</span>
<span id="L308">                                ! If true, use variables from TOPO_AT_VEL_FILE as parameters for porous barrier.</span>
<span id="L309">ROTATION = &quot;beta&quot;               ! default = &quot;2omegasinlat&quot;</span>
<span id="L310">                                ! This specifies how the Coriolis parameter is specified:</span>
<span id="L311">                                !     2omegasinlat - Use twice the planetary rotation rate</span>
<span id="L312">                                !       times the sine of latitude.</span>
<span id="L313">                                !     betaplane - Use a beta-plane or f-plane.</span>
<span id="L314">                                !     USER - call a user modified routine.</span>
<span id="L315">F_0 = 0.0                       !   [s-1] default = 0.0</span>
<span id="L316">                                ! The reference value of the Coriolis parameter with the betaplane option.</span>
<span id="L317">BETA = 0.0                      !   [m-1 s-1] default = 0.0</span>
<span id="L318">                                ! The northward gradient of the Coriolis parameter with the betaplane option.</span>
<span id="L319">BETA_LAT_REF = 0.0              !   [kilometers] default = 0.0</span>
<span id="L320">                                ! The reference latitude (origin) of the beta-plane</span>
<span id="L321">GRID_ROTATION_ANGLE_BUGS = False !   [Boolean] default = False</span>
<span id="L322">                                ! If true, use an older algorithm to calculate the sine and cosines needed</span>
<span id="L323">                                ! rotate between grid-oriented directions and true north and east.  Differences</span>
<span id="L324">                                ! arise at the tripolar fold.</span>
<span id="L325"></span>
<span id="L326">! === module MOM_verticalGrid ===</span>
<span id="L327">! Parameters providing information about the vertical grid.</span>
<span id="L328">G_EARTH = 10.0                  !   [m s-2] default = 9.8</span>
<span id="L329">                                ! The gravitational acceleration of the Earth.</span>
<span id="L330">RHO_0 = 1000.0                  !   [kg m-3] default = 1035.0</span>
<span id="L331">                                ! The mean ocean density used with BOUSSINESQ true to calculate accelerations</span>
<span id="L332">                                ! and the mass for conservation properties, or with BOUSSINSEQ false to convert</span>
<span id="L333">                                ! some parameters from vertical units of m to kg m-2.</span>
<span id="L334">BOUSSINESQ = True               !   [Boolean] default = True</span>
<span id="L335">                                ! If true, make the Boussinesq approximation.</span>
<span id="L336">ANGSTROM = 1.0E-15              !   [m] default = 1.0E-10</span>
<span id="L337">                                ! The minimum layer thickness, usually one-Angstrom.</span>
<span id="L338">H_TO_M = 1.0                    !   [m H-1] default = 1.0</span>
<span id="L339">                                ! A constant that translates the model&#x27;s internal units of thickness into m.</span>
<span id="L340">NK = 25                         !   [nondim]</span>
<span id="L341">                                ! The number of model layers.</span>
<span id="L342">ADVECTION_SCHEME_VARIANCE_UNDERFLOW = 1.0E-23 !   [Conc2 (tracer dependent)] default = 1.0E-23</span>
<span id="L343">                                ! A tiny magnitude for variance used to determine when advection scheme variance</span>
<span id="L344">                                ! production is set to 0.</span>
<span id="L345"></span>
<span id="L346">! === module MOM_tracer_registry ===</span>
<span id="L347"></span>
<span id="L348">! === module MOM_EOS ===</span>
<span id="L349">EQN_OF_STATE = &quot;LINEAR&quot;         ! default = &quot;WRIGHT_FULL&quot;</span>
<span id="L350">                                ! EQN_OF_STATE determines which ocean equation of state should be used.</span>
<span id="L351">                                ! Currently, the valid choices are &quot;LINEAR&quot;, &quot;UNESCO&quot;, &quot;JACKETT_MCD&quot;, &quot;WRIGHT&quot;,</span>
<span id="L352">                                ! &quot;WRIGHT_REDUCED&quot;, &quot;WRIGHT_FULL&quot;, &quot;NEMO&quot;, &quot;ROQUET_RHO&quot;, &quot;ROQUET_SPV&quot; and</span>
<span id="L353">                                ! &quot;TEOS10&quot;.  This is only used if USE_EOS is true.</span>
<span id="L354">RHO_REF_LINEAR_EOS = 1000.0     !   [kg m-3] default = 1000.0</span>
<span id="L355">                                ! When EQN_OF_STATE=LINEAR, this is the density at T=T_REF_LINEAR_EOS,</span>
<span id="L356">                                ! S=S_REF_LINEAR_EOS and p=P_REF_LINEAR_EOS</span>
<span id="L357">T_REF_LINEAR_EOS = 0.0          !   [degC] default = 0.0</span>
<span id="L358">                                ! When EQN_OF_STATE=LINEAR, this is the reference temperature.</span>
<span id="L359">S_REF_LINEAR_EOS = 0.0          !   [psu] default = 0.0</span>
<span id="L360">                                ! When EQN_OF_STATE=LINEAR, this is the reference salinity.</span>
<span id="L361">P_REF_LINEAR_EOS = 0.0          !   [Pa] default = 0.0</span>
<span id="L362">                                ! When EQN_OF_STATE=LINEAR, this is the reference pressure.</span>
<span id="L363">DRHO_DT = 0.0                   !   [kg m-3 K-1] default = -0.2</span>
<span id="L364">                                ! When EQN_OF_STATE=LINEAR, this is the partial derivative of density with</span>
<span id="L365">                                ! temperature.</span>
<span id="L366">DRHO_DS = 1.0                   !   [kg m-3 ppt-1] default = 0.8</span>
<span id="L367">                                ! When EQN_OF_STATE=LINEAR, this is the partial derivative of density with</span>
<span id="L368">                                ! salinity.</span>
<span id="L369">DRHO_DP = 0.0                   !   [s2 m-2] default = 0.0</span>
<span id="L370">                                ! When EQN_OF_STATE=LINEAR, this is the partial derivative of density with</span>
<span id="L371">                                ! pressure (the inverse of sound speed squared).</span>
<span id="L372">RHO_T0_S0 = 1000.0              !   [kg m-3] default = 1000.0</span>
<span id="L373">                                ! When EQN_OF_STATE=LINEAR, this is the density at T=0, S=0 and p=0.  If</span>
<span id="L374">                                ! RHO_TO_SO is specified, RHO_REF_LINEAR_EOS, T_REF_LINEAR_EOS, S_REF_LINEAR_EOS</span>
<span id="L375">                                ! and P_REF_LINEAR_EOS are not used.</span>
<span id="L376">EOS_QUADRATURE = False          !   [Boolean] default = False</span>
<span id="L377">                                ! If true, always use the generic (quadrature) code code for the integrals of</span>
<span id="L378">                                ! density.</span>
<span id="L379">TFREEZE_FORM = &quot;LINEAR&quot;         ! default = &quot;LINEAR&quot;</span>
<span id="L380">                                ! TFREEZE_FORM determines which expression should be used for the freezing</span>
<span id="L381">                                ! point.  Currently, the valid choices are &quot;LINEAR&quot;, &quot;MILLERO_78&quot;, &quot;TEOS_POLY&quot;,</span>
<span id="L382">                                ! &quot;TEOS10&quot;</span>
<span id="L383">TFREEZE_S0_P0 = 0.0             !   [degC] default = 0.0</span>
<span id="L384">                                ! When TFREEZE_FORM=LINEAR, this is the freezing potential temperature at S=0,</span>
<span id="L385">                                ! P=0.</span>
<span id="L386">DTFREEZE_DS = -0.054            !   [degC ppt-1] default = -0.054</span>
<span id="L387">                                ! When TFREEZE_FORM=LINEAR, this is the derivative of the freezing potential</span>
<span id="L388">                                ! temperature with salinity.</span>
<span id="L389">DTFREEZE_DP = 0.0               !   [degC Pa-1] default = 0.0</span>
<span id="L390">                                ! When TFREEZE_FORM=LINEAR, this is the derivative of the freezing potential</span>
<span id="L391">                                ! temperature with pressure.</span>
<span id="L392">TFREEZE_S_IS_PRACS = True       !   [Boolean] default = True</span>
<span id="L393">                                ! When True, the model will check if the model internal salinity is practical</span>
<span id="L394">                                ! salinity.  If the model uses absolute salinity, a conversion will be applied.</span>
<span id="L395">TFREEZE_T_IS_POTT = True        !   [Boolean] default = True</span>
<span id="L396">                                ! When True, the model will check if the model internal temperature is potential</span>
<span id="L397">                                ! temperature.  If the model uses conservative temperature, a conversion will be</span>
<span id="L398">                                ! applied.</span>
<span id="L399"></span>
<span id="L400">! === module MOM_restart ===</span>
<span id="L401">PARALLEL_RESTARTFILES = False   !   [Boolean] default = False</span>
<span id="L402">                                ! If true, the IO layout is used to group processors that write to the same</span>
<span id="L403">                                ! restart file or each processor writes its own (numbered) restart file. If</span>
<span id="L404">                                ! false, a single restart file is generated combining output from all PEs.</span>
<span id="L405">RESTARTFILE = &quot;MOM.res&quot;         ! default = &quot;MOM.res&quot;</span>
<span id="L406">                                ! The name-root of the restart file.</span>
<span id="L407">MAX_FIELDS = 100                ! default = 100</span>
<span id="L408">                                ! The maximum number of restart fields that can be used.</span>
<span id="L409">RESTART_CHECKSUMS_REQUIRED = True !   [Boolean] default = True</span>
<span id="L410">                                ! If true, require the restart checksums to match and error out otherwise. Users</span>
<span id="L411">                                ! may want to avoid this comparison if for example the restarts are made from a</span>
<span id="L412">                                ! run with a different mask_table than the current run, in which case the</span>
<span id="L413">                                ! checksums will not match and cause crash.</span>
<span id="L414">RESTART_SYMMETRIC_CHECKSUMS = False !   [Boolean] default = False</span>
<span id="L415">                                ! If true, do the restart checksums on all the edge points for a non-reentrant</span>
<span id="L416">                                ! grid.  This requires that SYMMETRIC_MEMORY_ is defined at compile time.</span>
<span id="L417">RESTART_UNSIGNED_ZEROS = False  !   [Boolean] default = False</span>
<span id="L418">                                ! If true, convert any negative zeros that would be written to the restart file</span>
<span id="L419">                                ! into ordinary unsigned zeros.  This does not change answers, but it can be</span>
<span id="L420">                                ! helpful in comparing restart files after grid rotation, for example.</span>
<span id="L421">USE_FILTER = False              !   [Boolean] default = False</span>
<span id="L422">                                ! If true, use streaming band-pass filters to detect the instantaneous tidal</span>
<span id="L423">                                ! signals in the simulation.</span>
<span id="L424"></span>
<span id="L425">! === module MOM_tracer_flow_control ===</span>
<span id="L426">USE_USER_TRACER_EXAMPLE = False !   [Boolean] default = False</span>
<span id="L427">                                ! If true, use the USER_tracer_example tracer package.</span>
<span id="L428">USE_DOME_TRACER = False         !   [Boolean] default = False</span>
<span id="L429">                                ! If true, use the DOME_tracer tracer package.</span>
<span id="L430">USE_ISOMIP_TRACER = False       !   [Boolean] default = False</span>
<span id="L431">                                ! If true, use the ISOMIP_tracer tracer package.</span>
<span id="L432">USE_RGC_TRACER = False          !   [Boolean] default = False</span>
<span id="L433">                                ! If true, use the RGC_tracer tracer package.</span>
<span id="L434">USE_IDEAL_AGE_TRACER = False    !   [Boolean] default = False</span>
<span id="L435">                                ! If true, use the ideal_age_example tracer package.</span>
<span id="L436">USE_MARBL_TRACERS = False       !   [Boolean] default = False</span>
<span id="L437">                                ! If true, use the MARBL tracer package.</span>
<span id="L438">USE_REGIONAL_DYES = False       !   [Boolean] default = False</span>
<span id="L439">                                ! If true, use the regional_dyes tracer package.</span>
<span id="L440">USE_FILE_DYES = False           !   [Boolean] default = False</span>
<span id="L441">                                ! If true, use the file dyes tracer package.</span>
<span id="L442">USE_OIL_TRACER = False          !   [Boolean] default = False</span>
<span id="L443">                                ! If true, use the oil_tracer tracer package.</span>
<span id="L444">USE_ADVECTION_TEST_TRACER = False !   [Boolean] default = False</span>
<span id="L445">                                ! If true, use the advection_test_tracer tracer package.</span>
<span id="L446">USE_OCMIP2_CFC = False          !   [Boolean] default = False</span>
<span id="L447">                                ! If true, use the MOM_OCMIP2_CFC tracer package.</span>
<span id="L448">USE_CFC_CAP = False             !   [Boolean] default = False</span>
<span id="L449">                                ! If true, use the MOM_CFC_cap tracer package.</span>
<span id="L450">USE_generic_tracer = False      !   [Boolean] default = False</span>
<span id="L451">                                ! If true and _USE_GENERIC_TRACER is defined as a preprocessor macro, use the</span>
<span id="L452">                                ! MOM_generic_tracer packages.</span>
<span id="L453">USE_PSEUDO_SALT_TRACER = False  !   [Boolean] default = False</span>
<span id="L454">                                ! If true, use the pseudo salt tracer, typically run as a diagnostic.</span>
<span id="L455">USE_BOUNDARY_IMPULSE_TRACER = False !   [Boolean] default = False</span>
<span id="L456">                                ! If true, use the boundary impulse tracer.</span>
<span id="L457">USE_DYED_OBC_TRACER = False     !   [Boolean] default = False</span>
<span id="L458">                                ! If true, use the dyed_obc_tracer tracer package.</span>
<span id="L459">USE_NW2_TRACERS = False         !   [Boolean] default = False</span>
<span id="L460">                                ! If true, use the NeverWorld2 tracers.</span>
<span id="L461"></span>
<span id="L462">! === module MOM_coord_initialization ===</span>
<span id="L463">COORD_CONFIG = &quot;linear&quot;         ! default = &quot;none&quot;</span>
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
<span id="L481">LIGHTEST_DENSITY = 1000.0       !   [kg m-3] default = 1000.0</span>
<span id="L482">                                ! The reference potential density used for the surface interface.</span>
<span id="L483">DENSITY_RANGE = 5.0             !   [kg m-3] default = 2.0</span>
<span id="L484">                                ! The range of reference potential densities across all interfaces.</span>
<span id="L485">GFS = 10.0                      !   [m s-2] default = 10.0</span>
<span id="L486">                                ! The reduced gravity at the free surface.</span>
<span id="L487">REGRIDDING_COORDINATE_MODE = &quot;RHO&quot; ! default = &quot;LAYER&quot;</span>
<span id="L488">                                ! Coordinate mode for vertical regridding. Choose among the following</span>
<span id="L489">                                ! possibilities:  LAYER - Isopycnal or stacked shallow water layers</span>
<span id="L490">                                !  ZSTAR, Z* - stretched geopotential z*</span>
<span id="L491">                                !  SIGMA_SHELF_ZSTAR - stretched geopotential z* ignoring shelf</span>
<span id="L492">                                !  SIGMA - terrain following coordinates</span>
<span id="L493">                                !  RHO   - continuous isopycnal</span>
<span id="L494">                                !  HYCOM1 - HyCOM-like hybrid coordinate</span>
<span id="L495">                                !  HYBGEN - Hybrid coordinate from the Hycom hybgen code</span>
<span id="L496">                                !  ADAPTIVE - optimize for smooth neutral density surfaces</span>
<span id="L497">REGRIDDING_COORDINATE_UNITS = &quot;kg m^-3&quot; ! default = &quot;kg m^-3&quot;</span>
<span id="L498">                                ! Units of the regridding coordinate.</span>
<span id="L499">INTERPOLATION_SCHEME = &quot;P3M_IH4IH3&quot; ! default = &quot;P1M_H2&quot;</span>
<span id="L500">                                ! This sets the interpolation scheme to use to determine the new grid. These</span>
<span id="L501">                                ! parameters are only relevant when REGRIDDING_COORDINATE_MODE is set to a</span>
<span id="L502">                                ! function of state. Otherwise, it is not used. It can be one of the following</span>
<span id="L503">                                ! schemes:</span>
<span id="L504">                                !  P1M_H2     (2nd-order accurate)</span>
<span id="L505">                                !  P1M_H4     (2nd-order accurate)</span>
<span id="L506">                                !  P1M_IH4    (2nd-order accurate)</span>
<span id="L507">                                !  PLM        (2nd-order accurate)</span>
<span id="L508">                                !  PPM_CW     (3rd-order accurate)</span>
<span id="L509">                                !  PPM_H4     (3rd-order accurate)</span>
<span id="L510">                                !  PPM_IH4    (3rd-order accurate)</span>
<span id="L511">                                !  P3M_IH4IH3 (4th-order accurate)</span>
<span id="L512">                                !  P3M_IH6IH5 (4th-order accurate)</span>
<span id="L513">                                !  PQM_IH4IH3 (4th-order accurate)</span>
<span id="L514">                                !  PQM_IH6IH5 (5th-order accurate)</span>
<span id="L515">REMAPPING_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L516">                                ! The vintage of the expressions and order of arithmetic to use for remapping.</span>
<span id="L517">                                ! Values below 20190101 result in the use of older, less accurate expressions</span>
<span id="L518">                                ! that were in use at the end of 2018.  Higher values result in the use of more</span>
<span id="L519">                                ! robust and accurate forms of mathematically equivalent expressions.</span>
<span id="L520">REGRIDDING_ANSWER_DATE = 20181231 ! default = 99991231</span>
<span id="L521">                                ! The vintage of the expressions and order of arithmetic to use for regridding.</span>
<span id="L522">                                ! Values below 20190101 result in the use of older, less accurate expressions</span>
<span id="L523">                                ! that were in use at the end of 2018.  Higher values result in the use of more</span>
<span id="L524">                                ! robust and accurate forms of mathematically equivalent expressions.</span>
<span id="L525">BOUNDARY_EXTRAPOLATION = True   !   [Boolean] default = False</span>
<span id="L526">                                ! When defined, a proper high-order reconstruction scheme is used within</span>
<span id="L527">                                ! boundary cells rather than PCM. E.g., if PPM is used for remapping, a PPM</span>
<span id="L528">                                ! reconstruction will also be used within boundary cells.</span>
<span id="L529">ALE_COORDINATE_CONFIG = &quot;UNIFORM&quot; ! default = &quot;UNIFORM&quot;</span>
<span id="L530">                                ! Determines how to specify the coordinate resolution. Valid options are:</span>
<span id="L531">                                !  PARAM       - use the vector-parameter ALE_RESOLUTION</span>
<span id="L532">                                !  UNIFORM[:N] - uniformly distributed</span>
<span id="L533">                                !  FILE:string - read from a file. The string specifies</span>
<span id="L534">                                !                the filename and variable name, separated</span>
<span id="L535">                                !                by a comma or space, e.g. FILE:lev.nc,dz</span>
<span id="L536">                                !                or FILE:lev.nc,interfaces=zw</span>
<span id="L537">                                !  WOA09[:N]   - the WOA09 vertical grid (approximately)</span>
<span id="L538">                                !  WOA09INT[:N] - layers spanned by the WOA09 depths</span>
<span id="L539">                                !  WOA23INT[:N] - layers spanned by the WOA23 depths</span>
<span id="L540">                                !  FNC1:string - FNC1:dz_min,H_total,power,precision</span>
<span id="L541">                                !  HYBRID:string - read from a file. The string specifies</span>
<span id="L542">                                !                the filename and two variable names, separated</span>
<span id="L543">                                !                by a comma or space, for sigma-2 and dz.</span>
<span id="L544">                                !                e.g. HYBRID:vgrid.nc,sigma2,dz</span>
<span id="L545">                                !  HYBRID_3D:string - read from a file. The string specifies</span>
<span id="L546">                                !                the filename and two 3D variable names, separated</span>
<span id="L547">                                !                by a comma or space, for sigma-2 and dz. The</span>
<span id="L548">                                !                latter can be FNC1:string which is used everywhere.</span>
<span id="L549">                                !                e.g. HYBRID_3D:vgrid.nc,sigma2,dz</span>
<span id="L550">                                !  HYBRID_MAP:string - read from a file. The string specifies</span>
<span id="L551">                                !                the filename and three variable names, separated</span>
<span id="L552">                                !                by a comma or space, for map, sigma-2 and dz.</span>
<span id="L553">                                !                Map is a spatial index array with, maxval(map)=N,</span>
<span id="L554">                                !                and the others are 2D arrays containing N profiles.</span>
<span id="L555">                                !                Map typically contains integer values, but it can</span>
<span id="L556">                                !                contain real values, I+w, which imply using</span>
<span id="L557">                                !                the weighted sum of profiles I and I+1.</span>
<span id="L558">                                !                Dz can be FNC1:string which is used everywhere.</span>
<span id="L559">                                !                e.g. HYBRID_MAP:vgrid.nc,map,sigma2,dz</span>
<span id="L560">!ALE_RESOLUTION = 25*0.2        !   [kg m^-3]</span>
<span id="L561">                                ! The distribution of vertical resolution for the target</span>
<span id="L562">                                ! grid used for Eulerian-like coordinates. For example,</span>
<span id="L563">                                ! in z-coordinate mode, the parameter is a list of level</span>
<span id="L564">                                ! thicknesses (in m). In sigma-coordinate mode, the list</span>
<span id="L565">                                ! is of non-dimensional fractions of the water column.</span>
<span id="L566">!TARGET_DENSITIES = 1000.0, 1000.2, 1000.4000000000001, 1000.6000000000001, 1000.8000000000002, 1001.0000000000002, 1001.2000000000003, 1001.4000000000003, 1001.6000000000004, 1001.8000000000004, 1002.0000000000005, 1002.2000000000005, 1002.4000000000005, 1002.6000000000006, 1002.8000000000006, 1003.0000000000007, 1003.2000000000007, 1003.4000000000008, 1003.6000000000008, 1003.8000000000009, 1004.0000000000009, 1004.200000000001, 1004.400000000001, 1004.600000000001, 1004.8000000000011, 1005.0 !   [kg m-3]</span>
<span id="L567">                                ! RHO target densities for interfaces</span>
<span id="L568">REGRID_COMPRESSIBILITY_FRACTION = 0.0 !   [nondim] default = 0.0</span>
<span id="L569">                                ! When interpolating potential density profiles we can add some artificial</span>
<span id="L570">                                ! compressibility solely to make homogeneous regions appear stratified.</span>
<span id="L571">MIN_THICKNESS = 1.0E-04         !   [m] default = 0.001</span>
<span id="L572">                                ! When regridding, this is the minimum layer thickness allowed.</span>
<span id="L573">MAXIMUM_INT_DEPTH_CONFIG = &quot;NONE&quot; ! default = &quot;NONE&quot;</span>
<span id="L574">                                ! Determines how to specify the maximum interface depths.</span>
<span id="L575">                                ! Valid options are:</span>
<span id="L576">                                !  NONE        - there are no maximum interface depths</span>
<span id="L577">                                !  PARAM       - use the vector-parameter MAXIMUM_INTERFACE_DEPTHS</span>
<span id="L578">                                !  FILE:string - read from a file. The string specifies</span>
<span id="L579">                                !                the filename and variable name, separated</span>
<span id="L580">                                !                by a comma or space, e.g. FILE:lev.nc,Z</span>
<span id="L581">                                !  FNC1:string - FNC1:dz_min,H_total,power,precision</span>
<span id="L582">MAX_LAYER_THICKNESS_CONFIG = &quot;NONE&quot; ! default = &quot;NONE&quot;</span>
<span id="L583">                                ! Determines how to specify the maximum layer thicknesses.</span>
<span id="L584">                                ! Valid options are:</span>
<span id="L585">                                !  NONE        - there are no maximum layer thicknesses</span>
<span id="L586">                                !  PARAM       - use the vector-parameter MAX_LAYER_THICKNESS</span>
<span id="L587">                                !  FILE:string - read from a file. The string specifies</span>
<span id="L588">                                !                the filename and variable name, separated</span>
<span id="L589">                                !                by a comma or space, e.g. FILE:lev.nc,Z</span>
<span id="L590">                                !  FNC1:string - FNC1:dz_min,H_total,power,precision</span>
<span id="L591">REMAPPING_SCHEME = &quot;PPM_IH4&quot;    ! default = &quot;PLM&quot;</span>
<span id="L592">                                ! This sets the reconstruction scheme used for vertical remapping for all</span>
<span id="L593">                                ! variables. It can be one of the following schemes:</span>
<span id="L594">                                ! PCM         (1st-order accurate)</span>
<span id="L595">                                ! PLM         (2nd-order accurate)</span>
<span id="L596">                                ! PLM_HYBGEN  (2nd-order accurate)</span>
<span id="L597">                                ! PPM_H4      (3rd-order accurate)</span>
<span id="L598">                                ! PPM_IH4     (3rd-order accurate)</span>
<span id="L599">                                ! PPM_HYBGEN  (3rd-order accurate)</span>
<span id="L600">                                ! WENO_HYBGEN (3rd-order accurate)</span>
<span id="L601">                                ! PQM_IH4IH3  (4th-order accurate)</span>
<span id="L602">                                ! PQM_IH6IH5  (5th-order accurate)</span>
<span id="L603">VELOCITY_REMAPPING_SCHEME = &quot;PPM_IH4&quot; ! default = &quot;PPM_IH4&quot;</span>
<span id="L604">                                ! This sets the reconstruction scheme used for vertical remapping of velocities.</span>
<span id="L605">                                ! By default it is the same as REMAPPING_SCHEME. It can be one of the following</span>
<span id="L606">                                ! schemes:</span>
<span id="L607">                                ! PCM         (1st-order accurate)</span>
<span id="L608">                                ! PLM         (2nd-order accurate)</span>
<span id="L609">                                ! PLM_HYBGEN  (2nd-order accurate)</span>
<span id="L610">                                ! PPM_H4      (3rd-order accurate)</span>
<span id="L611">                                ! PPM_IH4     (3rd-order accurate)</span>
<span id="L612">                                ! PPM_HYBGEN  (3rd-order accurate)</span>
<span id="L613">                                ! WENO_HYBGEN (3rd-order accurate)</span>
<span id="L614">                                ! PQM_IH4IH3  (4th-order accurate)</span>
<span id="L615">                                ! PQM_IH6IH5  (5th-order accurate)</span>
<span id="L616">FATAL_CHECK_RECONSTRUCTIONS = False !   [Boolean] default = False</span>
<span id="L617">                                ! If true, cell-by-cell reconstructions are checked for consistency and if</span>
<span id="L618">                                ! non-monotonicity or an inconsistency is detected then a FATAL error is issued.</span>
<span id="L619">FATAL_CHECK_REMAPPING = False   !   [Boolean] default = False</span>
<span id="L620">                                ! If true, the results of remapping are checked for conservation and new extrema</span>
<span id="L621">                                ! and if an inconsistency is detected then a FATAL error is issued.</span>
<span id="L622">REMAP_BOUND_INTERMEDIATE_VALUES = False !   [Boolean] default = False</span>
<span id="L623">                                ! If true, the values on the intermediate grid used for remapping are forced to</span>
<span id="L624">                                ! be bounded, which might not be the case due to round off.</span>
<span id="L625">REMAP_BOUNDARY_EXTRAP = False   !   [Boolean] default = False</span>
<span id="L626">                                ! If true, values at the interfaces of boundary cells are extrapolated instead</span>
<span id="L627">                                ! of piecewise constant</span>
<span id="L628">INIT_BOUNDARY_EXTRAP = False    !   [Boolean] default = False</span>
<span id="L629">                                ! If true, values at the interfaces of boundary cells are extrapolated instead</span>
<span id="L630">                                ! of piecewise constant during initialization.Defaults to REMAP_BOUNDARY_EXTRAP.</span>
<span id="L631">REMAPPING_USE_OM4_SUBCELLS = True !   [Boolean] default = True</span>
<span id="L632">                                ! This selects the remapping algorithm used in OM4 that does not use the full</span>
<span id="L633">                                ! reconstruction for the top- and lower-most sub-layers, but instead assumes</span>
<span id="L634">                                ! they are always vanished (untrue) and so just uses their edge values. We</span>
<span id="L635">                                ! recommend setting this option to false.</span>
<span id="L636">PARTIAL_CELL_VELOCITY_REMAP = False !   [Boolean] default = False</span>
<span id="L637">                                ! If true, use partial cell thicknesses at velocity points that are masked out</span>
<span id="L638">                                ! where they extend below the shallower of the neighboring bathymetry for</span>
<span id="L639">                                ! remapping velocity.</span>
<span id="L640">REMAP_AFTER_INITIALIZATION = True !   [Boolean] default = True</span>
<span id="L641">                                ! If true, applies regridding and remapping immediately after initialization so</span>
<span id="L642">                                ! that the state is ALE consistent. This is a legacy step and should not be</span>
<span id="L643">                                ! needed if the initialization is consistent with the coordinate mode.</span>
<span id="L644">REGRID_TIME_SCALE = 0.0         !   [s] default = 0.0</span>
<span id="L645">                                ! The time-scale used in blending between the current (old) grid and the target</span>
<span id="L646">                                ! (new) grid. A short time-scale favors the target grid (0. or anything less</span>
<span id="L647">                                ! than DT_THERM) has no memory of the old grid. A very long time-scale makes the</span>
<span id="L648">                                ! model more Lagrangian.</span>
<span id="L649">REGRID_FILTER_SHALLOW_DEPTH = 0.0 !   [m] default = 0.0</span>
<span id="L650">                                ! The depth above which no time-filtering is applied. Above this depth final</span>
<span id="L651">                                ! grid exactly matches the target (new) grid.</span>
<span id="L652">REGRID_FILTER_DEEP_DEPTH = 0.0  !   [m] default = 0.0</span>
<span id="L653">                                ! The depth below which full time-filtering is applied with time-scale</span>
<span id="L654">                                ! REGRID_TIME_SCALE. Between depths REGRID_FILTER_SHALLOW_DEPTH and</span>
<span id="L655">                                ! REGRID_FILTER_SHALLOW_DEPTH the filter weights adopt a cubic profile.</span>
<span id="L656">REMAP_VEL_MASK_BBL_THICK = -0.001 !   [m] default = -0.001</span>
<span id="L657">                                ! A thickness of a bottom boundary layer below which velocities in thin layers</span>
<span id="L658">                                ! are zeroed out after remapping, following practice with Hybgen remapping, or a</span>
<span id="L659">                                ! negative value to avoid such filtering altogether.</span>
<span id="L660">REMAP_VEL_CONSERVE_KE = False   !   [Boolean] default = False</span>
<span id="L661">                                ! If true, a correction is applied to the baroclinic component of velocity after</span>
<span id="L662">                                ! remapping so that total KE is conserved. KE may not be conserved when</span>
<span id="L663">                                ! (CS%BBL_h_vel_mask &gt; 0.0) .and. (CS%h_vel_mask &gt; 0.0)</span>
<span id="L664"></span>
<span id="L665">! === module MOM_state_initialization ===</span>
<span id="L666">FATAL_INCONSISTENT_RESTART_TIME = False !   [Boolean] default = False</span>
<span id="L667">                                ! If true and a time_in value is provided to MOM_initialize_state, verify that</span>
<span id="L668">                                ! the time read from a restart file is the same as time_in, and issue a fatal</span>
<span id="L669">                                ! error if it is not.  Otherwise, simply set the time to time_in if present.</span>
<span id="L670">INIT_LAYERS_FROM_Z_FILE = False !   [Boolean] default = False</span>
<span id="L671">                                ! If true, initialize the layer thicknesses, temperatures, and salinities from a</span>
<span id="L672">                                ! Z-space file on a latitude-longitude grid.</span>
<span id="L673">THICKNESS_CONFIG = &quot;adjustment2d&quot; ! default = &quot;uniform&quot;</span>
<span id="L674">                                ! A string that determines how the initial layer thicknesses are specified for a</span>
<span id="L675">                                ! new run:</span>
<span id="L676">                                !     file - read interface heights from the file specified</span>
<span id="L677">                                !       by (THICKNESS_FILE).</span>
<span id="L678">                                !     thickness_file - read thicknesses from the file specified</span>
<span id="L679">                                !       by (THICKNESS_FILE).</span>
<span id="L680">                                !     mass_file - read thicknesses in units of mass per unit area from the file</span>
<span id="L681">                                !       specified by (THICKNESS_FILE).</span>
<span id="L682">                                !     coord - determined by ALE coordinate.</span>
<span id="L683">                                !     uniform - uniform thickness layers evenly distributed</span>
<span id="L684">                                !       between the surface and MAXIMUM_DEPTH.</span>
<span id="L685">                                !     list - read a list of positive interface depths.</span>
<span id="L686">                                !     param - use thicknesses from parameter THICKNESS_INIT_VALUES.</span>
<span id="L687">                                !     DOME - use a slope and channel configuration for the</span>
<span id="L688">                                !       DOME sill-overflow test case.</span>
<span id="L689">                                !     ISOMIP - use a configuration for the</span>
<span id="L690">                                !       ISOMIP test case.</span>
<span id="L691">                                !     benchmark - use the benchmark test case thicknesses.</span>
<span id="L692">                                !     Neverworld - use the Neverworld test case thicknesses.</span>
<span id="L693">                                !     search - search a density profile for the interface</span>
<span id="L694">                                !       densities. This is not yet implemented.</span>
<span id="L695">                                !     circle_obcs - the circle_obcs test case is used.</span>
<span id="L696">                                !     DOME2D - 2D version of DOME initialization.</span>
<span id="L697">                                !     adjustment2d - 2D lock exchange thickness ICs.</span>
<span id="L698">                                !     sloshing - sloshing gravity thickness ICs.</span>
<span id="L699">                                !     seamount - no motion test with seamount ICs.</span>
<span id="L700">                                !     dumbbell - sloshing channel ICs.</span>
<span id="L701">                                !     soliton - Equatorial Rossby soliton.</span>
<span id="L702">                                !     rossby_front - a mixed layer front in thermal wind balance.</span>
<span id="L703">                                !     USER - call a user modified routine.</span>
<span id="L704"></span>
<span id="L705">! === module adjustment_initialization ===</span>
<span id="L706">S_REF = 0.0                     !   [ppt] default = 35.0</span>
<span id="L707">                                ! Reference salinity</span>
<span id="L708">ADJUSTMENT_WIDTH = 0.01         !   [km]</span>
<span id="L709">                                ! Width of frontal zone</span>
<span id="L710">DELTA_S_STRAT = 0.0             !   [ppt]</span>
<span id="L711">                                ! Top-to-bottom salinity difference of stratification</span>
<span id="L712">ADJUSTMENT_DELTAS = 5.0         !   [ppt]</span>
<span id="L713">                                ! Salinity difference across front</span>
<span id="L714">FRONT_WAVE_AMP = 0.0            !   [km] default = 0.0</span>
<span id="L715">                                ! Amplitude of trans-frontal wave perturbation</span>
<span id="L716">FRONT_WAVE_LENGTH = 0.0         !   [km] default = 0.0</span>
<span id="L717">                                ! Wave-length of trans-frontal wave perturbation</span>
<span id="L718">FRONT_WAVE_ASYM = 0.0           !   [km] default = 0.0</span>
<span id="L719">                                ! Amplitude of frontal asymmetric perturbation</span>
<span id="L720">TS_CONFIG = &quot;adjustment2d&quot;      !</span>
<span id="L721">                                ! A string that determines how the initial temperatures and salinities are</span>
<span id="L722">                                ! specified for a new run:</span>
<span id="L723">                                !     file - read velocities from the file specified</span>
<span id="L724">                                !       by (TS_FILE).</span>
<span id="L725">                                !     fit - find the temperatures that are consistent with</span>
<span id="L726">                                !       the layer densities and salinity S_REF.</span>
<span id="L727">                                !     TS_profile - use temperature and salinity profiles</span>
<span id="L728">                                !       (read from TS_FILE) to set layer densities.</span>
<span id="L729">                                !     benchmark - use the benchmark test case T &amp; S.</span>
<span id="L730">                                !     linear - linear in logical layer space.</span>
<span id="L731">                                !     DOME2D - 2D DOME initialization.</span>
<span id="L732">                                !     ISOMIP - ISOMIP initialization.</span>
<span id="L733">                                !     adjustment2d - 2d lock exchange T/S ICs.</span>
<span id="L734">                                !     sloshing - sloshing mode T/S ICs.</span>
<span id="L735">                                !     seamount - no motion test with seamount ICs.</span>
<span id="L736">                                !     dumbbell - sloshing channel ICs.</span>
<span id="L737">                                !     rossby_front - a mixed layer front in thermal wind balance.</span>
<span id="L738">                                !     SCM_CVMix_tests - used in the SCM CVMix tests.</span>
<span id="L739">                                !     USER - call a user modified routine.</span>
<span id="L740">T_REF = 0.0                     !   [degC]</span>
<span id="L741">                                ! Reference temperature</span>
<span id="L742">S_RANGE = 5.0                   !   [ppt] default = 2.0</span>
<span id="L743">                                ! Initial salinity range</span>
<span id="L744">T_RANGE = 1.0                   !   [degC] default = 1.0</span>
<span id="L745">                                ! Initial temperature range</span>
<span id="L746">DEPRESS_INITIAL_SURFACE = False !   [Boolean] default = False</span>
<span id="L747">                                ! If true,  depress the initial surface to avoid huge tsunamis when a large</span>
<span id="L748">                                ! surface pressure is applied.</span>
<span id="L749">TRIM_IC_FOR_P_SURF = False      !   [Boolean] default = False</span>
<span id="L750">                                ! If true, cuts way the top of the column for initial conditions at the depth</span>
<span id="L751">                                ! where the hydrostatic pressure matches the imposed surface pressure which is</span>
<span id="L752">                                ! read from file.</span>
<span id="L753">REGRID_ACCELERATE_INIT = False  !   [Boolean] default = False</span>
<span id="L754">                                ! If true, runs REGRID_ACCELERATE_ITERATIONS iterations of the regridding</span>
<span id="L755">                                ! algorithm to push the initial grid to be consistent with the initial</span>
<span id="L756">                                ! condition. Useful only for state-based and iterative coordinates.</span>
<span id="L757">VELOCITY_CONFIG = &quot;zero&quot;        ! default = &quot;zero&quot;</span>
<span id="L758">                                ! A string that determines how the initial velocities are specified for a new</span>
<span id="L759">                                ! run:</span>
<span id="L760">                                !     file - read velocities from the file specified</span>
<span id="L761">                                !       by (VELOCITY_FILE).</span>
<span id="L762">                                !     zero - the fluid is initially at rest.</span>
<span id="L763">                                !     uniform - the flow is uniform (determined by</span>
<span id="L764">                                !       parameters INITIAL_U_CONST and INITIAL_V_CONST).</span>
<span id="L765">                                !     rossby_front - a mixed layer front in thermal wind balance.</span>
<span id="L766">                                !     soliton - Equatorial Rossby soliton.</span>
<span id="L767">                                !     USER - call a user modified routine.</span>
<span id="L768">ODA_INCUPD = False              !   [Boolean] default = False</span>
<span id="L769">                                ! If true, oda incremental updates will be applied everywhere in the domain.</span>
<span id="L770">SPONGE = False                  !   [Boolean] default = False</span>
<span id="L771">                                ! If true, sponges may be applied anywhere in the domain. The exact location and</span>
<span id="L772">                                ! properties of those sponges are specified via SPONGE_CONFIG.</span>
<span id="L773"></span>
<span id="L774">! === module MOM_diag_mediator ===</span>
<span id="L775">NUM_DIAG_COORDS = 1             ! default = 1</span>
<span id="L776">                                ! The number of diagnostic vertical coordinates to use. For each coordinate, an</span>
<span id="L777">                                ! entry in DIAG_COORDS must be provided.</span>
<span id="L778">DIAG_REMAPPING_USE_OM4_SUBCELLS = True !   [Boolean] default = True</span>
<span id="L779">                                ! If true, use the OM4 remapping-via-subcells algorithm for diagnostics. See</span>
<span id="L780">                                ! REMAPPING_USE_OM4_SUBCELLS for details. We recommend setting this option to</span>
<span id="L781">                                ! false.</span>
<span id="L782">USE_INDEX_DIAGNOSTIC_AXES = False !   [Boolean] default = False</span>
<span id="L783">                                ! If true, use a grid index coordinate convention for diagnostic axes.</span>
<span id="L784">DIAG_COORDS = &quot;z Z ZSTAR&quot;       ! default = &quot;z Z ZSTAR&quot;</span>
<span id="L785">                                ! A list of string tuples associating diag_table modules to a coordinate</span>
<span id="L786">                                ! definition used for diagnostics. Each string is of the form &quot;MODULE_SUFFIX</span>
<span id="L787">                                ! PARAMETER_SUFFIX COORDINATE_NAME&quot;.</span>
<span id="L788">DIAG_MISVAL = 1.0E+20           !   [various] default = 1.0E+20</span>
<span id="L789">                                ! Set the default missing value to use for diagnostics.</span>
<span id="L790">DIAG_AS_CHKSUM = False          !   [Boolean] default = False</span>
<span id="L791">                                ! Instead of writing diagnostics to the diag manager, write a text file</span>
<span id="L792">                                ! containing the checksum (bitcount) of the array.</span>
<span id="L793">AVAILABLE_DIAGS_FILE = &quot;available_diags.000000&quot; ! default = &quot;available_diags.000000&quot;</span>
<span id="L794">                                ! A file into which to write a list of all available ocean diagnostics that can</span>
<span id="L795">                                ! be included in a diag_table.</span>
<span id="L796">DIAG_COORD_DEF_Z = &quot;UNIFORM&quot;    ! default = &quot;UNIFORM&quot;</span>
<span id="L797">                                ! Determines how to specify the coordinate resolution. Valid options are:</span>
<span id="L798">                                !  PARAM       - use the vector-parameter DIAG_COORD_RES_Z</span>
<span id="L799">                                !  UNIFORM[:N] - uniformly distributed</span>
<span id="L800">                                !  FILE:string - read from a file. The string specifies</span>
<span id="L801">                                !                the filename and variable name, separated</span>
<span id="L802">                                !                by a comma or space, e.g. FILE:lev.nc,dz</span>
<span id="L803">                                !                or FILE:lev.nc,interfaces=zw</span>
<span id="L804">                                !  WOA09[:N]   - the WOA09 vertical grid (approximately)</span>
<span id="L805">                                !  WOA09INT[:N] - layers spanned by the WOA09 depths</span>
<span id="L806">                                !  WOA23INT[:N] - layers spanned by the WOA23 depths</span>
<span id="L807">                                !  FNC1:string - FNC1:dz_min,H_total,power,precision</span>
<span id="L808">                                !  HYBRID:string - read from a file. The string specifies</span>
<span id="L809">                                !                the filename and two variable names, separated</span>
<span id="L810">                                !                by a comma or space, for sigma-2 and dz.</span>
<span id="L811">                                !                e.g. HYBRID:vgrid.nc,sigma2,dz</span>
<span id="L812">                                !  HYBRID_3D:string - read from a file. The string specifies</span>
<span id="L813">                                !                the filename and two 3D variable names, separated</span>
<span id="L814">                                !                by a comma or space, for sigma-2 and dz. The</span>
<span id="L815">                                !                latter can be FNC1:string which is used everywhere.</span>
<span id="L816">                                !                e.g. HYBRID_3D:vgrid.nc,sigma2,dz</span>
<span id="L817">                                !  HYBRID_MAP:string - read from a file. The string specifies</span>
<span id="L818">                                !                the filename and three variable names, separated</span>
<span id="L819">                                !                by a comma or space, for map, sigma-2 and dz.</span>
<span id="L820">                                !                Map is a spatial index array with, maxval(map)=N,</span>
<span id="L821">                                !                and the others are 2D arrays containing N profiles.</span>
<span id="L822">                                !                Map typically contains integer values, but it can</span>
<span id="L823">                                !                contain real values, I+w, which imply using</span>
<span id="L824">                                !                the weighted sum of profiles I and I+1.</span>
<span id="L825">                                !                Dz can be FNC1:string which is used everywhere.</span>
<span id="L826">                                !                e.g. HYBRID_MAP:vgrid.nc,map,sigma2,dz</span>
<span id="L827"></span>
<span id="L828">! === module MOM_MEKE ===</span>
<span id="L829">USE_MEKE = False                !   [Boolean] default = False</span>
<span id="L830">                                ! If true, turns on the MEKE scheme which calculates a sub-grid mesoscale eddy</span>
<span id="L831">                                ! kinetic energy budget.</span>
<span id="L832"></span>
<span id="L833">! === module MOM_lateral_mixing_coeffs ===</span>
<span id="L834">USE_VARIABLE_MIXING = False     !   [Boolean] default = False</span>
<span id="L835">                                ! If true, the variable mixing code will be called.  This allows diagnostics to</span>
<span id="L836">                                ! be created even if the scheme is not used.  If KHTR_SLOPE_CFF&gt;0 or</span>
<span id="L837">                                ! KhTh_Slope_Cff&gt;0, this is set to true regardless of what is in the parameter</span>
<span id="L838">                                ! file.</span>
<span id="L839">USE_VISBECK = False             !   [Boolean] default = False</span>
<span id="L840">                                ! If true, use the Visbeck et al. (1997) formulation for</span>
<span id="L841">                                ! thickness diffusivity.</span>
<span id="L842">RESOLN_SCALED_KH = False        !   [Boolean] default = False</span>
<span id="L843">                                ! If true, the Laplacian lateral viscosity is scaled away when the first</span>
<span id="L844">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L845">DEPTH_SCALED_KHTH = False       !   [Boolean] default = False</span>
<span id="L846">                                ! If true, KHTH is scaled away when the depth is shallowerthan a reference</span>
<span id="L847">                                ! depth: KHTH = MIN(1,H/H0)**N * KHTH, where H0 is a reference depth, controlled</span>
<span id="L848">                                ! via DEPTH_SCALED_KHTH_H0, and the exponent (N) is controlled via</span>
<span id="L849">                                ! DEPTH_SCALED_KHTH_EXP.</span>
<span id="L850">RESOLN_SCALED_KHTH = False      !   [Boolean] default = False</span>
<span id="L851">                                ! If true, the interface depth diffusivity is scaled away when the first</span>
<span id="L852">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L853">RESOLN_SCALED_KHTR = False      !   [Boolean] default = False</span>
<span id="L854">                                ! If true, the epipycnal tracer diffusivity is scaled away when the first</span>
<span id="L855">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L856">RESOLN_USE_EBT = False          !   [Boolean] default = False</span>
<span id="L857">                                ! If true, uses the equivalent barotropic wave speed instead of first baroclinic</span>
<span id="L858">                                ! wave for calculating the resolution fn.</span>
<span id="L859">BACKSCAT_EBT_POWER = 0.0        !   [nondim] default = 0.0</span>
<span id="L860">                                ! Power to raise EBT vertical structure to when backscatter has vertical</span>
<span id="L861">                                ! structure.</span>
<span id="L862">BS_USE_SQG_STRUCT = False       !   [Boolean] default = False</span>
<span id="L863">                                ! If true, the SQG vertical structure is used for backscatter on the condition</span>
<span id="L864">                                ! that BS_EBT_power=0</span>
<span id="L865">KHTH_USE_EBT_STRUCT = False     !   [Boolean] default = False</span>
<span id="L866">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L867">                                ! thickness diffusivity.</span>
<span id="L868">KHTH_USE_SQG_STRUCT = False     !   [Boolean] default = False</span>
<span id="L869">                                ! If true, uses the surface quasigeostrophic structure as the vertical structure</span>
<span id="L870">                                ! of thickness diffusivity.</span>
<span id="L871">KHTR_USE_EBT_STRUCT = False     !   [Boolean] default = False</span>
<span id="L872">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L873">                                ! tracer diffusivity.</span>
<span id="L874">KHTR_USE_SQG_STRUCT = False     !   [Boolean] default = False</span>
<span id="L875">                                ! If true, uses the surface quasigeostrophic structure as the vertical structure</span>
<span id="L876">                                ! of tracer diffusivity.</span>
<span id="L877">KD_GL90_USE_EBT_STRUCT = False  !   [Boolean] default = False</span>
<span id="L878">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L879">                                ! diffusivity in the GL90 scheme.</span>
<span id="L880">KD_GL90_USE_SQG_STRUCT = False  !   [Boolean] default = False</span>
<span id="L881">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L882">                                ! diffusivity in the GL90 scheme.</span>
<span id="L883">KHTH_SLOPE_CFF = 0.0            !   [nondim] default = 0.0</span>
<span id="L884">                                ! The nondimensional coefficient in the Visbeck formula for the interface depth</span>
<span id="L885">                                ! diffusivity</span>
<span id="L886">KHTR_SLOPE_CFF = 0.0            !   [nondim] default = 0.0</span>
<span id="L887">                                ! The nondimensional coefficient in the Visbeck formula for the epipycnal tracer</span>
<span id="L888">                                ! diffusivity</span>
<span id="L889">USE_STORED_SLOPES = False       !   [Boolean] default = False</span>
<span id="L890">                                ! If true, the isopycnal slopes are calculated once and stored for re-use. This</span>
<span id="L891">                                ! uses more memory but avoids calling the equation of state more times than</span>
<span id="L892">                                ! should be necessary.</span>
<span id="L893">VERY_SMALL_FREQUENCY = 1.0E-17  !   [s-1] default = 1.0E-17</span>
<span id="L894">                                ! A miniscule frequency that is used to avoid division by 0.  The default value</span>
<span id="L895">                                ! is roughly (pi / (the age of the universe)).</span>
<span id="L896">USE_STANLEY_ISO = False         !   [Boolean] default = False</span>
<span id="L897">                                ! If true, turn on Stanley SGS T variance parameterization in isopycnal slope</span>
<span id="L898">                                ! code.</span>
<span id="L899">KD_SMOOTH = 1.0E-06             !   [m2 s-1] default = 1.0E-06</span>
<span id="L900">                                ! A diapycnal diffusivity that is used to interpolate more sensible values of T</span>
<span id="L901">                                ! &amp; S into thin layers.</span>
<span id="L902">USE_QG_LEITH_GM = False         !   [Boolean] default = False</span>
<span id="L903">                                ! If true, use the QG Leith viscosity as the GM coefficient.</span>
<span id="L904"></span>
<span id="L905">! === module MOM_set_visc ===</span>
<span id="L906">SET_VISC_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L907">                                ! The vintage of the order of arithmetic and expressions in the set viscosity</span>
<span id="L908">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L909">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L910">BOTTOMDRAGLAW = True            !   [Boolean] default = True</span>
<span id="L911">                                ! If true, the bottom stress is calculated with a drag law of the form</span>
<span id="L912">                                ! c_drag*|u|*u. The velocity magnitude may be an assumed value or it may be</span>
<span id="L913">                                ! based on the actual velocity in the bottommost HBBL, depending on LINEAR_DRAG.</span>
<span id="L914">DRAG_AS_BODY_FORCE = False      !   [Boolean] default = False</span>
<span id="L915">                                ! If true, the bottom stress is imposed as an explicit body force applied over a</span>
<span id="L916">                                ! fixed distance from the bottom, rather than as an implicit calculation based</span>
<span id="L917">                                ! on an enhanced near-bottom viscosity. The thickness of the bottom boundary</span>
<span id="L918">                                ! layer is HBBL.</span>
<span id="L919">CHANNEL_DRAG = False            !   [Boolean] default = False</span>
<span id="L920">                                ! If true, the bottom drag is exerted directly on each layer proportional to the</span>
<span id="L921">                                ! fraction of the bottom it overlies.</span>
<span id="L922">LINEAR_DRAG = False             !   [Boolean] default = False</span>
<span id="L923">                                ! If LINEAR_DRAG and BOTTOMDRAGLAW are defined the drag law is</span>
<span id="L924">                                ! cdrag*DRAG_BG_VEL*u.</span>
<span id="L925">DYNAMIC_VISCOUS_ML = False      !   [Boolean] default = False</span>
<span id="L926">                                ! If true, use a bulk Richardson number criterion to determine the mixed layer</span>
<span id="L927">                                ! thickness for viscosity.</span>
<span id="L928">OMEGA = 7.2921E-05              !   [s-1] default = 7.2921E-05</span>
<span id="L929">                                ! The rotation rate of the earth.</span>
<span id="L930">HBBL = 0.001                    !   [m]</span>
<span id="L931">                                ! The thickness of a bottom boundary layer with a viscosity increased by</span>
<span id="L932">                                ! KV_EXTRA_BBL if BOTTOMDRAGLAW is not defined, or the thickness over which</span>
<span id="L933">                                ! near-bottom velocities are averaged for the drag law if BOTTOMDRAGLAW is</span>
<span id="L934">                                ! defined but LINEAR_DRAG is not.</span>
<span id="L935">CDRAG = 0.0                     !   [nondim] default = 0.003</span>
<span id="L936">                                ! CDRAG is the drag coefficient relating the magnitude of the velocity field to</span>
<span id="L937">                                ! the bottom stress. CDRAG is only used if BOTTOMDRAGLAW is defined.</span>
<span id="L938">BBL_USE_TIDAL_BG = False        !   [Boolean] default = False</span>
<span id="L939">                                ! Flag to use the tidal RMS amplitude in place of constant background velocity</span>
<span id="L940">                                ! for computing u* in the BBL. This flag is only used when BOTTOMDRAGLAW is true</span>
<span id="L941">                                ! and LINEAR_DRAG is false.</span>
<span id="L942">DRAG_BG_VEL = 0.0               !   [m s-1] default = 0.0</span>
<span id="L943">                                ! DRAG_BG_VEL is either the assumed bottom velocity (with LINEAR_DRAG) or an</span>
<span id="L944">                                ! unresolved  velocity that is combined with the resolved velocity to estimate</span>
<span id="L945">                                ! the velocity magnitude.  DRAG_BG_VEL is only used when BOTTOMDRAGLAW is</span>
<span id="L946">                                ! defined.</span>
<span id="L947">BBL_USE_EOS = True              !   [Boolean] default = True</span>
<span id="L948">                                ! If true, use the equation of state in determining the properties of the bottom</span>
<span id="L949">                                ! boundary layer.  Otherwise use the layer target potential densities.  The</span>
<span id="L950">                                ! default of this parameter is the value of USE_EOS.</span>
<span id="L951">BBL_THICK_MIN = 0.01            !   [m] default = 0.0</span>
<span id="L952">                                ! The minimum bottom boundary layer thickness that can be used with</span>
<span id="L953">                                ! BOTTOMDRAGLAW. This might be Kv/(cdrag*drag_bg_vel) to give Kv as the minimum</span>
<span id="L954">                                ! near-bottom viscosity.</span>
<span id="L955">HTBL_SHELF_MIN = 0.01           !   [m] default = 0.01</span>
<span id="L956">                                ! The minimum top boundary layer thickness that can be used with BOTTOMDRAGLAW.</span>
<span id="L957">                                ! This might be Kv/(cdrag*drag_bg_vel) to give Kv as the minimum near-top</span>
<span id="L958">                                ! viscosity.</span>
<span id="L959">HTBL_SHELF = 0.001              !   [m] default = 0.001</span>
<span id="L960">                                ! The thickness over which near-surface velocities are averaged for the drag law</span>
<span id="L961">                                ! under an ice shelf.  By default this is the same as HBBL</span>
<span id="L962">KV = 1.0E-06                    !   [m2 s-1]</span>
<span id="L963">                                ! The background kinematic viscosity in the interior. The molecular value, ~1e-6</span>
<span id="L964">                                ! m2 s-1, may be used.</span>
<span id="L965">KV_BBL_MIN = 1.0E-06            !   [m2 s-1] default = 1.0E-06</span>
<span id="L966">                                ! The minimum viscosities in the bottom boundary layer.</span>
<span id="L967">KV_TBL_MIN = 1.0E-06            !   [m2 s-1] default = 1.0E-06</span>
<span id="L968">                                ! The minimum viscosities in the top boundary layer.</span>
<span id="L969">CORRECT_BBL_BOUNDS = False      !   [Boolean] default = False</span>
<span id="L970">                                ! If true, uses the correct bounds on the BBL thickness and viscosity so that</span>
<span id="L971">                                ! the bottom layer feels the intended drag.</span>
<span id="L972"></span>
<span id="L973">! === module MOM_thickness_diffuse ===</span>
<span id="L974">KHTH = 1.0E-04                  !   [m2 s-1] default = 0.0</span>
<span id="L975">                                ! The background horizontal thickness diffusivity.</span>
<span id="L976">READ_KHTH = False               !   [Boolean] default = False</span>
<span id="L977">                                ! If true, read a file (given by KHTH_FILE) containing the spatially varying</span>
<span id="L978">                                ! horizontal isopycnal height diffusivity.</span>
<span id="L979">KHTH_MIN = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L980">                                ! The minimum horizontal thickness diffusivity.</span>
<span id="L981">KHTH_MAX = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L982">                                ! The maximum horizontal thickness diffusivity.</span>
<span id="L983">KHTH_MAX_CFL = 0.8              !   [nondimensional] default = 0.8</span>
<span id="L984">                                ! The maximum value of the local diffusive CFL ratio that is permitted for the</span>
<span id="L985">                                ! thickness diffusivity. 1.0 is the marginally unstable value in a pure layered</span>
<span id="L986">                                ! model, but much smaller numbers (e.g. 0.1) seem to work better for ALE-based</span>
<span id="L987">                                ! models.</span>
<span id="L988">KH_ETA_CONST = 0.0              !   [m2 s-1] default = 0.0</span>
<span id="L989">                                ! The background horizontal diffusivity of the interface heights (without</span>
<span id="L990">                                ! considering the layer density structure).  If diffusive CFL limits are</span>
<span id="L991">                                ! encountered, the diffusivities of the isopycnals and the interfaces heights</span>
<span id="L992">                                ! are scaled back proportionately.</span>
<span id="L993">KH_ETA_VEL_SCALE = 0.0          !   [m s-1] default = 0.0</span>
<span id="L994">                                ! A velocity scale that is multiplied by the grid spacing to give a contribution</span>
<span id="L995">                                ! to the horizontal diffusivity of the interface heights (without considering</span>
<span id="L996">                                ! the layer density structure).</span>
<span id="L997">DETANGLE_INTERFACES = False     !   [Boolean] default = False</span>
<span id="L998">                                ! If defined add 3-d structured enhanced interface height diffusivities to</span>
<span id="L999">                                ! horizontally smooth jagged layers.</span>
<span id="L1000">KHTH_SLOPE_MAX = 0.01           !   [nondim] default = 0.01</span>
<span id="L1001">                                ! A slope beyond which the calculated isopycnal slope is not reliable and is</span>
<span id="L1002">                                ! scaled away.</span>
<span id="L1003">KHTH_USE_FGNV_STREAMFUNCTION = False !   [Boolean] default = False</span>
<span id="L1004">                                ! If true, use the streamfunction formulation of Ferrari et al., 2010, which</span>
<span id="L1005">                                ! effectively emphasizes graver vertical modes by smoothing in the vertical.</span>
<span id="L1006">USE_STANLEY_GM = False          !   [Boolean] default = False</span>
<span id="L1007">                                ! If true, turn on Stanley SGS T variance parameterization in GM code.</span>
<span id="L1008">MEKE_GM_SRC_ALT = False         !   [Boolean] default = False</span>
<span id="L1009">                                ! If true, use the GM energy conversion form S^2*N^2*kappa rather than the</span>
<span id="L1010">                                ! streamfunction for the GM source term.</span>
<span id="L1011">MEKE_GEOMETRIC = False          !   [Boolean] default = False</span>
<span id="L1012">                                ! If true, uses the GM coefficient formulation from the GEOMETRIC framework</span>
<span id="L1013">                                ! (Marshall et al., 2012).</span>
<span id="L1014">USE_GME = False                 !   [Boolean] default = False</span>
<span id="L1015">                                ! If true, use the GM+E backscatter scheme in association with the Gent and</span>
<span id="L1016">                                ! McWilliams parameterization.</span>
<span id="L1017">USE_GM_WORK_BUG = False         !   [Boolean] default = False</span>
<span id="L1018">                                ! If true, compute the top-layer work tendency on the u-grid with the incorrect</span>
<span id="L1019">                                ! sign, for legacy reproducibility.</span>
<span id="L1020">STOCH_EOS = False               !   [Boolean] default = False</span>
<span id="L1021">                                ! If true, stochastic perturbations are applied to the EOS in the PGF.</span>
<span id="L1022">STANLEY_COEFF = -1.0            !   [nondim] default = -1.0</span>
<span id="L1023">                                ! Coefficient correlating the temperature gradient and SGS T variance.</span>
<span id="L1024"></span>
<span id="L1025">! === module MOM_dynamics_split_RK2 ===</span>
<span id="L1026">TIDES = False                   !   [Boolean] default = False</span>
<span id="L1027">                                ! If true, apply tidal momentum forcing.</span>
<span id="L1028">CALCULATE_SAL = False           !   [Boolean] default = False</span>
<span id="L1029">                                ! If true, calculate self-attraction and loading.</span>
<span id="L1030">USE_HA = False                  !   [Boolean] default = False</span>
<span id="L1031">                                ! If true, perform inline harmonic analysis.</span>
<span id="L1032">BE = 0.6                        !   [nondim] default = 0.6</span>
<span id="L1033">                                ! If SPLIT is true, BE determines the relative weighting of a  2nd-order</span>
<span id="L1034">                                ! Runga-Kutta baroclinic time stepping scheme (0.5) and a backward Euler scheme</span>
<span id="L1035">                                ! (1) that is used for the Coriolis and inertial terms.  BE may be from 0.5 to</span>
<span id="L1036">                                ! 1, but instability may occur near 0.5. BE is also applicable if SPLIT is false</span>
<span id="L1037">                                ! and USE_RK2 is true.</span>
<span id="L1038">BEGW = 0.0                      !   [nondim] default = 0.0</span>
<span id="L1039">                                ! If SPLIT is true, BEGW is a number from 0 to 1 that controls the extent to</span>
<span id="L1040">                                ! which the treatment of gravity waves is forward-backward (0) or simulated</span>
<span id="L1041">                                ! backward Euler (1).  0 is almost always used. If SPLIT is false and USE_RK2 is</span>
<span id="L1042">                                ! true, BEGW can be between 0 and 0.5 to damp gravity waves.</span>
<span id="L1043">SET_DTBT_USE_BT_CONT = False    !   [Boolean] default = False</span>
<span id="L1044">                                ! If true, use BT_CONT to calculate DTBT if possible.</span>
<span id="L1045">SPLIT_BOTTOM_STRESS = False     !   [Boolean] default = False</span>
<span id="L1046">                                ! If true, provide the bottom stress calculated by the vertical viscosity to the</span>
<span id="L1047">                                ! barotropic solver.</span>
<span id="L1048">BT_USE_LAYER_FLUXES = True      !   [Boolean] default = True</span>
<span id="L1049">                                ! If true, use the summed layered fluxes plus an adjustment due to the change in</span>
<span id="L1050">                                ! the barotropic velocity in the barotropic continuity equation.</span>
<span id="L1051">BT_ADJ_CORR_MASS_SRC = True     !   [Boolean] default = True</span>
<span id="L1052">                                ! If true, recalculates the barotropic mass source after predictor step. This</span>
<span id="L1053">                                ! should make little difference in the deep ocean but appears to help for</span>
<span id="L1054">                                ! vanished layers. If false, uses the same mass source as from the predictor</span>
<span id="L1055">                                ! step.</span>
<span id="L1056">STORE_CORIOLIS_ACCEL = True     !   [Boolean] default = True</span>
<span id="L1057">                                ! If true, calculate the Coriolis accelerations at the end of each timestep for</span>
<span id="L1058">                                ! use in the predictor step of the next split RK2 timestep.</span>
<span id="L1059">FPMIX = False                   !   [Boolean] default = False</span>
<span id="L1060">                                ! If true, add non-local momentum flux increments and diffuse down the Eulerian</span>
<span id="L1061">                                ! gradient.</span>
<span id="L1062">VISC_REM_BUG = True             !   [Boolean] default = False</span>
<span id="L1063">                                ! If true, visc_rem_[uv] in split mode is incorrectly calculated or accounted</span>
<span id="L1064">                                ! for in two places. This parameter controls the defaults of two individual</span>
<span id="L1065">                                ! flags, VISC_REM_TIMESTEP_BUG in MOM_dynamics_split_RK2(b) and</span>
<span id="L1066">                                ! VISC_REM_BT_WEIGHT_BUG in MOM_barotropic.</span>
<span id="L1067">VISC_REM_TIMESTEP_BUG = True    !   [Boolean] default = True</span>
<span id="L1068">                                ! If true, recover a bug that uses dt_pred rather than dt in vertvisc_remnant()</span>
<span id="L1069">                                ! at the end of predictor stage for the following continuity() and btstep()</span>
<span id="L1070">                                ! calls in the corrector step. Default of this flag is set by VISC_REM_BUG</span>
<span id="L1071"></span>
<span id="L1072">! === module MOM_continuity_PPM ===</span>
<span id="L1073">MONOTONIC_CONTINUITY = False    !   [Boolean] default = False</span>
<span id="L1074">                                ! If true, CONTINUITY_PPM uses the Colella and Woodward monotonic limiter.  The</span>
<span id="L1075">                                ! default (false) is to use a simple positive definite limiter.</span>
<span id="L1076">SIMPLE_2ND_PPM_CONTINUITY = False !   [Boolean] default = False</span>
<span id="L1077">                                ! If true, CONTINUITY_PPM uses a simple 2nd order (arithmetic mean)</span>
<span id="L1078">                                ! interpolation of the edge values. This may give better PV conservation</span>
<span id="L1079">                                ! properties. While it formally reduces the accuracy of the continuity solver</span>
<span id="L1080">                                ! itself in the strongly advective limit, it does not reduce the overall order</span>
<span id="L1081">                                ! of accuracy of the dynamic core.</span>
<span id="L1082">UPWIND_1ST_CONTINUITY = False   !   [Boolean] default = False</span>
<span id="L1083">                                ! If true, CONTINUITY_PPM becomes a 1st-order upwind continuity solver.  This</span>
<span id="L1084">                                ! scheme is highly diffusive but may be useful for debugging or in single-column</span>
<span id="L1085">                                ! mode where its minimal stencil is useful.</span>
<span id="L1086">ETA_TOLERANCE = 1.0E-12         !   [m] default = 1.25E-14</span>
<span id="L1087">                                ! The tolerance for the differences between the barotropic and baroclinic</span>
<span id="L1088">                                ! estimates of the sea surface height due to the fluxes through each face.  The</span>
<span id="L1089">                                ! total tolerance for SSH is 4 times this value.  The default is</span>
<span id="L1090">                                ! 0.5*NK*ANGSTROM, and this should not be set less than about</span>
<span id="L1091">                                ! 10^-15*MAXIMUM_DEPTH.</span>
<span id="L1092">VELOCITY_TOLERANCE = 3.0E+08    !   [m s-1] default = 3.0E+08</span>
<span id="L1093">                                ! The tolerance for barotropic velocity discrepancies between the barotropic</span>
<span id="L1094">                                ! solution and  the sum of the layer thicknesses.</span>
<span id="L1095">CONT_PPM_AGGRESS_ADJUST = False !   [Boolean] default = False</span>
<span id="L1096">                                ! If true, allow the adjusted velocities to have a relative CFL change up to</span>
<span id="L1097">                                ! 0.5.</span>
<span id="L1098">CONT_PPM_VOLUME_BASED_CFL = False !   [Boolean] default = False</span>
<span id="L1099">                                ! If true, use the ratio of the open face lengths to the tracer cell areas when</span>
<span id="L1100">                                ! estimating CFL numbers.  The default is set by CONT_PPM_AGGRESS_ADJUST.</span>
<span id="L1101">CONTINUITY_CFL_LIMIT = 0.5      !   [nondim] default = 0.5</span>
<span id="L1102">                                ! The maximum CFL of the adjusted velocities.</span>
<span id="L1103">CONT_PPM_BETTER_ITER = True     !   [Boolean] default = True</span>
<span id="L1104">                                ! If true, stop corrective iterations using a velocity based criterion and only</span>
<span id="L1105">                                ! stop if the iteration is better than all predecessors.</span>
<span id="L1106">CONT_PPM_USE_VISC_REM_MAX = True !   [Boolean] default = True</span>
<span id="L1107">                                ! If true, use more appropriate limiting bounds for corrections in strongly</span>
<span id="L1108">                                ! viscous columns.</span>
<span id="L1109">CONT_PPM_MARGINAL_FACE_AREAS = True !   [Boolean] default = True</span>
<span id="L1110">                                ! If true, use the marginal face areas from the continuity solver for use as the</span>
<span id="L1111">                                ! weights in the barotropic solver. Otherwise use the transport averaged areas.</span>
<span id="L1112"></span>
<span id="L1113">! === module MOM_CoriolisAdv ===</span>
<span id="L1114">NOSLIP = False                  !   [Boolean] default = False</span>
<span id="L1115">                                ! If true, no slip boundary conditions are used; otherwise free slip boundary</span>
<span id="L1116">                                ! conditions are assumed. The implementation of the free slip BCs on a C-grid is</span>
<span id="L1117">                                ! much cleaner than the no slip BCs. The use of free slip BCs is strongly</span>
<span id="L1118">                                ! encouraged, and no slip BCs are not used with the biharmonic viscosity.</span>
<span id="L1119">CORIOLIS_EN_DIS = False         !   [Boolean] default = False</span>
<span id="L1120">                                ! If true, two estimates of the thickness fluxes are used to estimate the</span>
<span id="L1121">                                ! Coriolis term, and the one that dissipates energy relative to the other one is</span>
<span id="L1122">                                ! used.</span>
<span id="L1123">CORIOLIS_SCHEME = &quot;SADOURNY75_ENERGY&quot; ! default = &quot;SADOURNY75_ENERGY&quot;</span>
<span id="L1124">                                ! CORIOLIS_SCHEME selects the discretization for the Coriolis terms. Valid</span>
<span id="L1125">                                ! values are:</span>
<span id="L1126">                                !    SADOURNY75_ENERGY - Sadourny, 1975; energy cons.</span>
<span id="L1127">                                !    ARAKAWA_HSU90     - Arakawa &amp; Hsu, 1990</span>
<span id="L1128">                                !    SADOURNY75_ENSTRO - Sadourny, 1975; enstrophy cons.</span>
<span id="L1129">                                !    ARAKAWA_LAMB81    - Arakawa &amp; Lamb, 1981; En. + Enst.</span>
<span id="L1130">                                !    ARAKAWA_LAMB_BLEND - A blend of Arakawa &amp; Lamb with</span>
<span id="L1131">                                !                         Arakawa &amp; Hsu and Sadourny energy</span>
<span id="L1132">                                !    WENOVI5TH_PV_ENSTRO   - 5th-order WENO PV enstrophy</span>
<span id="L1133">                                !    WENOVI3RD_PV_ENSTRO   - 3rd-order WENO PV enstrophy</span>
<span id="L1134">                                !    WENOVI7TH_PV_ENSTRO  - 7th-order WENO PV enstrophy</span>
<span id="L1135">BOUND_CORIOLIS = True           !   [Boolean] default = False</span>
<span id="L1136">                                ! If true, the Coriolis terms at u-points are bounded by the four estimates of</span>
<span id="L1137">                                ! (f+rv)v from the four neighboring v-points, and similarly at v-points.  This</span>
<span id="L1138">                                ! option would have no effect on the SADOURNY Coriolis scheme if it were</span>
<span id="L1139">                                ! possible to use centered difference thickness fluxes.</span>
<span id="L1140">KE_SCHEME = &quot;KE_GUDONOV&quot;        ! default = &quot;KE_ARAKAWA&quot;</span>
<span id="L1141">                                ! KE_SCHEME selects the discretization for acceleration due to the kinetic</span>
<span id="L1142">                                ! energy gradient. Valid values are:</span>
<span id="L1143">                                !    KE_ARAKAWA, KE_SIMPLE_GUDONOV, KE_GUDONOV, KE_UP3</span>
<span id="L1144">PV_ADV_SCHEME = &quot;PV_ADV_CENTERED&quot; ! default = &quot;PV_ADV_CENTERED&quot;</span>
<span id="L1145">                                ! PV_ADV_SCHEME selects the discretization for PV advection. Valid values are:</span>
<span id="L1146">                                !    PV_ADV_CENTERED - centered (aka Sadourny, 75)</span>
<span id="L1147">                                !    PV_ADV_UPWIND1  - upwind, first order</span>
<span id="L1148"></span>
<span id="L1149">! === module MOM_PressureForce ===</span>
<span id="L1150">ANALYTIC_FV_PGF = True          !   [Boolean] default = True</span>
<span id="L1151">                                ! If true the pressure gradient forces are calculated with a finite volume form</span>
<span id="L1152">                                ! that analytically integrates the equations of state in pressure to avoid any</span>
<span id="L1153">                                ! possibility of numerical thermobaric instability, as described in Adcroft et</span>
<span id="L1154">                                ! al., O. Mod. (2008).</span>
<span id="L1155"></span>
<span id="L1156">! === module MOM_PressureForce_FV ===</span>
<span id="L1157">RHO_PGF_REF = 1000.0            !   [kg m-3] default = 1000.0</span>
<span id="L1158">                                ! The reference density that is subtracted off when calculating pressure</span>
<span id="L1159">                                ! gradient forces.  Its inverse is subtracted off of specific volumes when in</span>
<span id="L1160">                                ! non-Boussinesq mode.  The default is RHO_0.</span>
<span id="L1161">RHO_PGF_REF_BUG = True          !   [Boolean] default = True</span>
<span id="L1162">                                ! If true, recover a bug that RHO_0 (the mean seawater density in Boussinesq</span>
<span id="L1163">                                ! mode) and RHO_PGF_REF (the subtracted reference density in finite volume</span>
<span id="L1164">                                ! pressure gradient forces) are incorrectly interchanged in several instances in</span>
<span id="L1165">                                ! Boussinesq mode.</span>
<span id="L1166">SSH_IN_EOS_PRESSURE_FOR_PGF = False !   [Boolean] default = False</span>
<span id="L1167">                                ! If true, include contributions from the sea surface height in the height-based</span>
<span id="L1168">                                ! pressure used in the equation of state calculations for the Boussinesq</span>
<span id="L1169">                                ! pressure gradient forces, including adjustments for atmospheric or sea-ice</span>
<span id="L1170">                                ! pressure.</span>
<span id="L1171">MASS_WEIGHT_IN_PRESSURE_GRADIENT = False !   [Boolean] default = False</span>
<span id="L1172">                                ! If true, use mass weighting when interpolating T/S for integrals near the</span>
<span id="L1173">                                ! bathymetry in FV pressure gradient calculations.</span>
<span id="L1174">MASS_WEIGHT_IN_PRESSURE_GRADIENT_TOP = False !   [Boolean] default = False</span>
<span id="L1175">                                ! If true and MASS_WEIGHT_IN_PRESSURE_GRADIENT is true, use mass weighting when</span>
<span id="L1176">                                ! interpolating T/S for integrals near the top of the water column in FV</span>
<span id="L1177">                                ! pressure gradient calculations.</span>
<span id="L1178">MASS_WEIGHT_IN_PGF_VANISHED_ONLY = False !   [Boolean] default = False</span>
<span id="L1179">                                ! If true, use mass weighting when interpolating T/S for integrals only if one</span>
<span id="L1180">                                ! side is vanished according to RESET_INTXPA_H_NONVANISHED.</span>
<span id="L1181">CORRECTION_INTXPA = False       !   [Boolean] default = False</span>
<span id="L1182">                                ! If true, use a correction for surface pressure curvature in intx_pa.</span>
<span id="L1183">RESET_INTXPA_INTEGRAL = False   !   [Boolean] default = False</span>
<span id="L1184">                                ! If true, reset INTXPA to match pressures at first nonvanished cell. Includes</span>
<span id="L1185">                                ! pressure correction.</span>
<span id="L1186">RESET_INTXPA_INTEGRAL_FLATTEST = False !   [Boolean] default = False</span>
<span id="L1187">                                ! If true, use flattest interface as reference interface where there is no</span>
<span id="L1188">                                ! better choice for RESET_INTXPA_INTEGRAL. Otherwise, use surface interface.</span>
<span id="L1189">USE_INACCURATE_PGF_RHO_ANOM = False !   [Boolean] default = False</span>
<span id="L1190">                                ! If true, use a form of the PGF that uses the reference density in an</span>
<span id="L1191">                                ! inaccurate way. This is not recommended.</span>
<span id="L1192">RECONSTRUCT_FOR_PRESSURE = True !   [Boolean] default = True</span>
<span id="L1193">                                ! If True, use vertical reconstruction of T &amp; S within the integrals of the FV</span>
<span id="L1194">                                ! pressure gradient calculation. If False, use the constant-by-layer algorithm.</span>
<span id="L1195">                                ! The default is set by USE_REGRIDDING.</span>
<span id="L1196">PRESSURE_RECONSTRUCTION_SCHEME = 1 ! default = 1</span>
<span id="L1197">                                ! Order of vertical reconstruction of T/S to use in the integrals within the FV</span>
<span id="L1198">                                ! pressure gradient calculation.</span>
<span id="L1199">                                !  0: PCM or no reconstruction.</span>
<span id="L1200">                                !  1: PLM reconstruction.</span>
<span id="L1201">                                !  2: PPM reconstruction.</span>
<span id="L1202">BOUNDARY_EXTRAPOLATION_PRESSURE = True !   [Boolean] default = True</span>
<span id="L1203">                                ! If true, the reconstruction of T &amp; S for pressure in boundary cells is</span>
<span id="L1204">                                ! extrapolated, rather than using PCM in these cells. If true, the same order</span>
<span id="L1205">                                ! polynomial is used as is used for the interior cells.</span>
<span id="L1206">USE_STANLEY_PGF = False         !   [Boolean] default = False</span>
<span id="L1207">                                ! If true, turn on Stanley SGS T variance parameterization in PGF code.</span>
<span id="L1208"></span>
<span id="L1209">! === module MOM_Zanna_Bolton ===</span>
<span id="L1210">USE_ZB2020 = False              !   [Boolean] default = False</span>
<span id="L1211">                                ! If true, turns on Zanna-Bolton-2020 (ZB) subgrid momentum parameterization of</span>
<span id="L1212">                                ! mesoscale eddies.</span>
<span id="L1213"></span>
<span id="L1214">! === module MOM_hor_visc ===</span>
<span id="L1215">USE_CIRCULATION_IN_HORVISC = False !   [Boolean] default = False</span>
<span id="L1216">                                ! Use circulation theorem to compute vorticity in horvisc module (for ZB20 or</span>
<span id="L1217">                                ! Leith)</span>
<span id="L1218">USE_CONT_THICKNESS = False      !   [Boolean] default = False</span>
<span id="L1219">                                ! If true, use thickness at velocity points from continuity solver. This option</span>
<span id="L1220">                                ! currently only works with split mode.</span>
<span id="L1221">LAPLACIAN = True                !   [Boolean] default = False</span>
<span id="L1222">                                ! If true, use a Laplacian horizontal viscosity.</span>
<span id="L1223">KH = 0.0                        !   [m2 s-1] default = 0.0</span>
<span id="L1224">                                ! The background Laplacian horizontal viscosity.</span>
<span id="L1225">KH_BG_MIN = 0.0                 !   [m2 s-1] default = 0.0</span>
<span id="L1226">                                ! The minimum value allowed for Laplacian horizontal viscosity, KH.</span>
<span id="L1227">KH_VEL_SCALE = 0.0              !   [m s-1] default = 0.0</span>
<span id="L1228">                                ! The velocity scale which is multiplied by the grid spacing to calculate the</span>
<span id="L1229">                                ! Laplacian viscosity. The final viscosity is the largest of this scaled</span>
<span id="L1230">                                ! viscosity, the Smagorinsky and Leith viscosities, and KH.</span>
<span id="L1231">KH_SIN_LAT = 0.0                !   [m2 s-1] default = 0.0</span>
<span id="L1232">                                ! The amplitude of a latitudinally-dependent background viscosity of the form</span>
<span id="L1233">                                ! KH_SIN_LAT*(SIN(LAT)**KH_PWR_OF_SINE).</span>
<span id="L1234">SMAGORINSKY_KH = True           !   [Boolean] default = False</span>
<span id="L1235">                                ! If true, use a Smagorinsky nonlinear eddy viscosity.</span>
<span id="L1236">SMAG_LAP_CONST = 0.15           !   [nondim] default = 0.0</span>
<span id="L1237">                                ! The nondimensional Laplacian Smagorinsky constant, often 0.15.</span>
<span id="L1238">LEITH_KH = False                !   [Boolean] default = False</span>
<span id="L1239">                                ! If true, use a Leith nonlinear eddy viscosity.</span>
<span id="L1240">BOUND_KH = True                 !   [Boolean] default = True</span>
<span id="L1241">                                ! If true, the Laplacian coefficient is locally limited to be stable.</span>
<span id="L1242">EY24_EBT_BS = False             !   [Boolean] default = False</span>
<span id="L1243">                                ! If true, use the the backscatter scheme (EBT mode with kill switch)developed</span>
<span id="L1244">                                ! by Yankovsky et al. (2024).</span>
<span id="L1245">ANISOTROPIC_VISCOSITY = False   !   [Boolean] default = False</span>
<span id="L1246">                                ! If true, allow anistropic viscosity in the Laplacian horizontal viscosity.</span>
<span id="L1247">ADD_LES_VISCOSITY = False       !   [Boolean] default = False</span>
<span id="L1248">                                ! If true, adds the viscosity from Smagorinsky and Leith to the background</span>
<span id="L1249">                                ! viscosity instead of taking the maximum.</span>
<span id="L1250">BIHARMONIC = False              !   [Boolean] default = True</span>
<span id="L1251">                                ! If true, use a biharmonic horizontal viscosity. BIHARMONIC may be used with</span>
<span id="L1252">                                ! LAPLACIAN.</span>
<span id="L1253">USE_LEITHY = False              !   [Boolean] default = False</span>
<span id="L1254">                                ! If true, use a biharmonic Leith nonlinear eddy viscosity together with a</span>
<span id="L1255">                                ! harmonic backscatter.</span>
<span id="L1256">USE_LAND_MASK_FOR_HVISC = True  !   [Boolean] default = True</span>
<span id="L1257">                                ! If true, use the land mask for the computation of thicknesses at velocity</span>
<span id="L1258">                                ! locations. This eliminates the dependence on arbitrary values over land or</span>
<span id="L1259">                                ! outside of the domain.</span>
<span id="L1260">HORVISC_BOUND_COEF = 0.8        !   [nondim] default = 0.8</span>
<span id="L1261">                                ! The nondimensional coefficient of the ratio of the viscosity bounds to the</span>
<span id="L1262">                                ! theoretical maximum for stability without considering other terms.</span>
<span id="L1263">USE_KH_BG_2D = False            !   [Boolean] default = False</span>
<span id="L1264">                                ! If true, read a file containing 2-d background harmonic viscosities. The final</span>
<span id="L1265">                                ! viscosity is the maximum of the other terms and this background value.</span>
<span id="L1266">FRICTWORK_BUG = False           !   [Boolean] default = False</span>
<span id="L1267">                                ! If true, retain an answer-changing bug in calculating the FrictWork, which</span>
<span id="L1268">                                ! cancels the h in thickness flux and the h at velocity point. This isnot</span>
<span id="L1269">                                ! recommended.</span>
<span id="L1270"></span>
<span id="L1271">! === module MOM_vert_friction ===</span>
<span id="L1272">VERT_FRICTION_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1273">                                ! The vintage of the order of arithmetic and expressions in the viscous</span>
<span id="L1274">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L1275">                                ! while higher values use expressions that do not use an arbitrary hard-coded</span>
<span id="L1276">                                ! maximum viscous coupling coefficient between layers.  Values below 20230601</span>
<span id="L1277">                                ! recover a form of the viscosity within the mixed layer that breaks up the</span>
<span id="L1278">                                ! magnitude of the wind stress in some non-Boussinesq cases.</span>
<span id="L1279">DIRECT_STRESS = True            !   [Boolean] default = False</span>
<span id="L1280">                                ! If true, the wind stress is distributed over the topmost HMIX_STRESS of fluid</span>
<span id="L1281">                                ! (like in HYCOM), and an added mixed layer viscosity or a physically based</span>
<span id="L1282">                                ! boundary layer turbulence parameterization is not needed for stability.</span>
<span id="L1283">FIXED_DEPTH_LOTW_ML = False     !   [Boolean] default = False</span>
<span id="L1284">                                ! If true, use a Law-of-the-wall prescription for the mixed layer viscosity</span>
<span id="L1285">                                ! within a boundary layer that is the lesser of HMIX_FIXED and the total depth</span>
<span id="L1286">                                ! of the ocean in a column.</span>
<span id="L1287">LOTW_VISCOUS_ML_FLOOR = False   !   [Boolean] default = False</span>
<span id="L1288">                                ! If true, use a Law-of-the-wall prescription to set a lower bound on the</span>
<span id="L1289">                                ! viscous coupling between layers within the surface boundary layer, based the</span>
<span id="L1290">                                ! distance of interfaces from the surface.  This only acts when there are large</span>
<span id="L1291">                                ! changes in the thicknesses of successive layers or when the viscosity is set</span>
<span id="L1292">                                ! externally and the wind stress has subsequently increased.</span>
<span id="L1293">VON_KARMAN_CONST = 0.41         !   [nondim] default = 0.41</span>
<span id="L1294">                                ! The value the von Karman constant as used for mixed layer viscosity.</span>
<span id="L1295">HARMONIC_VISC = False           !   [Boolean] default = False</span>
<span id="L1296">                                ! If true, use the harmonic mean thicknesses for calculating the vertical</span>
<span id="L1297">                                ! viscosity.</span>
<span id="L1298">HARMONIC_BL_SCALE = 0.0         !   [nondim] default = 0.0</span>
<span id="L1299">                                ! A scale to determine when water is in the boundary layers based solely on</span>
<span id="L1300">                                ! harmonic mean thicknesses for the purpose of determining the extent to which</span>
<span id="L1301">                                ! the thicknesses used in the viscosities are upwinded.</span>
<span id="L1302">HMIX_FIXED = 1.0E-10            !   [m]</span>
<span id="L1303">                                ! The prescribed depth over which the near-surface viscosity and diffusivity are</span>
<span id="L1304">                                ! elevated when the bulk mixed layer is not used.</span>
<span id="L1305">HMIX_STRESS = 1.0E-10           !   [m] default = 1.0E-10</span>
<span id="L1306">                                ! The depth over which the wind stress is applied if DIRECT_STRESS is true.</span>
<span id="L1307">USE_GL90_IN_SSW = False         !   [Boolean] default = False</span>
<span id="L1308">                                ! If true, use simpler method to calculate 1/N^2 in GL90 vertical viscosity</span>
<span id="L1309">                                ! coefficient. This method is valid in stacked shallow water mode.</span>
<span id="L1310">KV_ML_INVZ2 = 0.0               !   [m2 s-1] default = 0.0</span>
<span id="L1311">                                ! An extra kinematic viscosity in a mixed layer of thickness HMIX_FIXED, with</span>
<span id="L1312">                                ! the actual viscosity scaling as 1/(z*HMIX_FIXED)^2, where z is the distance</span>
<span id="L1313">                                ! from the surface, to allow for finite wind stresses to be transmitted through</span>
<span id="L1314">                                ! infinitesimally thin surface layers.  This is an older option for numerical</span>
<span id="L1315">                                ! convenience without a strong physical basis, and its use is now discouraged.</span>
<span id="L1316">CFL_TRUNCATE = 0.5              !   [nondim] default = 0.5</span>
<span id="L1317">                                ! The value of the CFL number that will cause velocity components to be</span>
<span id="L1318">                                ! truncated; instability can occur past 0.5.</span>
<span id="L1319">CFL_REPORT = 0.5                !   [nondim] default = 0.5</span>
<span id="L1320">                                ! The value of the CFL number that causes accelerations to be reported; the</span>
<span id="L1321">                                ! default is CFL_TRUNCATE.</span>
<span id="L1322">CFL_TRUNCATE_RAMP_TIME = 0.0    !   [s] default = 0.0</span>
<span id="L1323">                                ! The time over which the CFL truncation value is ramped up at the beginning of</span>
<span id="L1324">                                ! the run.</span>
<span id="L1325">CFL_TRUNCATE_START = 0.0        !   [nondim] default = 0.0</span>
<span id="L1326">                                ! The start value of the truncation CFL number used when ramping up CFL_TRUNC.</span>
<span id="L1327">STOKES_MIXING_COMBINED = False  !   [Boolean] default = False</span>
<span id="L1328">                                ! Flag to use Stokes drift Mixing via the Lagrangian  current (Eulerian plus</span>
<span id="L1329">                                ! Stokes drift).  Still needs work and testing, so not recommended for use.</span>
<span id="L1330">VEL_UNDERFLOW = 1.0E-30         !   [m s-1] default = 0.0</span>
<span id="L1331">                                ! A negligibly small velocity magnitude below which velocity components are set</span>
<span id="L1332">                                ! to 0.  A reasonable value might be 1e-30 m/s, which is less than an Angstrom</span>
<span id="L1333">                                ! divided by the age of the universe.</span>
<span id="L1334"></span>
<span id="L1335">! === module MOM_barotropic ===</span>
<span id="L1336">USE_BT_CONT_TYPE = True         !   [Boolean] default = True</span>
<span id="L1337">                                ! If true, use a structure with elements that describe effective face areas from</span>
<span id="L1338">                                ! the summed continuity solver as a function the barotropic flow in coupling</span>
<span id="L1339">                                ! between the barotropic and baroclinic flow.  This is only used if SPLIT is</span>
<span id="L1340">                                ! true.</span>
<span id="L1341">INTEGRAL_BT_CONTINUITY = False  !   [Boolean] default = False</span>
<span id="L1342">                                ! If true, use the time-integrated velocity over the barotropic steps to</span>
<span id="L1343">                                ! determine the integrated transports used to update the continuity equation.</span>
<span id="L1344">                                ! Otherwise the transports are the sum of the transports based on a series of</span>
<span id="L1345">                                ! instantaneous velocities and the BT_CONT_TYPE for transports.  This is only</span>
<span id="L1346">                                ! valid if USE_BT_CONT_TYPE = True.</span>
<span id="L1347">BOUND_BT_CORRECTION = True      !   [Boolean] default = False</span>
<span id="L1348">                                ! If true, the corrective pseudo mass-fluxes into the barotropic solver are</span>
<span id="L1349">                                ! limited to values that require less than maxCFL_BT_cont to be accommodated.</span>
<span id="L1350">BT_CONT_CORR_BOUNDS = True      !   [Boolean] default = True</span>
<span id="L1351">                                ! If true, and BOUND_BT_CORRECTION is true, use the BT_cont_type variables to</span>
<span id="L1352">                                ! set limits determined by MAXCFL_BT_CONT on the CFL number of the velocities</span>
<span id="L1353">                                ! that are likely to be driven by the corrective mass fluxes.</span>
<span id="L1354">ADJUST_BT_CONT = False          !   [Boolean] default = False</span>
<span id="L1355">                                ! If true, adjust the curve fit to the BT_cont type that is used by the</span>
<span id="L1356">                                ! barotropic solver to match the transport about which the flow is being</span>
<span id="L1357">                                ! linearized.</span>
<span id="L1358">GRADUAL_BT_ICS = False          !   [Boolean] default = False</span>
<span id="L1359">                                ! If true, adjust the initial conditions for the barotropic solver to the values</span>
<span id="L1360">                                ! from the layered solution over a whole timestep instead of instantly. This is</span>
<span id="L1361">                                ! a decent approximation to the inclusion of sum(u dh_dt) while also correcting</span>
<span id="L1362">                                ! for truncation errors.</span>
<span id="L1363">BT_USE_VISC_REM_U_UH0 = False   !   [Boolean] default = False</span>
<span id="L1364">                                ! If true, use the viscous remnants when estimating the barotropic velocities</span>
<span id="L1365">                                ! that were used to calculate uh0 and vh0.  False is probably the better choice.</span>
<span id="L1366">BT_PROJECT_VELOCITY = True      !   [Boolean] default = False</span>
<span id="L1367">                                ! If true, step the barotropic velocity first and project out the velocity</span>
<span id="L1368">                                ! tendency by 1+BEBT when calculating the transport.  The default (false) is to</span>
<span id="L1369">                                ! use a predictor continuity step to find the pressure field, and then to do a</span>
<span id="L1370">                                ! corrector continuity step using a weighted average of the old and new</span>
<span id="L1371">                                ! velocities, with weights of (1-BEBT) and BEBT.</span>
<span id="L1372">BT_NONLIN_STRESS = False        !   [Boolean] default = False</span>
<span id="L1373">                                ! If true, use the full depth of the ocean at the start of the barotropic step</span>
<span id="L1374">                                ! when calculating the surface stress contribution to the barotropic</span>
<span id="L1375">                                ! acclerations.  Otherwise use the depth based on bathyT.</span>
<span id="L1376">DYNAMIC_SURFACE_PRESSURE = False !   [Boolean] default = False</span>
<span id="L1377">                                ! If true, add a dynamic pressure due to a viscous ice shelf, for instance.</span>
<span id="L1378">BT_CORIOLIS_SCALE = 1.0         !   [nondim] default = 1.0</span>
<span id="L1379">                                ! A factor by which the barotropic Coriolis anomaly terms are scaled.</span>
<span id="L1380">BAROTROPIC_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1381">                                ! The vintage of the expressions in the barotropic solver. Values below 20190101</span>
<span id="L1382">                                ! recover the answers from the end of 2018, while higher values use more</span>
<span id="L1383">                                ! efficient or general expressions.</span>
<span id="L1384">VISC_REM_BT_WEIGHT_BUG = True   !   [Boolean] default = True</span>
<span id="L1385">                                ! If true, recover a bug in barotropic solver that uses an unnormalized weight</span>
<span id="L1386">                                ! function for vertical averages of baroclinic velocity and forcing. Default of</span>
<span id="L1387">                                ! this flag is set by VISC_REM_BUG.</span>
<span id="L1388">TIDAL_SAL_FLATHER = False       !   [Boolean] default = False</span>
<span id="L1389">                                ! If true, then apply adjustments to the external gravity wave speed used with</span>
<span id="L1390">                                ! the Flather OBC routine consistent with the barotropic solver. This applies to</span>
<span id="L1391">                                ! cases with  tidal forcing using the scalar self-attraction approximation. The</span>
<span id="L1392">                                ! default is currently False in order to retain previous answers but should be</span>
<span id="L1393">                                ! set to True for new experiments</span>
<span id="L1394">SADOURNY = True                 !   [Boolean] default = True</span>
<span id="L1395">                                ! If true, the Coriolis terms are discretized with the Sadourny (1975) energy</span>
<span id="L1396">                                ! conserving scheme, otherwise the Arakawa &amp; Hsu scheme is used.  If the</span>
<span id="L1397">                                ! internal deformation radius is not resolved, the Sadourny scheme should</span>
<span id="L1398">                                ! probably be used.</span>
<span id="L1399">BT_THICK_SCHEME = &quot;HYBRID&quot;      ! default = &quot;FROM_BT_CONT&quot;</span>
<span id="L1400">                                ! A string describing the scheme that is used to set the open face areas used</span>
<span id="L1401">                                ! for barotropic transport and the relative weights of the accelerations. Valid</span>
<span id="L1402">                                ! values are:</span>
<span id="L1403">                                !    ARITHMETIC - arithmetic mean layer thicknesses</span>
<span id="L1404">                                !    HARMONIC - harmonic mean layer thicknesses</span>
<span id="L1405">                                !    HYBRID (the default) - use arithmetic means for</span>
<span id="L1406">                                !       layers above the shallowest bottom, the harmonic</span>
<span id="L1407">                                !       mean for layers below, and a weighted average for</span>
<span id="L1408">                                !       layers that straddle that depth</span>
<span id="L1409">                                !    FROM_BT_CONT - use the average thicknesses kept</span>
<span id="L1410">                                !       in the h_u and h_v fields of the BT_cont_type</span>
<span id="L1411">BT_STRONG_DRAG = False          !   [Boolean] default = False</span>
<span id="L1412">                                ! If true, use a stronger estimate of the retarding effects of strong bottom</span>
<span id="L1413">                                ! drag, by making it implicit with the barotropic time-step instead of implicit</span>
<span id="L1414">                                ! with the baroclinic time-step and dividing by the number of barotropic steps.</span>
<span id="L1415">BT_LINEAR_WAVE_DRAG = False     !   [Boolean] default = False</span>
<span id="L1416">                                ! If true, apply a linear drag to the barotropic velocities, using rates set by</span>
<span id="L1417">                                ! lin_drag_u &amp; _v divided by the depth of the ocean.  This was introduced to</span>
<span id="L1418">                                ! facilitate tide modeling.</span>
<span id="L1419">BT_LINEAR_FREQ_DRAG = False     !   [Boolean] default = False</span>
<span id="L1420">                                ! If true, apply frequency-dependent drag to the tidal velocities. The streaming</span>
<span id="L1421">                                ! band-pass filter must be turned on.</span>
<span id="L1422">CLIP_BT_VELOCITY = False        !   [Boolean] default = False</span>
<span id="L1423">                                ! If true, limit any velocity components that exceed CFL_TRUNCATE.  This should</span>
<span id="L1424">                                ! only be used as a desperate debugging measure.</span>
<span id="L1425">MAXCFL_BT_CONT = 0.25           !   [nondim] default = 0.25</span>
<span id="L1426">                                ! The maximum permitted CFL number associated with the barotropic accelerations</span>
<span id="L1427">                                ! from the summed velocities times the time-derivatives of thicknesses.</span>
<span id="L1428">DT_BT_FILTER = -0.25            !   [sec or nondim] default = -0.25</span>
<span id="L1429">                                ! A time-scale over which the barotropic mode solutions are filtered, in seconds</span>
<span id="L1430">                                ! if positive, or as a fraction of DT if negative. When used this can never be</span>
<span id="L1431">                                ! taken to be longer than 2*dt.  Set this to 0 to apply no filtering.</span>
<span id="L1432">G_BT_EXTRA = 0.0                !   [nondim] default = 0.0</span>
<span id="L1433">                                ! A nondimensional factor by which gtot is enhanced.</span>
<span id="L1434">SSH_EXTRA = 1.0                 !   [m] default = 1.0</span>
<span id="L1435">                                ! An estimate of how much higher SSH might get, for use in calculating the safe</span>
<span id="L1436">                                ! external wave speed. The default is the minimum of 10 m or 5% of</span>
<span id="L1437">                                ! MAXIMUM_DEPTH.</span>
<span id="L1438">LINEARIZED_BT_CORIOLIS = True   !   [Boolean] default = True</span>
<span id="L1439">                                ! If true use the bottom depth instead of the total water column thickness in</span>
<span id="L1440">                                ! the barotropic Coriolis term calculations.</span>
<span id="L1441">BEBT = 0.2                      !   [nondim] default = 0.1</span>
<span id="L1442">                                ! BEBT determines whether the barotropic time stepping uses the forward-backward</span>
<span id="L1443">                                ! time-stepping scheme or a backward Euler scheme. BEBT is valid in the range</span>
<span id="L1444">                                ! from 0 (for a forward-backward treatment of nonrotating gravity waves) to 1</span>
<span id="L1445">                                ! (for a backward Euler treatment). In practice, BEBT must be greater than about</span>
<span id="L1446">                                ! 0.05.</span>
<span id="L1447">DTBT = 5.0                      !   [s or nondim] default = -0.98</span>
<span id="L1448">                                ! The barotropic time step, in s. DTBT is only used with the split explicit time</span>
<span id="L1449">                                ! stepping. To set the time step automatically based the maximum stable value</span>
<span id="L1450">                                ! use 0, or a negative value gives the fraction of the stable value. Setting</span>
<span id="L1451">                                ! DTBT to 0 is the same as setting it to -0.98. The value of DTBT that will</span>
<span id="L1452">                                ! actually be used is an integer fraction of DT, rounding down.</span>
<span id="L1453">BT_USE_OLD_CORIOLIS_BRACKET_BUG = False !   [Boolean] default = False</span>
<span id="L1454">                                ! If True, use an order of operations that is not bitwise rotationally symmetric</span>
<span id="L1455">                                ! in the meridional Coriolis term of the barotropic solver.</span>
<span id="L1456">MASK_COASTAL_PRESSURE_FORCE = False !   [Boolean] default = False</span>
<span id="L1457">                                ! If true, use the land masks to zero out the diagnosed barotropic pressure</span>
<span id="L1458">                                ! gradient accelerations at coastal or land points.  This changes diagnostics</span>
<span id="L1459">                                ! and improves the reproducibility of certain debugging checksums, but it does</span>
<span id="L1460">                                ! not alter the solutions themselves.</span>
<span id="L1461"></span>
<span id="L1462">! === module MOM_mixed_layer_restrat ===</span>
<span id="L1463">MIXEDLAYER_RESTRAT = False      !   [Boolean] default = False</span>
<span id="L1464">                                ! If true, a density-gradient dependent re-stratifying flow is imposed in the</span>
<span id="L1465">                                ! mixed layer. Can be used in ALE mode without restriction but in layer mode can</span>
<span id="L1466">                                ! only be used if BULKMIXEDLAYER is true.</span>
<span id="L1467"></span>
<span id="L1468">! === module MOM_diagnostics ===</span>
<span id="L1469">DIAG_EBT_MONO_N2_COLUMN_FRACTION = 0.0 !   [nondim] default = 0.0</span>
<span id="L1470">                                ! The lower fraction of water column over which N2 is limited as monotonic for</span>
<span id="L1471">                                ! the purposes of calculating the equivalent barotropic wave speed.</span>
<span id="L1472">DIAG_EBT_MONO_N2_DEPTH = -1.0   !   [m] default = -1.0</span>
<span id="L1473">                                ! The depth below which N2 is limited as monotonic for the purposes of</span>
<span id="L1474">                                ! calculating the equivalent barotropic wave speed.</span>
<span id="L1475">INTERNAL_WAVE_SPEED_TOL = 0.001 !   [nondim] default = 0.001</span>
<span id="L1476">                                ! The fractional tolerance for finding the wave speeds.</span>
<span id="L1477">INTERNAL_WAVE_SPEED_MIN = 0.0   !   [m s-1] default = 0.0</span>
<span id="L1478">                                ! A floor in the first mode speed below which 0 used instead.</span>
<span id="L1479">INTERNAL_WAVE_SPEED_BETTER_EST = True !   [Boolean] default = True</span>
<span id="L1480">                                ! If true, use a more robust estimate of the first mode wave speed as the</span>
<span id="L1481">                                ! starting point for iterations.</span>
<span id="L1482">INTWAVE_REMAPPING_USE_OM4_SUBCELLS = True !   [Boolean] default = True</span>
<span id="L1483">                                ! If true, use the OM4 remapping-via-subcells algorithm for calculating EBT</span>
<span id="L1484">                                ! structure. See REMAPPING_USE_OM4_SUBCELLS for details. We recommend setting</span>
<span id="L1485">                                ! this option to false.</span>
<span id="L1486"></span>
<span id="L1487">! === module MOM_diabatic_driver ===</span>
<span id="L1488">! The following parameters are used for diabatic processes.</span>
<span id="L1489">USE_LEGACY_DIABATIC_DRIVER = True !   [Boolean] default = True</span>
<span id="L1490">                                ! If true, use a legacy version of the diabatic subroutine. This is temporary</span>
<span id="L1491">                                ! and is needed to avoid change in answers.</span>
<span id="L1492">ENERGETICS_SFC_PBL = False      !   [Boolean] default = False</span>
<span id="L1493">                                ! If true, use an implied energetics planetary boundary layer scheme to</span>
<span id="L1494">                                ! determine the diffusivity and viscosity in the surface boundary layer.</span>
<span id="L1495">EPBL_IS_ADDITIVE = True         !   [Boolean] default = True</span>
<span id="L1496">                                ! If true, the diffusivity from ePBL is added to all other diffusivities.</span>
<span id="L1497">                                ! Otherwise, the larger of kappa-shear and ePBL diffusivities are used.</span>
<span id="L1498">INTERNAL_TIDES = False          !   [Boolean] default = False</span>
<span id="L1499">                                ! If true, use the code that advances a separate set of equations for the</span>
<span id="L1500">                                ! internal tide energy density.</span>
<span id="L1501">MASSLESS_MATCH_TARGETS = True   !   [Boolean] default = True</span>
<span id="L1502">                                ! If true, the temperature and salinity of massless layers are kept consistent</span>
<span id="L1503">                                ! with their target densities. Otherwise the properties of massless layers</span>
<span id="L1504">                                ! evolve diffusively to match massive neighboring layers.</span>
<span id="L1505">AGGREGATE_FW_FORCING = True     !   [Boolean] default = True</span>
<span id="L1506">                                ! If true, the net incoming and outgoing fresh water fluxes are combined and</span>
<span id="L1507">                                ! applied as either incoming or outgoing depending on the sign of the net. If</span>
<span id="L1508">                                ! false, the net incoming fresh water flux is added to the model and thereafter</span>
<span id="L1509">                                ! the net outgoing is removed from the topmost non-vanished layers of the</span>
<span id="L1510">                                ! updated state.</span>
<span id="L1511">MIX_BOUNDARY_TRACERS = True     !   [Boolean] default = True</span>
<span id="L1512">                                ! If true, mix the passive tracers in massless layers at the bottom into the</span>
<span id="L1513">                                ! interior as though a diffusivity of KD_MIN_TR were operating.</span>
<span id="L1514">MIX_BOUNDARY_TRACER_ALE = False !   [Boolean] default = False</span>
<span id="L1515">                                ! If true and in ALE mode, mix the passive tracers in massless layers at the</span>
<span id="L1516">                                ! bottom into the interior as though a diffusivity of KD_MIN_TR were operating.</span>
<span id="L1517">KD_MIN_TR = 0.0                 !   [m2 s-1] default = 0.0</span>
<span id="L1518">                                ! A minimal diffusivity that should always be applied to tracers, especially in</span>
<span id="L1519">                                ! massless layers near the bottom. The default is 0.1*KD.</span>
<span id="L1520">KD_BBL_TR = 0.0                 !   [m2 s-1] default = 0.0</span>
<span id="L1521">                                ! A bottom boundary layer tracer diffusivity that will allow for explicitly</span>
<span id="L1522">                                ! specified bottom fluxes. The entrainment at the bottom is at least</span>
<span id="L1523">                                ! sqrt(Kd_BBL_tr*dt) over the same distance.</span>
<span id="L1524">TRACER_TRIDIAG = False          !   [Boolean] default = False</span>
<span id="L1525">                                ! If true, use the passive tracer tridiagonal solver for T and S</span>
<span id="L1526">MINIMUM_FORCING_DEPTH = 0.001   !   [m] default = 0.001</span>
<span id="L1527">                                ! The smallest depth over which forcing can be applied. This only takes effect</span>
<span id="L1528">                                ! when near-surface layers become thin relative to this scale, in which case the</span>
<span id="L1529">                                ! forcing tendencies scaled down by distributing the forcing over this depth</span>
<span id="L1530">                                ! scale.</span>
<span id="L1531">EVAP_CFL_LIMIT = 0.8            !   [nondim] default = 0.8</span>
<span id="L1532">                                ! The largest fraction of a layer than can be lost to forcing (e.g. evaporation,</span>
<span id="L1533">                                ! sea-ice formation) in one time-step. The unused mass loss is passed down</span>
<span id="L1534">                                ! through the column.</span>
<span id="L1535">MLD_EN_VALS = 25.0, 2500.0, 2.5E+05 !   [J/m2] default = 25.0, 2500.0, 2.5E+05</span>
<span id="L1536">                                ! The energy values used to compute MLDs.  If not set (or all set to 0.), the</span>
<span id="L1537">                                ! default will overwrite to 25., 2500., 250000.</span>
<span id="L1538">BMLD_EN_VALS = 25.0, 2500.0, 2.5E+05 !   [J/m2] default = 25.0, 2500.0, 2.5E+05</span>
<span id="L1539">                                ! The energy values used to compute Bottom MLDs.  If not set (or all set to 0.),</span>
<span id="L1540">                                ! the default will overwrite to 25., 2500., 250000.</span>
<span id="L1541">DIAG_MLD_DENSITY_DIFF = 0.1     !   [kg/m3] default = 0.1</span>
<span id="L1542">                                ! The density difference used to determine a diagnostic mixed layer depth,</span>
<span id="L1543">                                ! MLD_user, following the definition of Levitus 1982. The MLD is the depth at</span>
<span id="L1544">                                ! which the density is larger than the surface density by the specified amount.</span>
<span id="L1545">DIAG_DEPTH_SUBML_N2 = 50.0      !   [m] default = 50.0</span>
<span id="L1546">                                ! The distance over which to calculate a diagnostic of the stratification at the</span>
<span id="L1547">                                ! base of the mixed layer.</span>
<span id="L1548"></span>
<span id="L1549">! === module MOM_CVMix_KPP ===</span>
<span id="L1550">! This is the MOM wrapper to CVMix:KPP</span>
<span id="L1551">! See http://cvmix.github.io/</span>
<span id="L1552">USE_KPP = False                 !   [Boolean] default = False</span>
<span id="L1553">                                ! If true, turns on the [CVMix] KPP scheme of Large et al., 1994, to calculate</span>
<span id="L1554">                                ! diffusivities and non-local transport in the OBL.</span>
<span id="L1555"></span>
<span id="L1556">! === module MOM_CVMix_conv ===</span>
<span id="L1557">! Parameterization of enhanced mixing due to convection via CVMix</span>
<span id="L1558">USE_CVMix_CONVECTION = False    !   [Boolean] default = False</span>
<span id="L1559">                                ! If true, turns on the enhanced mixing due to convection via CVMix. This scheme</span>
<span id="L1560">                                ! increases diapycnal diffs./viscs. at statically unstable interfaces. Relevant</span>
<span id="L1561">                                ! parameters are contained in the CVMix_CONVECTION% parameter block.</span>
<span id="L1562"></span>
<span id="L1563">! === module MOM_set_diffusivity ===</span>
<span id="L1564">FLUX_RI_MAX = 0.2               !   [nondim] default = 0.2</span>
<span id="L1565">                                ! The flux Richardson number where the stratification is large enough that N2 &gt;</span>
<span id="L1566">                                ! omega2.  The full expression for the Flux Richardson number is usually</span>
<span id="L1567">                                ! FLUX_RI_MAX*N2/(N2+OMEGA2).</span>
<span id="L1568">SET_DIFF_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1569">                                ! The vintage of the order of arithmetic and expressions in the set diffusivity</span>
<span id="L1570">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L1571">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L1572">                                ! Values above 20250301 also use less confusing expressions to set the</span>
<span id="L1573">                                ! bottom-drag generated diffusivity when USE_LOTW_BBL_DIFFUSIVITY is false.</span>
<span id="L1574"></span>
<span id="L1575">! === module MOM_tidal_mixing ===</span>
<span id="L1576">! Vertical Tidal Mixing Parameterization</span>
<span id="L1577">USE_CVMix_TIDAL = False         !   [Boolean] default = False</span>
<span id="L1578">                                ! If true, turns on tidal mixing via CVMix</span>
<span id="L1579">INT_TIDE_DISSIPATION = False    !   [Boolean] default = False</span>
<span id="L1580">                                ! If true, use an internal tidal dissipation scheme to drive diapycnal mixing,</span>
<span id="L1581">                                ! along the lines of St. Laurent et al. (2002) and Simmons et al. (2004).</span>
<span id="L1582">ML_RADIATION = False            !   [Boolean] default = False</span>
<span id="L1583">                                ! If true, allow a fraction of TKE available from wind work to penetrate below</span>
<span id="L1584">                                ! the base of the mixed layer with a vertical decay scale determined by the</span>
<span id="L1585">                                ! minimum of: (1) The depth of the mixed layer, (2) an Ekman length scale.</span>
<span id="L1586">BBL_EFFIC = 0.0                 !   [nondim] default = 0.2</span>
<span id="L1587">                                ! The efficiency with which the energy extracted by bottom drag drives BBL</span>
<span id="L1588">                                ! diffusion.  This is only used if BOTTOMDRAGLAW is true.</span>
<span id="L1589">BBL_MIXING_MAX_DECAY = 200.0    !   [m] default = 200.0</span>
<span id="L1590">                                ! The maximum decay scale for the BBL diffusion, or 0 to allow the mixing to</span>
<span id="L1591">                                ! penetrate as far as stratification and rotation permit.  The default for now</span>
<span id="L1592">                                ! is 200 m. This is only used if BOTTOMDRAGLAW is true.</span>
<span id="L1593">BBL_MIXING_AS_MAX = True        !   [Boolean] default = True</span>
<span id="L1594">                                ! If true, take the maximum of the diffusivity from the BBL mixing and the other</span>
<span id="L1595">                                ! diffusivities. Otherwise, diffusivity from the BBL_mixing is simply added.</span>
<span id="L1596">USE_LOTW_BBL_DIFFUSIVITY = False !   [Boolean] default = False</span>
<span id="L1597">                                ! If true, uses a simple, imprecise but non-coordinate dependent, model of BBL</span>
<span id="L1598">                                ! mixing diffusivity based on Law of the Wall. Otherwise, uses the original BBL</span>
<span id="L1599">                                ! scheme.</span>
<span id="L1600">DZ_BBL_AVG_MIN = 0.0            !   [m] default = 0.0</span>
<span id="L1601">                                ! A minimal distance over which to average to determine the average bottom</span>
<span id="L1602">                                ! boundary layer density.</span>
<span id="L1603">SIMPLE_TKE_TO_KD = False        !   [Boolean] default = False</span>
<span id="L1604">                                ! If true, uses a simple estimate of Kd/TKE that will work for arbitrary</span>
<span id="L1605">                                ! vertical coordinates. If false, calculates Kd/TKE and bounds based on exact</span>
<span id="L1606">                                ! energetics for an isopycnal layer-formulation.</span>
<span id="L1607"></span>
<span id="L1608">! === module MOM_bkgnd_mixing ===</span>
<span id="L1609">! Adding static vertical background mixing coefficients</span>
<span id="L1610">KD = 0.0                        !   [m2 s-1] default = 0.0</span>
<span id="L1611">                                ! The background diapycnal diffusivity of density in the interior. Zero or the</span>
<span id="L1612">                                ! molecular value, ~1e-7 m2 s-1, may be used.</span>
<span id="L1613">KD_MIN = 0.0                    !   [m2 s-1] default = 0.0</span>
<span id="L1614">                                ! The minimum diapycnal diffusivity.</span>
<span id="L1615">KD_ML_TOT = 0.0                 !   [m2 s-1] default = 0.0</span>
<span id="L1616">                                ! The total diapcynal diffusivity in the surface mixed layer when there is not a</span>
<span id="L1617">                                ! physically based parameterization of mixing in the mixed layer, such as bulk</span>
<span id="L1618">                                ! mixed layer or KPP or ePBL.</span>
<span id="L1619">BRYAN_LEWIS_DIFFUSIVITY = False !   [Boolean] default = False</span>
<span id="L1620">                                ! If true, use a Bryan &amp; Lewis (JGR 1979) like tanh profile of background</span>
<span id="L1621">                                ! diapycnal diffusivity with depth. This is done via CVMix.</span>
<span id="L1622">HORIZ_VARYING_BACKGROUND = False !   [Boolean] default = False</span>
<span id="L1623">                                ! If true, apply vertically uniform, latitude-dependent background diffusivity,</span>
<span id="L1624">                                ! as described in Danabasoglu et al., 2012</span>
<span id="L1625">PRANDTL_BKGND = 1.0             !   [nondim] default = 1.0</span>
<span id="L1626">                                ! Turbulent Prandtl number used to convert vertical background diffusivities</span>
<span id="L1627">                                ! into viscosities.</span>
<span id="L1628">HENYEY_IGW_BACKGROUND = False   !   [Boolean] default = False</span>
<span id="L1629">                                ! If true, use a latitude-dependent scaling for the near surface background</span>
<span id="L1630">                                ! diffusivity, as described in Harrison &amp; Hallberg, JPO 2008.</span>
<span id="L1631">KD_TANH_LAT_FN = False          !   [Boolean] default = False</span>
<span id="L1632">                                ! If true, use a tanh dependence of Kd_sfc on latitude, like CM2.1/CM2M.  There</span>
<span id="L1633">                                ! is no physical justification for this form, and it can not be used with</span>
<span id="L1634">                                ! HENYEY_IGW_BACKGROUND.</span>
<span id="L1635">KD_MAX = -1.0                   !   [m2 s-1] default = -1.0</span>
<span id="L1636">                                ! The maximum permitted increment for the diapycnal diffusivity from TKE-based</span>
<span id="L1637">                                ! parameterizations, or a negative value for no limit.</span>
<span id="L1638">KD_ADD = 0.0                    !   [m2 s-1] default = 0.0</span>
<span id="L1639">                                ! A uniform diapycnal diffusivity that is added everywhere without any filtering</span>
<span id="L1640">                                ! or scaling.</span>
<span id="L1641">USER_CHANGE_DIFFUSIVITY = False !   [Boolean] default = False</span>
<span id="L1642">                                ! If true, call user-defined code to change the diffusivity.</span>
<span id="L1643">DISSIPATION_MIN = 0.0           !   [W m-3] default = 0.0</span>
<span id="L1644">                                ! The minimum dissipation by which to determine a lower bound of Kd (a floor).</span>
<span id="L1645">DISSIPATION_N0 = 0.0            !   [W m-3] default = 0.0</span>
<span id="L1646">                                ! The intercept when N=0 of the N-dependent expression used to set a minimum</span>
<span id="L1647">                                ! dissipation by which to determine a lower bound of Kd (a floor): A in eps_min</span>
<span id="L1648">                                ! = A + B*N.</span>
<span id="L1649">DISSIPATION_N1 = 0.0            !   [J m-3] default = 0.0</span>
<span id="L1650">                                ! The coefficient multiplying N, following Gargett, used to set a minimum</span>
<span id="L1651">                                ! dissipation by which to determine a lower bound of Kd (a floor): B in eps_min</span>
<span id="L1652">                                ! = A + B*N</span>
<span id="L1653">DISSIPATION_KD_MIN = 0.0        !   [m2 s-1] default = 0.0</span>
<span id="L1654">                                ! The minimum vertical diffusivity applied as a floor.</span>
<span id="L1655">DOUBLE_DIFFUSION = False        !   [Boolean] default = False</span>
<span id="L1656">                                ! If true, increase diffusivites for temperature or salinity based on the</span>
<span id="L1657">                                ! double-diffusive parameterization described in Large et al. (1994).</span>
<span id="L1658"></span>
<span id="L1659">! === module MOM_kappa_shear ===</span>
<span id="L1660">! Parameterization of shear-driven turbulence following Jackson, Hallberg and Legg, JPO 2008</span>
<span id="L1661">USE_JACKSON_PARAM = False       !   [Boolean] default = False</span>
<span id="L1662">                                ! If true, use the Jackson-Hallberg-Legg (JPO 2008) shear mixing</span>
<span id="L1663">                                ! parameterization.</span>
<span id="L1664">VERTEX_SHEAR_THICKNESS_MEAN = False !   [Boolean] default = False</span>
<span id="L1665">                                ! If true, apply thickness weighting to horizontal averagings of diffusivity to</span>
<span id="L1666">                                ! tracer points in the kappa shear solver.</span>
<span id="L1667">KD_SEED_KAPPA_SHEAR = 1.0       !   [m2 s-1] default = 1.0</span>
<span id="L1668">                                ! A moderately large seed value of diapycnal diffusivity that is used as a</span>
<span id="L1669">                                ! starting turbulent diffusivity in the iterations to find an energetically</span>
<span id="L1670">                                ! constrained solution for the shear-driven diffusivity.</span>
<span id="L1671">LZ_RESCALE = 1.0                !   [nondim] default = 1.0</span>
<span id="L1672">                                ! A coefficient to rescale the distance to the nearest solid boundary. This</span>
<span id="L1673">                                ! adjustment is to account for regions where 3 dimensional turbulence prevents</span>
<span id="L1674">                                ! the growth of shear instabilies [nondim].</span>
<span id="L1675">TKE_BACKGROUND = 0.0            !   [m2 s-2] default = 0.0</span>
<span id="L1676">                                ! A background level of TKE used in the first iteration of the kappa equation.</span>
<span id="L1677">                                ! TKE_BACKGROUND could be 0.</span>
<span id="L1678"></span>
<span id="L1679">! === module MOM_CVMix_shear ===</span>
<span id="L1680">! Parameterization of shear-driven turbulence via CVMix (various options)</span>
<span id="L1681">USE_LMD94 = False               !   [Boolean] default = False</span>
<span id="L1682">                                ! If true, use the Large-McWilliams-Doney (JGR 1994) shear mixing</span>
<span id="L1683">                                ! parameterization.</span>
<span id="L1684">USE_PP81 = False                !   [Boolean] default = False</span>
<span id="L1685">                                ! If true, use the Pacanowski and Philander (JPO 1981) shear mixing</span>
<span id="L1686">                                ! parameterization.</span>
<span id="L1687"></span>
<span id="L1688">! === module MOM_CVMix_ddiff ===</span>
<span id="L1689">! Parameterization of mixing due to double diffusion processes via CVMix</span>
<span id="L1690">USE_CVMIX_DDIFF = False         !   [Boolean] default = False</span>
<span id="L1691">                                ! If true, turns on double diffusive processes via CVMix. Note that double</span>
<span id="L1692">                                ! diffusive processes on viscosity are ignored in CVMix, see</span>
<span id="L1693">                                ! http://cvmix.github.io/ for justification.</span>
<span id="L1694"></span>
<span id="L1695">! === module MOM_diabatic_aux ===</span>
<span id="L1696">! The following parameters are used for auxiliary diabatic processes.</span>
<span id="L1697">RECLAIM_FRAZIL = True           !   [Boolean] default = True</span>
<span id="L1698">                                ! If true, try to use any frazil heat deficit to cool any overlying layers down</span>
<span id="L1699">                                ! to the freezing point, thereby avoiding the creation of thin ice when the SST</span>
<span id="L1700">                                ! is above the freezing point.</span>
<span id="L1701">SALT_EXTRACTION_LIMIT = 0.9999  !   [nondim] default = 0.9999</span>
<span id="L1702">                                ! An upper limit on the fraction of the salt in a layer that can be lost to the</span>
<span id="L1703">                                ! net surface salt fluxes within a timestep.</span>
<span id="L1704">PRESSURE_DEPENDENT_FRAZIL = False !   [Boolean] default = False</span>
<span id="L1705">                                ! If true, use a pressure dependent freezing temperature when making frazil. The</span>
<span id="L1706">                                ! default is false, which will be faster but is inappropriate with ice-shelf</span>
<span id="L1707">                                ! cavities.</span>
<span id="L1708">USE_RIVER_HEAT_CONTENT = False  !   [Boolean] default = False</span>
<span id="L1709">                                ! If true, use the fluxes%runoff_Hflx field to set the heat carried by runoff,</span>
<span id="L1710">                                ! instead of using SST*CP*liq_runoff.</span>
<span id="L1711">USE_CALVING_HEAT_CONTENT = False !   [Boolean] default = False</span>
<span id="L1712">                                ! If true, use the fluxes%calving_Hflx field to set the heat carried by runoff,</span>
<span id="L1713">                                ! instead of using SST*CP*froz_runoff.</span>
<span id="L1714">DO_BRINE_PLUME = False          !   [Boolean] default = False</span>
<span id="L1715">                                ! If true, use a brine plume parameterization from Nguyen et al., 2009.</span>
<span id="L1716">VAR_PEN_SW = False              !   [Boolean] default = False</span>
<span id="L1717">                                ! If true, use one of the CHL_A schemes specified by OPACITY_SCHEME to determine</span>
<span id="L1718">                                ! the e-folding depth of incoming short wave radiation.</span>
<span id="L1719"></span>
<span id="L1720">! === module MOM_regularize_layers ===</span>
<span id="L1721">REGULARIZE_SURFACE_LAYERS = False !   [Boolean] default = False</span>
<span id="L1722">                                ! If defined, vertically restructure the near-surface layers when they have too</span>
<span id="L1723">                                ! much lateral variations to allow for sensible lateral barotropic transports.</span>
<span id="L1724"></span>
<span id="L1725">! === module MOM_opacity ===</span>
<span id="L1726">EXP_OPACITY_SCHEME = &quot;SINGLE_EXP&quot; ! default = &quot;SINGLE_EXP&quot;</span>
<span id="L1727">                                ! This character string specifies which exponential opacity scheme to utilize.</span>
<span id="L1728">                                ! Currently valid options include:</span>
<span id="L1729">                                !        SINGLE_EXP - Single Exponent decay.</span>
<span id="L1730">                                !        DOUBLE_EXP - Double Exponent decay.</span>
<span id="L1731">PEN_SW_SCALE = 15.0             !   [m] default = 0.0</span>
<span id="L1732">                                ! The vertical absorption e-folding depth of the penetrating shortwave</span>
<span id="L1733">                                ! radiation.</span>
<span id="L1734">PEN_SW_FRAC = 0.42              !   [nondim] default = 0.0</span>
<span id="L1735">                                ! The fraction of the shortwave radiation that penetrates below the surface.</span>
<span id="L1736">PEN_SW_NBANDS = 1               ! default = 1</span>
<span id="L1737">                                ! The number of bands of penetrating shortwave radiation.</span>
<span id="L1738">OPTICS_ANSWER_DATE = 99991231   ! default = 99991231</span>
<span id="L1739">                                ! The vintage of the order of arithmetic and expressions in the optics</span>
<span id="L1740">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L1741">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L1742">PEN_SW_FLUX_ABSORB = 2.5E-11    !   [degC m s-1] default = 2.5E-11</span>
<span id="L1743">                                ! A minimum remaining shortwave heating rate that will be simply absorbed in the</span>
<span id="L1744">                                ! next sufficiently thick layers for computational efficiency, instead of</span>
<span id="L1745">                                ! continuing to penetrate.  The default, 2.5e-11 degC m s-1, is about 1e-4 W m-2</span>
<span id="L1746">                                ! or 0.08 degC m century-1, but 0 is also a valid value.</span>
<span id="L1747">PEN_SW_ABSORB_MINTHICK = 1.0    !   [m] default = 1.0</span>
<span id="L1748">                                ! A thickness that is used to absorb the remaining penetrating shortwave heat</span>
<span id="L1749">                                ! flux when it drops below PEN_SW_FLUX_ABSORB.</span>
<span id="L1750">OPACITY_LAND_VALUE = 10.0       !   [m-1] default = 10.0</span>
<span id="L1751">                                ! The value to use for opacity over land. The default is 10 m-1 - a value for</span>
<span id="L1752">                                ! muddy water.</span>
<span id="L1753"></span>
<span id="L1754">! === module MOM_tracer_advect ===</span>
<span id="L1755">TRACER_ADVECTION_SCHEME = &quot;PLM&quot; ! default = &quot;PLM&quot;</span>
<span id="L1756">                                ! The horizontal transport scheme for tracers:</span>
<span id="L1757">                                !   PLM    - Piecewise Linear Method</span>
<span id="L1758">                                !   PPM:H3 - Piecewise Parabolic Method (Huyhn 3rd order)</span>
<span id="L1759">                                !   PPM    - Piecewise Parabolic Method (Colella-Woodward)</span>
<span id="L1760"></span>
<span id="L1761">! === module MOM_tracer_hor_diff ===</span>
<span id="L1762">KHTR = 0.0                      !   [m2 s-1] default = 0.0</span>
<span id="L1763">                                ! The background along-isopycnal tracer diffusivity.</span>
<span id="L1764">KHTR_MIN = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L1765">                                ! The minimum along-isopycnal tracer diffusivity.</span>
<span id="L1766">KHTR_MAX = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L1767">                                ! The maximum along-isopycnal tracer diffusivity. Set to a positive value to</span>
<span id="L1768">                                ! activate.</span>
<span id="L1769">KHTR_PASSIVITY_COEFF = 0.0      !   [nondim] default = 0.0</span>
<span id="L1770">                                ! The coefficient that scales deformation radius over grid-spacing in passivity,</span>
<span id="L1771">                                ! where passivity is the ratio between along isopycnal mixing of tracers to</span>
<span id="L1772">                                ! thickness mixing. A non-zero value enables this parameterization.</span>
<span id="L1773">KHTR_PASSIVITY_MIN = 0.5        !   [nondim] default = 0.5</span>
<span id="L1774">                                ! The minimum passivity which is the ratio between along isopycnal mixing of</span>
<span id="L1775">                                ! tracers to thickness mixing.</span>
<span id="L1776">DIFFUSE_ML_TO_INTERIOR = False  !   [Boolean] default = False</span>
<span id="L1777">                                ! If true, enable epipycnal mixing between the surface boundary layer and the</span>
<span id="L1778">                                ! interior.</span>
<span id="L1779">CHECK_DIFFUSIVE_CFL = False     !   [Boolean] default = False</span>
<span id="L1780">                                ! If true, use enough iterations the diffusion to ensure that the diffusive</span>
<span id="L1781">                                ! equivalent of the CFL limit is not violated.  If false, always use the greater</span>
<span id="L1782">                                ! of 1 or MAX_TR_DIFFUSION_CFL iteration.</span>
<span id="L1783">MAX_TR_DIFFUSION_CFL = -1.0     !   [nondim] default = -1.0</span>
<span id="L1784">                                ! If positive, locally limit the along-isopycnal tracer diffusivity to keep the</span>
<span id="L1785">                                ! diffusive CFL locally at or below this value.  The number of diffusive</span>
<span id="L1786">                                ! iterations is often this value or the next greater integer.</span>
<span id="L1787">RECALC_NEUTRAL_SURF = False     !   [Boolean] default = False</span>
<span id="L1788">                                ! If true, then recalculate the neutral surfaces if the</span>
<span id="L1789">                                ! diffusive CFL is exceeded. If false, assume that the</span>
<span id="L1790">                                ! positions of the surfaces do not change</span>
<span id="L1791"></span>
<span id="L1792">! === module MOM_neutral_diffusion ===</span>
<span id="L1793">! This module implements neutral diffusion of tracers</span>
<span id="L1794">USE_NEUTRAL_DIFFUSION = False   !   [Boolean] default = False</span>
<span id="L1795">                                ! If true, enables the neutral diffusion module.</span>
<span id="L1796"></span>
<span id="L1797">! === module MOM_hor_bnd_diffusion ===</span>
<span id="L1798">! This module implements horizontal diffusion of tracers near boundaries</span>
<span id="L1799">USE_HORIZONTAL_BOUNDARY_DIFFUSION = False !   [Boolean] default = False</span>
<span id="L1800">                                ! If true, enables the horizonal boundary tracer&#x27;s diffusion module.</span>
<span id="L1801">OBSOLETE_DIAGNOSTIC_IS_FATAL = True !   [Boolean] default = True</span>
<span id="L1802">                                ! If an obsolete diagnostic variable appears in the diag_table, cause a FATAL</span>
<span id="L1803">                                ! error rather than issue a WARNING.</span>
<span id="L1804"></span>
<span id="L1805">! === module MOM_sum_output ===</span>
<span id="L1806">CALCULATE_APE = True            !   [Boolean] default = True</span>
<span id="L1807">                                ! If true, calculate the available potential energy of the interfaces.  Setting</span>
<span id="L1808">                                ! this to false reduces the memory footprint of high-PE-count models</span>
<span id="L1809">                                ! dramatically.</span>
<span id="L1810">WRITE_STOCKS = True             !   [Boolean] default = True</span>
<span id="L1811">                                ! If true, write the integrated tracer amounts to stdout when the energy files</span>
<span id="L1812">                                ! are written.</span>
<span id="L1813">MAXTRUNC = 10                   !   [truncations save_interval-1] default = 0</span>
<span id="L1814">                                ! The run will be stopped, and the day set to a very large value if the velocity</span>
<span id="L1815">                                ! is truncated more than MAXTRUNC times between energy saves.  Set MAXTRUNC to 0</span>
<span id="L1816">                                ! to stop if there is any truncation of velocities.</span>
<span id="L1817">MAX_ENERGY = 0.0                !   [m2 s-2] default = 0.0</span>
<span id="L1818">                                ! The maximum permitted average energy per unit mass; the model will be stopped</span>
<span id="L1819">                                ! if there is more energy than this.  If zero or negative, this is set to</span>
<span id="L1820">                                ! 10*MAXVEL^2.</span>
<span id="L1821">MAXVEL = 10.0                   !   [m s-1] default = 3.0E+08</span>
<span id="L1822">                                ! The maximum velocity allowed before the velocity components are truncated.</span>
<span id="L1823">ENERGYFILE = &quot;ocean.stats&quot;      ! default = &quot;ocean.stats&quot;</span>
<span id="L1824">                                ! The file to use to write the energies and globally summed diagnostics.</span>
<span id="L1825">DATE_STAMPED_STDOUT = False     !   [Boolean] default = True</span>
<span id="L1826">                                ! If true, use dates (not times) in messages to stdout</span>
<span id="L1827">ISO_DATE_STAMPED_STDOUT = False !   [Boolean] default = False</span>
<span id="L1828">                                ! If true, use ISO formatted dates in messages to stdout</span>
<span id="L1829">TIMEUNIT = 3600.0               !   [s] default = 8.64E+04</span>
<span id="L1830">                                ! The time unit in seconds a number of input fields</span>
<span id="L1831">READ_DEPTH_LIST = False         !   [Boolean] default = False</span>
<span id="L1832">                                ! Read the depth list from a file if it exists or create that file otherwise.</span>
<span id="L1833">DEPTH_LIST_MIN_INC = 1.0E-10    !   [m] default = 1.0E-10</span>
<span id="L1834">                                ! The minimum increment between the depths of the entries in the depth-list</span>
<span id="L1835">                                ! file.</span>
<span id="L1836">ENERGYSAVEDAYS = 0.5            !   [hours] default = 24.0</span>
<span id="L1837">                                ! The interval in units of TIMEUNIT between saves of the energies of the run and</span>
<span id="L1838">                                ! other globally summed diagnostics.</span>
<span id="L1839">ENERGYSAVEDAYS_GEOMETRIC = 0.0  !   [hours] default = 0.0</span>
<span id="L1840">                                ! The starting interval in units of TIMEUNIT for the first call to save the</span>
<span id="L1841">                                ! energies of the run and other globally summed diagnostics. The interval</span>
<span id="L1842">                                ! increases by a factor of 2. after each call to write_energy.</span>
<span id="L1843"></span>
<span id="L1844">! === module ocean_stochastics_init ===</span>
<span id="L1845">DO_SPPT = False                 !   [Boolean] default = False</span>
<span id="L1846">                                ! If true, then stochastically perturb the thermodynamic tendencies of T,S, amd</span>
<span id="L1847">                                ! h.  Amplitude and correlations are controlled by the nam_stoch namelist in the</span>
<span id="L1848">                                ! UFS model only.</span>
<span id="L1849">DO_SKEB = False                 !   [Boolean] default = False</span>
<span id="L1850">                                ! If true, then stochastically perturb the currents using the stochastic kinetic</span>
<span id="L1851">                                ! energy backscatter scheme.</span>
<span id="L1852">PERT_EPBL = False               !   [Boolean] default = False</span>
<span id="L1853">                                ! If true, then stochastically perturb the kinetic energy production and</span>
<span id="L1854">                                ! dissipation terms.  Amplitude and correlations are controlled by the nam_stoch</span>
<span id="L1855">                                ! namelist in the UFS model only.</span>
<span id="L1856"></span>
<span id="L1857">! === module MOM_surface_forcing ===</span>
<span id="L1858">VARIABLE_WINDS = False          !   [Boolean] default = True</span>
<span id="L1859">                                ! If true, the winds vary in time after the initialization.</span>
<span id="L1860">VARIABLE_BUOYFORCE = False      !   [Boolean] default = True</span>
<span id="L1861">                                ! If true, the buoyancy forcing varies in time after the initialization of the</span>
<span id="L1862">                                ! model.</span>
<span id="L1863">BUOY_CONFIG = &quot;NONE&quot;            ! default = &quot;zero&quot;</span>
<span id="L1864">                                ! The character string that indicates how buoyancy forcing is specified.  Valid</span>
<span id="L1865">                                ! options include (file), (data_override), (zero), (const), (linear), (MESO),</span>
<span id="L1866">                                ! (SCM_CVmix_tests), (BFB), (dumbbell), (USER) and (NONE).</span>
<span id="L1867">WIND_CONFIG = &quot;zero&quot;            ! default = &quot;zero&quot;</span>
<span id="L1868">                                ! The character string that indicates how wind forcing is specified.  Valid</span>
<span id="L1869">                                ! options include (file), (data_override), (2gyre), (1gyre), (gyres), (zero),</span>
<span id="L1870">                                ! (const), (Neverworld), (scurves), (ideal_hurr), (SCM_CVmix_tests) and (USER).</span>
<span id="L1871">RESTOREBUOY = False             !   [Boolean] default = False</span>
<span id="L1872">                                ! If true, the buoyancy fluxes drive the model back toward some specified</span>
<span id="L1873">                                ! surface state with a rate given by FLUXCONST.</span>
<span id="L1874">LATENT_HEAT_FUSION = 3.34E+05   !   [J/kg] default = 3.34E+05</span>
<span id="L1875">                                ! The latent heat of fusion.</span>
<span id="L1876">LATENT_HEAT_VAPORIZATION = 2.5E+06 !   [J/kg] default = 2.5E+06</span>
<span id="L1877">                                ! The latent heat of fusion.</span>
<span id="L1878">GUST_CONST = 0.0                !   [Pa] default = 0.0</span>
<span id="L1879">                                ! The background gustiness in the winds.</span>
<span id="L1880">USTAR_GUSTLESS_BUG = False      !   [Boolean] default = False</span>
<span id="L1881">                                ! If true include a bug in the time-averaging of the gustless wind friction</span>
<span id="L1882">                                ! velocity</span>
<span id="L1883">READ_GUST_2D = False            !   [Boolean] default = False</span>
<span id="L1884">                                ! If true, use a 2-dimensional gustiness supplied from an input file</span>
<span id="L1885"></span>
<span id="L1886">! === module MOM_restart ===</span>
<span id="L1887">USE_WAVES = False               !   [Boolean] default = False</span>
<span id="L1888">                                ! If true, enables surface wave modules.</span>
<span id="L1889"></span>
<span id="L1890">! === module MOM_main (MOM_driver) ===</span>
<span id="L1891">DT_FORCING = 600.0              !   [s] default = 150.0</span>
<span id="L1892">                                ! The time step for changing forcing, coupling with other components, or</span>
<span id="L1893">                                ! potentially writing certain diagnostics. The default value is given by DT.</span>
<span id="L1894">DAYMAX = 2.0                    !   [hours]</span>
<span id="L1895">                                ! The final time of the whole simulation, in units of TIMEUNIT seconds.  This</span>
<span id="L1896">                                ! also sets the potential end time of the present run segment if the end time is</span>
<span id="L1897">                                ! not set via ocean_solo_nml in input.nml.</span>
<span id="L1898">SINGLE_STEPPING_CALL = True     !   [Boolean] default = True</span>
<span id="L1899">                                ! If true, advance the state of MOM with a single step including both dynamics</span>
<span id="L1900">                                ! and thermodynamics.  If false the two phases are advanced with separate calls.</span>
<span id="L1901">RESTART_CONTROL = 3             ! default = 1</span>
<span id="L1902">                                ! An integer whose bits encode which restart files are written. Add 2 (bit 1)</span>
<span id="L1903">                                ! for a time-stamped file, and odd (bit 0) for a non-time-stamped file. A</span>
<span id="L1904">                                ! non-time-stamped restart file is saved at the end of the run segment for any</span>
<span id="L1905">                                ! non-negative value.</span>
<span id="L1906">RESTINT = 240.0                 !   [hours] default = 0.0</span>
<span id="L1907">                                ! The interval between saves of the restart file in units of TIMEUNIT.  Use 0</span>
<span id="L1908">                                ! (the default) to not save incremental restart files at all.</span>
<span id="L1909">WRITE_CPU_STEPS = 1000          ! default = 1000</span>
<span id="L1910">                                ! The number of coupled timesteps between writing the cpu time. If this is not</span>
<span id="L1911">                                ! positive, do not check cpu time, and the segment run-length can not be set via</span>
<span id="L1912">                                ! an elapsed CPU time.</span>
<span id="L1913"></span>
<span id="L1914">! === module MOM_write_cputime ===</span>
<span id="L1915">MAXCPU = -1.0                   !   [wall-clock seconds] default = -1.0</span>
<span id="L1916">                                ! The maximum amount of cpu time per processor for which MOM should run before</span>
<span id="L1917">                                ! saving a restart file and quitting with a return value that indicates that a</span>
<span id="L1918">                                ! further run is required to complete the simulation. If automatic restarts are</span>
<span id="L1919">                                ! not desired, use a negative value for MAXCPU.  MAXCPU has units of wall-clock</span>
<span id="L1920">                                ! seconds, so the actual CPU time used is larger by a factor of the number of</span>
<span id="L1921">                                ! processors used.</span>
<span id="L1922">CPU_TIME_FILE = &quot;CPU_stats&quot;     ! default = &quot;CPU_stats&quot;</span>
<span id="L1923">                                ! The file into which CPU time is written.</span>
<span id="L1924"></span>
<span id="L1925">! === module MOM_file_parser ===</span>
<span id="L1926">SEND_LOG_TO_STDOUT = False      !   [Boolean] default = False</span>
<span id="L1927">                                ! If true, all log messages are also sent to stdout.</span>
<span id="L1928">DOCUMENT_FILE = &quot;MOM_parameter_doc&quot; ! default = &quot;MOM_parameter_doc&quot;</span>
<span id="L1929">                                ! The basename for files where run-time parameters, their settings, units and</span>
<span id="L1930">                                ! defaults are documented. Blank will disable all parameter documentation.</span>
<span id="L1931">COMPLETE_DOCUMENTATION = True   !   [Boolean] default = True</span>
<span id="L1932">                                ! If true, all run-time parameters are documented in MOM_parameter_doc.all .</span>
<span id="L1933">MINIMAL_DOCUMENTATION = True    !   [Boolean] default = True</span>
<span id="L1934">                                ! If true, non-default run-time parameters are documented in</span>
<span id="L1935">                                ! MOM_parameter_doc.short .</span>
</pre>
